#!/user/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a, b = args
        res = fct(a, b)
        return res
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
