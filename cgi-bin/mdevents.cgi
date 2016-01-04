#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mdevents
import cgi
import glob

camera = 1 # selected camera id
limit = 0 # max display events (0 = unlimited) 
path1 = "/var/lib/motion/x-archive1-*.jpg"
path2 = "/var/lib/motion/x-archive2-*.jpg"

# Parse CGI arguments
args = cgi.parse()
try:
    arg_camera = args["camera"][0]
    if arg_camera == "1":
        camera = 1
    elif arg_camera == "2":
        camera = 2
    else:
        camera = 1
except KeyError:
    camera = 1
try:
    arg_limit = args["limit"][0]
    limit = int(arg_limit)
except KeyError:
    limit = 0

# Select a camera
path = path1
if camera == 2:
    path = path2

# Print the html
print mdevents.get_header(camera)
mdevents.print_event_list(glob.glob(path), limit)
print mdevents.get_footer(camera)

