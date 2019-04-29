# Please copy this as a settings_local.py on the same directory and ensure to not add to version control, i.e. git ignore this file. Adjust the variables to meet your own settings
#To automate Local and Production server settings
import socket
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}



