import os

ENVIRONMENT = os.getenv('environment', 'development')

if ENVIRONMENT == 'development':
    SETTINGS_FILE = 'config.settings.development'
elif ENVIRONMENT == 'production':
    SETTINGS_FILE = 'config.settings.production'
