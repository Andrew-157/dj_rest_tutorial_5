# Set up Basic AUthentication Scheme with Django REST Framework

## Configuration

In 'settings.py' of your project add the following code:
```python
    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}
```