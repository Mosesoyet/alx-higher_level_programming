#!/usr/bin/python3
def safe_print_ineger(value):
    try:
        print('{:d}'.format(value))
        return True
    except:
        return False
