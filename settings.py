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

# Store sensitive or information specific to your purpose in the settings_local.py
# that is not tracked by Git.
try:
    from settings_local import *
except ImportError:
    print FontColors.WARNING + "WARNING: settings_local.py not found" + FontColors.ENDC
    pass
