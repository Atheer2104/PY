import sys, random, argparse
import numpy as np
import math
from PIL import Image

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
gscale2 = '@%#*+=-:. '

def getAverageGrayScale(image):
    # get image as numpy array
    im = np.array(image)

    #get shape
    w, h = im.shape

    # get average
    return np.average(im.reshape(w*h))

def convertImageIntoAscii(fileName, cols, scale, moreLevels):

    global gscale1, gscale2

    # open image and convert into grayscale
    image = Image.open(fileName).convert("L")

    # store dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H)) 

    #width of tile
    w = W/cols

    # tile height based on aspect ratio and scale
    h = w/scale

    #number of rows
    rows = int(H/h)

    print("cols: %d, rows: %d" % (cols, rows)) 
    print("tile dims: %d x %d" % (w, h)) 

    #check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!") 
        exit(0) 

    #ascii image is a list of character strings
    aimg = []

    # list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        #correcting last tile
        if j == rows-1:
            y2 = H

        aimg.append("")

        for i in range(cols):
            #crop image to tilex
            x1 = int(i*w)
            x2 = int((i+1)*w)

            # correct last tile
            if i == cols-1:
                x2 = W

            #croping image to get tile
            img = image.crop((x1, y1, x2, y2))

            avg = int(getAverageGrayScale(img))

            # look up ascii character
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

            aimg[j] += gsval

    return aimg

def main():
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr) 
    # add expected arguments 
    parser.add_argument('--file', dest='imgFile', required=True) 
    parser.add_argument('--scale', dest='scale', required=False) 
    parser.add_argument('--out', dest='outFile', required=False) 
    parser.add_argument('--cols', dest='cols', required=False) 
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true') 

    args = parser.parse_args()

    imgFile = args.imgFile

    #setting output file
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile

    #setting defualt scale to 0.43
    scale = 0.43
    if args.scale: 
        scale = float(args.scale)

    #setting defualt cols to 80
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('generating ASCII art...') 
    # convert image to ascii txt 
    aimg = convertImageIntoAscii(imgFile, cols, scale, args.moreLevels) 

    # open file 
    f = open(outFile, "w")

    # write to file
    for row in aimg:
        f.write(row + "\n")

    #cleanup
    f.close()
    print("ASCII art written to %s" % outFile) 


#call main
if __name__ == '__main__':
    main()

            

