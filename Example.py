import pylogs

# Prints information about the library
print(pylogs.__name__ + ", Version " + pylogs.__version__)
print("Made by " + pylogs.__author__ + "\n\n")

# Prints critical error message with (1st) and without (2nd) color:
pylogs.critical("Critical Error Message", True)
pylogs.critical("Critical Error Message", False)

# Prints error message with (1st) and without (2nd) color:
pylogs.error("Error Message", True)
pylogs.error("Error Message", False)

# Prints warning message with (1st) and without (2nd) color:
pylogs.warning("Warning Message", True)
pylogs.warning("Warning Message", False)

# Prints info message with (1st) and without (2nd) color:
pylogs.info("Info Message", True)
pylogs.info("Info Message", False)

# Prints debug message with (1st) and without (2nd) color:
pylogs.debug("Debug Message", True)
pylogs.debug("Debug Message", False)

# Prints success message with (1st) and without (2nd) color:
pylogs.success("Success Message", True)
pylogs.success("Success Message", False)