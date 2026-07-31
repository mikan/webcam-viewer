#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mdevents
import cgi
import glob

camera = 1  # selected camera id
limit = 0  # max display events (0 = unlimited)
path1 = "/var/lib/motion/x-archive-????????-??????.jpg"
path2 = "/var/lib/motion2/x-archive-????????-??????.jpg"
mpath1 = "/var/lib/motion/y-archive-????????-??????.mp4"
mpath2 = "/var/lib/motion2/y-archive-????????-??????.mp4"

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
video_list = []
pic_list = []
if camera == 1:
    video_list = glob.glob(mpath1)
    pic_list = glob.glob(path1)
if camera == 2:
    video_list = glob.glob(mpath2)
    pic_list = glob.glob(path2)

# Print the html
print(mdevents.get_header(camera))
if len(video_list) > 0:
    mdevents.print_video_list(video_list, limit)
if len(pic_list) > 0:
    mdevents.print_event_list(pic_list, limit)
if len(video_list) == 0 and len(pic_list) == 0:
    mdevents.no_events()
print(mdevents.get_footer(camera))
