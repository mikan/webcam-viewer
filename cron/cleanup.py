#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import datetime
import os
import os.path

IMGDIR = '/var/lib/motion/'
IMGDIR2 = '/var/lib/motion2/'
LIMIT_DAYS = 30


def get_date_time(filePath):
    time = filePath.split("/")[-1].split(".")[0].split("-")[2:4]
    s = time[0] + time[1]
    return datetime.datetime(int(s[0:4]), int(s[4:6]), int(s[6:8]), int(s[8:10]), int(s[10:12]), int(s[12:14]))


def clean_old_log(file_list):
    file_list.sort()  # sort
    file_list.reverse()  # reverse
    delete_count = 0
    today = datetime.datetime.today()
    for file_path in file_list:
        event_date_time = get_date_time(file_path)
        delta = today - event_date_time
        if delta.days >= LIMIT_DAYS:
            print "delete event: " + str(event_date_time)
            os.remove(file_path)
            delete_count = delete_count + 1
    if delete_count == 0:
        print "cleanup: no deletions."
    elif delete_count == 1:
        print "cleanup: 1 file deleted."
    else:
        print "cleanup: " + str(delete_count) + " files deleted."


if os.path.exists(IMGDIR):
    clean_old_log(glob.glob(IMGDIR + 'x-archive-*.jpg'))
if os.path.exists(IMGDIR2):
    clean_old_log(glob.glob(IMGDIR2 + 'x-archive-*.jpg'))
