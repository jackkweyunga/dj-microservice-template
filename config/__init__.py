from .celery import app as celery_app


__version__ = '1.0.0'
__build__ = "dd1bdcf"

VERSION = __version__
BUILD = __build__

__all__ = (
    'celery_app',
    '__version__',
    '__build__',
    'VERSION',
    'BUILD',
    
)