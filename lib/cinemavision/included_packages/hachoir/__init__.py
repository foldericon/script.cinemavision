from __future__ import absolute_import
import os
import sys
import inspect

# Include this hachoir folder in sys.path so included libs will import properly
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from . import hachoir_core
from . import hachoir_parser
from . import hachoir_metadata
