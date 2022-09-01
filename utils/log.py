# -*- coding: utf-8 -*-
import logging
from logging import config  # pylint: disable=W0611

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "%(asctime)s %(levelname)-10s: %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'extended': {
            'format': "%(asctime)s %(filename)s:%(lineno)-5s %(levelname)-10s: %(message)s",
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'default': {
            'level': 'WARNING',
            'formatter': 'extended',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file_handler': {
            'level': 'DEBUG',
            'formatter': 'extended',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'matos-gcp-provider.log',  # Default is stderr
            "mode": "a",
            "encoding": "utf-8"
        }
    },
    'loggers': {
        'matos_aws_provider': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'matos_gcp_provider': {
            'handlers': ['default',],
            'level': 'DEBUG',
            'propagate': False
        },
        'matos_azure_provider': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["default"]
    }
}


def config_logger():
    """config logger

    Returns:
        None
    """
    logging.config.dictConfig(LOGGING_CONFIG)
    # logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger("azure").setLevel(logging.WARNING)
