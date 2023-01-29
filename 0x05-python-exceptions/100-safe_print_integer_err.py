#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as er:
        sys.stderr.write("Exception: {}\n".format(er))
        return False
    else:
        return True
