#!/usr/bin/env python
#
# usage: ./op_tapahtumat_to_json.py < tapahtumat20150101-20150131.csv
# 

copyright = """
Convert OP (Osuuspankki) tilitapahtumat lines to json.

Copyright (C) 2016 Pasi Lammi

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

import sys
import json
import string
import re
import locale


def get_value(name,d):
  replaced = re.sub('[\"]', '', d)
  if name.find('EUROA')>0:
    try:
      return locale.atof(replaced)
    except:
      pass
  return replaced.strip()
  
def get_name(name):
  name = re.sub('[\"]', '', name)
  return name

locale.setlocale(locale.LC_ALL, 'fi_FI')

headers = []
counter=0
ret = []
for line in sys.stdin:
  ret_line = {}
  counter+=1
  l = line.decode('latin-1').strip()
  if counter == 1:
    _headers = string.split(l,';')
    for h in _headers:
      headers.append(get_name(h))
    continue
  d = string.split(l,';')
  if len(d) < 10:
    continue
  for n in range(len(headers)-1):
    name = headers[n]
    ret_line[name]=get_value(name,d[n])
  ret.append(ret_line)

print json.dumps(ret,indent=1)
