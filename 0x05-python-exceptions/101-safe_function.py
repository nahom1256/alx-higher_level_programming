
#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        n = fct(*args)
        return n
    except Exception as erro:
        print("Exception: {}".format(erro), file=sys.stderr)
        return None
