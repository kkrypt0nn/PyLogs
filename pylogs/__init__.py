from .Severity import *
from .Formatting import *
from .Log import *

name = "pylogs"
__name__ = "PyLogs"
__author__ = "Krypton"
__copyright__ = "Copyright ©2019 Krypton"
__credits__ = []
__license__ = "Apache 2.0"
__version__ = "2.0.2"
__maintainer__ = "Krypton"
__status__ = "Development (Alpha Build)"

__all__ = [

    'Severity',
    'Formatting',

    # Logging messages
    'critical',
    'error',
    'warning',
    'info',
    'debug',
    'success'

]
