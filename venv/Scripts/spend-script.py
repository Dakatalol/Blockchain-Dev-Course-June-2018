#!C:\Users\Jordan\PycharmProjects\blockchain\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pycoin==0.80','console_scripts','spend'
__requires__ = 'pycoin==0.80'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pycoin==0.80', 'console_scripts', 'spend')()
    )
