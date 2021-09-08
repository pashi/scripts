#!/usr/bin/env python
import argparse
import os
import av

args=None

def read_params():
        global args
        parser = argparse.ArgumentParser()
        parser.add_argument('--debug', action='store_true', help='debug')
        parser.add_argument('--sf', help='start frame', type=int, default=0)
        parser.add_argument('--ef', help='end frame', type=int, default=0)
        parser.add_argument('--fs', help='frame steps', type=int, default=25)
        parser.add_argument('--fileprefix', help='output fileprefix', default='f_')
        parser.add_argument('video', help='video filename')
        parser.add_argument('outputdir', help='output directory', default='/tmp')
        args = parser.parse_args()
        if args.debug:
                print (args)


def convert():
	global args
	container = av.open(args.video)
	video = next(s for s in container.streams if s.type == b'video')

	pc = 0
	is_last = False
	for packet in container.demux(video):
		if is_last:
			break
		for frame in packet.decode():
			export_frame = True

			# is this frame smaller than start frame (if defined)
			if args.sf > 0 and frame.index < args.sf:
				export_frame = False

			# is this frame bigger than end frame (if defined)
			if args.ef > 0 and frame.index > args.ef:
				export_frame = False
				is_last = True
				break

			# check is this frame amount of steps
			if args.fs > 0 and not pc%args.fs == 0:
				export_frame = False

			filename = '%s/%s%06d.jpg' % (args.outputdir, args.fileprefix,frame.index)
#			print "export %s file=%s, index=%s, pc=%s %s" % (export_frame,filename,frame.index,pc, (pc%args.fs))
			pc+=1
			if not export_frame:
				continue
			print ("export file=%s, frame index=%s" % (filename,frame.index))
			frame.to_image().save(filename)


if __name__ == "__main__":
	read_params()
	convert()
