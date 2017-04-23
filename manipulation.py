# Manipulation.py
# manipulation module, import manipulation
def isInteger(intprocess):
    # process integer
    try:
        int(intprocess)
        return True
    except Exception:
        return False

def isString(strprocess):
    # process string
    try:
        int(strprocess)
        return False
    except Exception:
        return True
