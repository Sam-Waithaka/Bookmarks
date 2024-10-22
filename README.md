
# BookMark - Django Social Website

**BookMark** is a social website built with Django, aiming to provide core social networking functionality. This project demonstrates how to implement user authentication and profile management using Django's built-in tools and customizations.

## Features

- **User Authentication**: Provides login, logout, password change, and password reset functionality using Django's built-in authentication system.
- **User Registration**: Allows users to sign up and create accounts.
- **User Profile Management**: Extends Django’s default `User` model with additional fields (like date of birth and profile picture).
- **Profile Editing**: Users can update their profile information and upload a profile picture.
- **Dashboard**: A user dashboard where users can view and manage their profile.

## Project Structure

The project includes the following key components:

1. **User Authentication**: Leveraging Django's built-in views for login, logout, and password management.
2. **Custom User Profiles**: Extending the default `User` model to allow additional user data storage (e.g., profile pictures).
3. **Media File Uploads**: Supporting user-uploaded profile pictures and other media through Django's media configuration.

## Setup and Installation

To run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd BookMark
   ```

2. **Install Dependencies**:
   Make sure you have a virtual environment set up and then install the project dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**:
   Apply the database migrations to set up the necessary tables.
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:
   Start the local Django development server.
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Media Files Configuration

To handle user-uploaded files (e.g., profile pictures), the following settings should be added to your `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Make sure your project includes proper configuration for handling static and media files during development and deployment.

## Templates

The templates used for user registration, login, dashboard, and profile editing should be stored under:

```
<project_root>/
    templates/
        account/
            login.html
            register.html
            register_done.html
            dashboard.html
            edit.html
```

These templates define the user interface and are rendered in the views handling user actions.

## License

This project is open-source and available under the MIT License.
