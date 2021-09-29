import sys

with open('sys_info.txt', 'w') as out:
    for k, v in sys.__dict__.items():
        if not callable(v):
            print("%20s: %s" % (k, repr(v)), file=out)
