#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
