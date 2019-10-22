"""
PyLogs is a simple library to make easier for everyone to add logs into their Python programs
PyLogs currently is in an alpha version and under development

@name PyLogs
@author Krypton
@copyright Copyright ©2019 Krypton
@credits
@licence Apache 2.0
@version 0.0.1
@maintainer Krypton
@status Development (Alpha Build)
"""

import Formatting

__name__ = "PyLogs"
__author__ = "Krypton"
__copyright__ = "Copyright ©2019 Krypton"
__credits__ = []
__license__ = "Apache 2.0"
__version__ = "1.0.0"
__maintainer__ = "Krypton"
__status__ = "Development (Alpha Build)"

class Log():

    def critical(message : str, color : bool):
        if color:
            return print(Formatting.ERROR_BOLD + "[CRITICAL] " + Formatting.STOP + message)
        else:
            return print("[CRITICAL] " + message)

    def error(message : str, color : bool):
        if color:
            return print(Formatting.ERROR_THIN + "[ERROR] " + Formatting.STOP + message)
        else:
            return print("[ERROR] " + message)

    def warning(message : str, color : bool):
        if color:
            return print(Formatting.WARNING_THIN + "[WARNING] " + Formatting.STOP + message)
        else:
            return print("[WARNING] " + message)

    def info(message : str, color : bool):
        if color:
            return print(Formatting.INFO_THIN + "[INFO] " + Formatting.STOP + message)
        else:
            return print("[INFO] " + message)

    def debug(message : str, color : bool):
        if color:
            return print(Formatting.DEBUG_THIN + "[DEBUG] " + Formatting.STOP + message)
        else:
            return print("[DEBUG] " + message)

    def success(message : str, color : bool):
        if color:
            return print(Formatting.SUCCESS_THIN + "[SUCCESS] " + Formatting.STOP + message)
        else:
            return print("[SUCCESS] " + message)