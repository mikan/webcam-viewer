#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime

def get_log_name(file_path):
    time = file_path.split("/")[-1].split(".")[0].split("-")[2:4]
    return time[0] + "-" + time[1]

def current_date_time():
    return datetime.datetime.today().strftime("%Y.%m.%d %H:%M")

def format_date_time(t):
    return t[0:4] + "." + t[4:6] + "." + t[6:8] + " " + t[9:11] + ":" + t[11:13]

def createEventId(t):
    return t[0:4] + t[4:6] + t[6:8] + t[9:11] + t[11:13]

def formatTime(t):
    return t[9:11] + "時" + t[11:13] + "分" + t[13:15] + "秒"

def web_path(file_path):
    return "/webcam/webcam/" + file_path.split("/")[-1]

def create_file_link(file_path, event):
    return "<a href=\"" + file_path + "\" data-lightbox=\"" + createEventId(event) + "\" title=\"" + formatTime(get_log_name(file_path)) + "\" class=\"button\">" + formatTime(get_log_name(file_path)) + "</a>"

# event listing function
# @param file_list file list
# @param limit event printing limit
def print_event_list(file_list, limit):
    path_list = []
    for path in file_list:
        path_list.append(web_path(path))
    path_list.sort()	# sort by date-time
    path_list.reverse()
    eventDict = {}
    eventList = []
    currentEvent = "19700000-0000"

    # build event list
    for path in path_list:
        time = get_log_name(path)	# yyyymmdd-HHMMSS
        event = time[0:13]		# yyyymmdd-HHMM
        if currentEvent != event:
            eventDict[event] = 1
            eventList.append(event)
            currentEvent = event
        else:
            eventDict[event] = eventDict[event] + 1

    # count result
    length = len(eventList)
    if limit <= 0:
        limit = length	# 0 以下なら全件表示
        print "<div class=\"control center\">" + str(length) + " events found. <a onclick=\"location.reload()\" class=\"button\">Refresh</a></div>"

    # print table
    index = 0	# fileList index
    event_count = 0	# printed event count
    for event in eventList:
        if event_count >= limit:
            break
        else:
            event_count = event_count + 1
            print "<h2>" + format_date_time(event) + "</h2>"
            print "<div class=\"view\"><img src=\"/webcam/img/loading.gif\" data-original="+ path_list[index]  +" alt=\"image\" class=\"lazy\" /></div>"
            print "<div class=\"control\">"
            print create_file_link(path_list[index], event)
            index = index + 1
            for var in range(1, eventDict[event]):
                print create_file_link(path_list[index], event)
                index = index + 1
            print "</div>"

html_header = '''Content-Type: text/html

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Camera %d: MOTION</title>
    <script type="text/javascript" src="/webcam/js/jquery-1.10.2.min.js"></script>
    <script type="text/javascript" src="/webcam/js/jquery.lazyload.min.js"></script>
    <script type="text/javascript" src="/webcam/js/lightbox-2.6.min.js"></script>
    <script type="text/javascript">$(function(){$("img.lazy").lazyload();});</script>
    <link rel="stylesheet" type="text/css" href="/webcam/css/screen.css" media="screen" />
    <link rel="stylesheet" type="text/css" href="/webcam/css/lightbox.css" media="screen" />
</head>
<body>
<div id="wrapper">
<div id="navigation">
    <ul>
        <li><a href="/webcam/live%d.html" class="live">LIVE</a></li>
        <li><a href="/webcam/timelapse%d.html" class="timelapse">TIMELAPSE</a></li>
        <li><a href="mdevents.cgi?camera=%d" class="camera-switch">Camera %d</a></li>
    </ul>
</div>
<h1>Camera %d <span class="motion">MOTION</span></h1>
'''

html_footer = '''<div id="footer">
    <p>&copy; 2005-2017 <a href="https://github.com/mikan">mikan</a></p>
</div>
</div>
</body>
</html>
'''

def reverse(num):
    if num == 1:
        return 2
    if num == 2:
        return 1

def get_header(num):
    return html_header % (num, num, num, reverse(num), reverse(num), num)

def get_footer(num):
    return html_footer


