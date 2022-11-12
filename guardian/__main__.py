"""
Invokes the Guardian application when executed from the command line.

python -m guardian
"""

from guardian.core import management

if __name__ == '__main__':
    management.execute()
