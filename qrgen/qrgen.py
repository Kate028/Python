#!/usr/bin/env python3

"""
You are free to encode any url of your choice.
e.g. Instagram, Twitter, LinkedIn or any other ids, Youtube url, etc.
"""

import qrcode
import sys

def print_usage():
    print("usage: %s url [output filename]" % sys.argv[0])
    print(" if no output filename is set \"QR_code.png\" is used")

# if no url is passed print usage text and exit
if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

url = sys.argv[1]
output = "QR_code.png"

# if 2nd parameter is set use this as filename instead of QR_code.png
if len(sys.argv) > 2:
    output = sys.argv[2]

# create image object
img = qrcode.make(url)

# save image to file
img.save(output)

print("image saved as %s" % output)
