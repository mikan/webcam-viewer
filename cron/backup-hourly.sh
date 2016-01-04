#!/bin/sh

IMGPATH="/var/lib/motion/"
OWNPATH="$(cd "$(dirname "${BASH_SOURCE:-$0}")"; pwd)"
CMDNAME=`basename $0`
if [ $# -ne 1 ]; then
    echo "Usage: $CMDNAME hh (eg. 08)"
    exit 1
fi

input1="webcam1.jpg"
output1="webcam1-$1h.jpg"
thumb1="webcam1-$1h-s.jpg"

cp -p $IMGPATH$input1 $IMGPATH$output1
$OWNPATH/thumb.py $IMGPATH$output1 $IMGPATH$thumb1

