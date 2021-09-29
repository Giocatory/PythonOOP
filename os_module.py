import os

with open('os_info.txt', 'w') as out:
    for k, v in os.__dict__.items():
        if not callable(v):
            print("%20s: %s" % (k, repr(v)), file=out)
