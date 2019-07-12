import logging
import sys
from logging.config import dictConfig

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class LoggerSimple:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', 'default')
        dictConfig({
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'console': {
                    'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
                },
                'file': {
                    'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'console',
                },

            },
            'loggers': {
                # root logger
                '': {
                    'level': 'INFO',
                    'handlers': ['console'],
                },
            },
        })

        self.logger = logging.getLogger(self.name)
