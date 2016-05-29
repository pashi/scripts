#!/usr/bin/env python

copyright = """
Convert json for gnucash

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


import glob
import json
import string
import datetime
import re

def gnucash_line(data):
  ret = [u'' for x in range(4) ]
  
  for k,v in data.iteritems():
    if k == u"Arvop\u00e4iv\u00e4":
      ret[0] = u'%s' % v
    elif k == u"M\u00e4\u00e4r\u00e4\u00a0 EUROA":
      if v > 0:
        ret[1] = u'%s' % v
        ret[2] = u'%s' % 0
      else:
        ret[1] = u'%s' % 0
        ret[2] = u'%s' % (v * -1)
  txt = []
  for x in [u'Saaja/Maksaja', u'Viite',u'Selitys',u'Viesti',u'Saajan tilinumero ja pankin BIC']:
    if not data[x].strip() == '':
      n = string.replace(x,' ', '_')
      d = data[x]
      txt.append("%s=%s " % (n,d))
  ret[3] = u''.join(txt).strip()
  print string.join(ret,u';').encode('utf-8')

files = glob.glob('*.json')
for f in files:
  with open(f) as f:
    d = json.loads(f.read())
    for line in d:
      gnucash_line(line)
