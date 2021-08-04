#!/usr/bin/python

import os

print("Content-type: text/html\r")
print ("<font size=+1>Environment</font><\br>")
i = 0
for param in os.environ.keys():
    i = i+1
    print (i, " %20s : %s " % (param, os.environ[param]))