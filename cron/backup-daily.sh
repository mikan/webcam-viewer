#!/bin/sh

IMGPATH="/var/lib/motion/"
IMGPATH2="/var/lib/motion2/"
EXT=".jpg"
EXTS="-s.jpg"
FIRST=1
input1="webcam-08h"
output1="webcam-w"

for insert in 6 5 4 3 2 1
do
	tmp=`expr $insert + 1`
	cp -p $IMGPATH$output1$insert$EXT $IMGPATH$output1$tmp$EXT
	cp -p $IMGPATH2$output1$insert$EXT $IMGPATH2$output1$tmp$EXT
	cp -p $IMGPATH$output1$insert$EXTS $IMGPATH$output1$tmp$EXTS
	cp -p $IMGPATH2$output1$insert$EXTS $IMGPATH2$output1$tmp$EXTS
done
cp -p $IMGPATH$input1$EXT $IMGPATH$output1$FIRST$EXT
cp -p $IMGPATH2$input1$EXT $IMGPATH2$output1$FIRST$EXT
cp -p $IMGPATH$input1$EXTS $IMGPATH$output1$FIRST$EXTS
cp -p $IMGPATH2$input1$EXTS $IMGPATH2$output1$FIRST$EXTS

