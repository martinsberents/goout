# -*- encoding: utf-8 -*-
from font_colors import FontColors

# The id and secret of Facebook's app.
# Advise: set these in the settings_local.py file
CLIENT_ID = ''
CLIENT_SECRET = ''

DEBUG = False
BABEL_DEFAULT_LOCALE = 'en'

# A list containing dictionaries with Facebook profile's id and name [{'id': '', 'name': u''}, ...]
PROFILES = []

# A list of email addresses that should receive notifications regarding the application
ADMINS = []

# E-mail setup options
# SMTP_HOST = 'smtp.gmail.com'
# SMTP_PORT = 587
# EMAIL_ADDRESS = ''
# EMAIL_PASSWORD = ''

FACEBOOK_API_ERROR_REPORT_ENABLED = False
# Store sensitive or information specific to your purpose in the settings_local.py
# that is not tracked by Git.
try:
    from settings_local import *
except ImportError:
    print FontColors.WARNING + "WARNING: settings_local.py not found" + FontColors.ENDC
    pass
