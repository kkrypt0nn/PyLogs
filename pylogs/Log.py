from .Formatting import Formatting

__all__ = [
    'critical',
    'error',
    'warning',
    'info',
    'debug',
    'success'
]

def critical(message: str, color: bool):
    """
    Log into the console a critical message
    :param: message String - The message that should be shown in the log
    :param: color Boolean - Should the output be with color or not
    :return: print String - Returns the built string and print it
    """

    if color:
        return print(Formatting.ERROR_BOLD + "[CRITICAL] " + Formatting.STOP + message)
    else:
        return print("[CRITICAL] " + message)

def error(message: str, color: bool):
    """
    Log into the console a normal error message
    :param: message String - The message that should be shown in the log
    :param: color Boolean - Should the output be with color or not
    :return: Print the built string
    """

    if color:
        return print(Formatting.ERROR_THIN + "[ERROR] " + Formatting.STOP + message)
    else:
        return print("[ERROR] " + message)

def warning(message: str, color: bool):
    """
    Log into the console a warning message
    :param: message String - The message that should be shown in the log
    :param: color Boolean - Should the output be with color or not
    :return: Print the built string
    """

    if color:
        return print(Formatting.WARNING_THIN + "[WARNING] " + Formatting.STOP + message)
    else:
        return print("[WARNING] " + message)

def info(message: str, color: bool):
    """
    Log into the console an info message
    :param: message String - The message that should be shown in the log
    :param: color Boolean - Should the output be with color or not
    :return: Print the built string
    """

    if color:
        return print(Formatting.INFO_THIN + "[INFO] " + Formatting.STOP + message)
    else:
        return print("[INFO] " + message)

def debug(message: str, color: bool):
    """
    Log into the console a debug message
    :param: message String - The message that should be shown in the log
    :param: color Boolean - Should the output be with color or not
    :return: Print the built string
    """

    if color:
        return print(Formatting.DEBUG_THIN + "[DEBUG] " + Formatting.STOP + message)
    else:
        return print("[DEBUG] " + message)

def success(message: str, color: bool):
    """
    Log into the console a success message
    :param: message String - The message that should be shown in the log
    :param: color Boolean - Should the output be with color or not
    :return: Print the built string
    """

    if color:
        return print(Formatting.SUCCESS_THIN + "[SUCCESS] " + Formatting.STOP + message)
    else:
        return print("[SUCCESS] " + message)
