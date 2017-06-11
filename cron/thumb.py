#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PIL import Image


in_file = sys.argv[1]
out_file = sys.argv[2]
try:
    image = Image.open(in_file)
    new_size = image.size[0] / 4, image.size[1] / 4
    image.thumbnail(new_size)
    image.save(out_file, "JPEG")
except IOError:
    print "cannot create thumbnail for ", in_file
