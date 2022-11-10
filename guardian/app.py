from guardian.core.app import AppConfig

from guardian.settings import BASE_DIR, GUARDED_DIRS, GUARDED_FILES, GUARDIAN_CACHE_FILENAME

class GuardianConfig(AppConfig):
    """
    Class representing the File Integrity Guard application and its
    default configuration.
    """

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(GuardianConfig, self).__new__(self)
            self.logger.debug('Created %s.' % self)
        self.logger.debug('Returned %s.' % self)
        return self.instance

    def __init__(self):
        if not hasattr(self, 'name'):
            self.name = 'guardian'

        if not hasattr(self, 'verbose_name'):
            self.verbose_name = self.name.title()

        self.cache_filename = '.guardian'
        if isinstance(GUARDIAN_CACHE_FILENAME, str) \
           and len(GUARDIAN_CACHE_FILENAME) > 0 \
           and GUARDIAN_CACHE_FILENAME[0:1] == '.':
            self.cache_filename = GUARDIAN_CACHE_FILENAME

        self.project_dir = None
        if isinstance(BASE_DIR, str):
            self.project_dir = BASE_DIR

        self.guarded_dirs = []
        if isinstance(GUARDED_DIRS, list):
            self.guarded_dirs = GUARDED_DIRS

        self.guarded_files = []
        if isinstance(GUARDED_FILES, list):
            self.guarded_files = GUARDED_FILES

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)