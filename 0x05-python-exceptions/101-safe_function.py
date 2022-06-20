#!/user/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a, b = args
        res = fct(a, b)
        return res
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
