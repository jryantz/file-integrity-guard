from .logger import AppLogger

class AppConfig(object):
    """
    Default object for defining a singleton based app configuration.
    """

    logger = AppLogger().logger