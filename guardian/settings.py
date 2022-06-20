"""
Settings for the File Integrity Guard package.
"""

from pathlib import Path

# Use this to build relative paths to this project.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# The secret key is used as a seed in the file hash.
SECRET_KEY = ''

# Use debug mode to enable in-depth logging.
DEBUG = True

# Runtime Config

GUARDED_DIRS = [

]

# Reporting Config

ADMINS = [

]

DEFAULT_FROM_EMAIL = ''

