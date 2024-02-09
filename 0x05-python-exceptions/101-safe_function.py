#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        print("result of {}: {}".format(fct.__name__, result))
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None

