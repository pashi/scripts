#!/usr/bin/python 

import sys
import os
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

copy_text='(C) pashi@iki.fi'

for f in sys.argv[1:]:

	filename= '%s/%s' % (os.getcwd(),f)
	basewidth = 800
	img = Image.open(filename)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-M.ttf", 30)
	draw.text((img.size[0]-252, img.size[1]-37), copy_text,(0,0,0),font=font)
	draw.text((img.size[0]-248, img.size[1]-33), copy_text,(0,0,0),font=font)
	draw.text((img.size[0]-250, img.size[1]-35), copy_text,(255,255,255),font=font)
	img.save('/tmp/pashi_%s' % f)

