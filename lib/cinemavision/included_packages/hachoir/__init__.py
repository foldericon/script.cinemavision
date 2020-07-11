import os
import sys
import inspect

# Include this hachoir folder in sys.path so included libs will import properly
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import core
import parser
import metadata

VERSION = (3, 1, 1)
__version__ = ".".join(map(str, VERSION))
