#!/usr/bin/env python3

"""
You are free to encode any url of your choice.
e.g. Instagram, Twitter, LinkedIn or any other ids, Youtube url, etc.
"""

import qrcode
import sys

def print_usage():
    print("usage: %s data [output filename]" % sys.argv[0])
    print(" if no output filename is set \"qrcode.png\" is used")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

data = sys.argv[1]
output = "qrcode.png"

if len(sys.argv) > 2:
    output = sys.argv[2]

img = qrcode.make(data)

img.save(output)

print("image saved as %s" % output)
