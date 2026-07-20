import logging

# Simple logging configuration to be imported in settings.py
LOGGING_CONFIG_DICT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'shopsphere': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'products': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
