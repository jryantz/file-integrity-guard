import logging

from guardian.settings import DEBUG

class CoreLogger(object):
    """
    App logger for registering issues at runtime.
    
    Settings `DEBUG = True` enables logging at the debug level.
    """

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(CoreLogger, self).__new__(self)
        return self.instance

    def __init__(self):
        # Create logger.
        self.logger = logging.getLogger('guardian')
        if DEBUG: self.logger.setLevel(logging.DEBUG)
        else: self.logger.setLevel(logging.WARNING)

        # Create console handler and set level to debug.
        ch = logging.StreamHandler()
        if DEBUG: ch.setLevel(logging.DEBUG)
        else: ch.setLevel(logging.WARNING)

        # Create formatter.
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to ch.
        ch.setFormatter(formatter)

        # Add ch to logger.
        self.logger.addHandler(ch)

        # Test logs.
        # self.logger.debug('debug message')
        # self.logger.info('info message')
        # self.logger.warning('warn message')
        # self.logger.error('error message')
        # self.logger.critical('critical message')