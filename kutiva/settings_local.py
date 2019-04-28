# Please copy this as a settings_local.py on the same directory and ensure to not add to version control, i.e. git ignore this file. Adjust the variables to meet your own settings
#To automate Local and Production server settings
import socket

if socket.gethostname() == 'josemachava-ThinkPad-T440':	#ensure your local machine hostname is used
    DEBUG = True
    DATABASES['default'] = DATABASES['default']	#for tests, comment out upon upgrade
    
Has_Local_Settings = True


UG = True

