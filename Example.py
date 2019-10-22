from PyLogs import Log
import PyLogs

print(PyLogs.__name__ + ", Version " + PyLogs.__version__)
print("Made by " + PyLogs.__author__ + "\n\n")

# Prints Critical Error Message With Color
Log.critical("Critical Error Message", True)
# Prints Critical Error Message Without Color
Log.critical("Critical Error Message", False)

# Prints Error Message With Color
Log.error("Error Message", True)
# Prints Critical Error Message Without Color
Log.error("Error Message", False)

# Prints Warning Message With Color
Log.warning("Warning Message", True)
# Prints Warning Message Without Color
Log.warning("Warning Message", False)

# Prints Info Message With Color
Log.info("Info Message", True)
# Prints Info Message Without Color
Log.info("Info Message", False)

# Prints Debug Message With Color
Log.debug("Debug Message", True)
# Prints Debug Message Without Color
Log.debug("Debug Message", False)

# Prints Success Message With Color
Log.success("Success Message", True)
# Prints Success Message Without Color
Log.success("Success Message", False)