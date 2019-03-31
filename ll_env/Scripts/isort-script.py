#!D:\learning_log_djingo\ll_env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'isort==4.3.9','console_scripts','isort'
__requires__ = 'isort==4.3.9'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('isort==4.3.9', 'console_scripts', 'isort')()
    )
