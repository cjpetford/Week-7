As of 26/03/2024
I've had to restart a few times to clear a lot of errors that i couldn't find solutions to such as a recursion error which for some reason something was looping and exceeded the depth limit. This project is a current work in progress, and it aims to display my experience and a little of my past knowledge concerning html, web design, django frameworks and source control. I will continue to update my repository through source control which i learnt during my last project. I'll also add a few links from resources I gathered researching and understanding how django works and why it's used.

As of 2/04/2024
Dependencies concerning this project are as follows:
Python 3.12.2 or later installed
Django 4.2.5 
django-crispy-forms 2.1
crispy-bootstrap4
pillow 10.2.0
install these using the python package installer command pip install ___. Ensure the directory you work in has appropriate naming conventions, one issue i noticed was showing paths when I had an apostrophe in one of the folders in my directory. Ensure you add both apps to INSTALLED_APPS section with correct syntax and that your STATIC, LOGIN, and MEDIA sections are correct. Ensure that whenever you make any changes to your models.py that they are migrated before you make any further changes elsewhere. Do this by the command python manage.py makemigrations, and once that finishes running, python manage.py migrate. Under my third party INSTALLED APPS list, i added CRISPY_TEMPLATE_PACK = 'bootstrap4' as the bootstrap i had been using was not compatible with the crispy forms i had installed. The versions required are all listed in the depenndencies above, and later versions should work fine.
