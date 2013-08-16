#!/usr/bin/python
#    Python scripts that converts any video stream into a set of JPEG files.
#    Copyright (C) 2013  Farious
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import cv2, getopt, sys, urllib, time

def main():
# input arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:io", ["help","input=","output="])
        if opts == []:
            usage()
            sys.exit('')
    except getopt.GetoptError:
        usage()
    
    inputF = ''
    outputF = 'output/'

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        if o in ("-i", "--input"):
            inputF = str(a)
        if o in ("-o", "--output"):
            outputD = str(a)

    if inputF == '':
        usage()
        sys.exit()

# strips video stream
    stripVideo(inputF, outputD)

def stripVideo(inputF, outputD):
# strips video stream
    try:
        cap = cv2.VideoCapture(inputF)
        if not cap.isOpened():
            print 'Couldn\'t open file, please confirm that it is a video file.'
            raise IOError
    except:
        sys.exit()

    name = inputF.split('.')[0].split('/')[-1]
    print 'Video file opened, starting strip of the video.'
    
    imOK, image = cap.read()
    img_counter = 0
    residual = 0
    while imOK:
        img_counter += 1
        cv2.imwrite(outputD + name + '_{0:05d}.jpg'.format(img_counter), image)
        
        q, r = divmod(img_counter, 100)
        if r == 0:
            print 'Processed {} images.'.format(img_counter)
        imOK, image = cap.read()

    print 'Done, {} image files were created.'.format(img_counter)

def usage():

    print ' -------------------------------------------------------------------------'
    print ' Fabio Reis (info - at - fabioreis.net),  2013'
    print ' '
    print ' Turns any video stream into a group of JPEG individual images. ' 
    print ' '
    print ' Typical usage:'
    print ' pyVID2JPEG.py --input=test.avi --output=output/'
    print ' '
    print ' -------------------------------------------------------------------------'
    sys.exit(' ')

#-------------------------------
if __name__ == "__main__":
    main()
