import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {'url': forms.HiddenInput,}

    def clean_url(self):
        url = self.cleaned_data['url']
        
        # Make a HEAD request to get the Content-Type header
        try:
            response = requests.head(url, allow_redirects=True)
            content_type = response.headers.get('Content-Type', '').lower()
            # print('Content type is: ' + content_type)

            # Check if the Content-Type is an image
            if not content_type.startswith('image/'):
                raise forms.ValidationError('The given URL does not point to a valid image file.')
        
        except requests.RequestException:
            raise forms.ValidationError('Could not retrieve the URL. Please check if it is correct and accessible.')
        
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        
        # Extract the extension based on content type or fallback to the last part of the URL
        extension = image_url.rsplit('.', 1)[-1].lower() if '.' in image_url else 'jpg'
        image_name = f'{name}.{extension}'

        # Download image from the given URL
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)

        if commit:
            image.save()
        return image
