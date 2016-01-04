#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import datetime
import os

IMGDIR = '/var/lib/motion/'
LIMIT_DAYS = 14

def getDateTime(filePath):
	eventDateTime = filePath.split("/")[-1].split(".")[0].split("-")[2:4]
	s = eventDateTime[0] + eventDateTime[1]
	dateTime = datetime.datetime(int(s[0:4]), int(s[4:6]), int(s[6:8]), int(s[8:10]), int(s[10:12]), int(s[12:14]))
	return dateTime

def cleanOldLog(fileList):
	fileList.sort()		# sort
	fileList.reverse()	# reverse
	deleteCount = 0
	today = datetime.datetime.today()
	for filePath in fileList:
		eventDateTime = getDateTime(filePath)
		delta = today - eventDateTime
		if delta.days >= LIMIT_DAYS:
			print "delete event: " + str(eventDateTime)
			os.remove(filePath)
			deleteCount = deleteCount + 1
	if deleteCount == 0:
		print "delete file is nothing"
	elif deleteCount == 1:
		print "1 file deleted"
	else:
		print str(deleteCount) + "files deleted."

cleanOldLog(glob.glob(IMGDIR + 'x-archive1-*.jpg'))

