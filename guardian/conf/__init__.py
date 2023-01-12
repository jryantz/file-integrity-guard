from guardian.settings import BASE_DIR, DEBUG, GUARDED_DIRS, GUARDED_FILES, GUARDIAN_CACHE_FILENAME

class Settings:
    """
    Class representing the File Integrity Guard application and its
    default configuration.
    """

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Settings, self).__new__(self)
            self.initialized = False
        return self.instance

    def __init__(self):
        # Check if the the settings manager already exists.
        if self.initialized: return

        self.debug = True
        if isinstance(DEBUG, bool):
            self.debug = DEBUG

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

        self.initialized = True

settings = Settings()
