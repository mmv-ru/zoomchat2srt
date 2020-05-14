#!/usr/bin/env python3

import datetime
import re
import textwrap

chartime = 80
linetime = 100
long_pause = 1000
preshow_after_long_pause = 200
maxlen = 60

delay_on_overflow = True

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")
wrapper = textwrap.TextWrapper(width=maxlen) 

file_name = "/mnt/media3/20200513 Защита прав по лекарственному обеспечению/GMT20200513-140640_----------.txt"
with open(file_name, 'r') as f:
    lines = f.readlines()

    last_endtime_obj = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
    src_line_num = 1
    sub_line_num = src_line_num
    for line in lines:
      timestamp, text = line.split(None, 1)
      text = _RE_COMBINE_WHITESPACE.sub(" ", text).strip()
      starttime_obj = datetime.datetime.strptime(timestamp, '%H:%M:%S')
      extend = datetime.timedelta(milliseconds=0)
      if starttime_obj - last_endtime_obj > datetime.timedelta(milliseconds=long_pause) :
        starttime_obj -= datetime.timedelta(milliseconds=preshow_after_long_pause)
        extend = datetime.timedelta(milliseconds=preshow_after_long_pause)
      if delay_on_overflow :
        if starttime_obj < last_endtime_obj :
          starttime_obj = last_endtime_obj
      else: 
        assert starttime_obj >= last_endtime_obj , "starttime: {} lastendtime: {}".format(starttime_obj.strftime('%H:%M:%S.%f'), last_endtime_obj.strftime('%H:%M:%S.%f'))
      text_letters = len(text)
      wrapped = wrapper.wrap(text)
      for text in wrapped :
        text_letters = len(_RE_COMBINE_WHITESPACE.sub("", text).strip())
        endtime_obj = starttime_obj + datetime.timedelta(milliseconds=text_letters*chartime + linetime ) + extend
        print(sub_line_num)
        print(starttime_obj.strftime('%H:%M:%S.%f')[:-3] + ' --> ' + endtime_obj.strftime('%H:%M:%S.%f')[:-3])
        print(text)
        print()
        last_endtime_obj = endtime_obj
        sub_line_num += 1
        starttime_obj = endtime_obj
        extend = datetime.timedelta(milliseconds=0)
        src_line_num += 1
