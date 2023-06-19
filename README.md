
# Django Boilerplate
This boilier plate includes all of the basic features that you need to start a new project. It includes the following features:
- User Registration
- User Login
- User Logout
- Swagger Documentation
- Zappa Deployment settings (AWS Lambda)


## Libraries Used
- Django 3.1.7
- Python 3.10.07
- Django Rest Framework

## Generate Django Secret
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Installation
```bash
# Clone the repo
git clone https://github.com/lukuku-dev/django-rest-boilerplate.git
# Change directory
cd django-rest-boilerplate
# See available pyton versions
pyenv install --list
# Install the python version
pyenv install 3.10.07
# Create a virtual environment
pyenv virtualenv 3.10.07 <env-name>
# Activate the virtual environment
pyenv activate <env-name>
# Please use pyenv here, if you want to attach this code with aws-lambda
# Install the requirements
pip install -r requirements.txt
# rename .env.example to .env
# Fill the variables
# Run the migrations
python manage.py migrate
# Create a superuser
python manage.py createsuperuser
# Run the server
python manage.py runserver
```
# Customization
1. search `FIXME` and fill the variables

## Deployment
1. Create a new AWS account
2. Create a new IAM user
3. Create a new S3 bucket
4. Create a new Lambda function
5. Create a new API Gateway
6. Set aws credentials in your local machine
7. Set the variables in `zappa_settings.json`
8. Run `zappa deploy dev`