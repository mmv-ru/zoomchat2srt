#!/usr/bin/env python3

import datetime
import re

chartime = 100
linetime = 400
maxlen = 40

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

file_name = "/mnt/media3/20200513 Защита прав по лекарственному обеспечению/GMT20200513-140640_----------.txt"
with open(file_name, 'r') as f:
    lines = f.readlines()
    line_num = 1
    for line in lines:
      timestamp, text = line.split(None, 1)
      text = _RE_COMBINE_WHITESPACE.sub(" ", text).strip()
      text_letters = len(text)
      starttime_obj = datetime.datetime.strptime(timestamp, '%H:%M:%S')
      endtime_obj = starttime_obj + datetime.timedelta(milliseconds=text_letters*chartime + linetime )
      print(line_num)
      print(starttime_obj.strftime('%H:%M:%S.%f')[:-3] + ' --> ' + endtime_obj.strftime('%H:%M:%S.%f')[:-3])
      print(str(text_letters) + ' ' + text)


      line_num += 1
