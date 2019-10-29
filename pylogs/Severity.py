from enum import Enum

class Severity(Enum):
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    SUCCESS = 0
    NOTSET = -1
