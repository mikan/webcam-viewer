#!/bin/sh

IMGPATH="/var/lib/motion/"
IMGPATH2="/var/lib/motion2/"
OWNPATH="$(cd "$(dirname "${BASH_SOURCE:-$0}")"; pwd)"
CMDNAME=`basename $0`
if [ $# -ne 1 ]; then
	echo "Usage: $CMDNAME hh (eg. 08)"
	exit 1
fi

input1="webcam.jpg"
output1="webcam-$1h.jpg"
thumb1="webcam-$1h-s.jpg"

if [ -d $IMGPATH ]; then
	cp -p $IMGPATH$input1 $IMGPATH$output1
	$OWNPATH/thumb.py $IMGPATH$output1 $IMGPATH$thumb1
fi
if [ -d $IMGPATH2 ]; then
	cp -p $IMGPATH2$input1 $IMGPATH2$output1
	$OWNPATH/thumb.py $IMGPATH2$output1 $IMGPATH2$thumb1
fi

