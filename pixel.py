from PIL import Image
import numpy as np


# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')


def convert_grayscale(imagePath):
    img = open_image(imagePath)

    # getting pixel data
    pixels = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):

            # get current from pixel from given pixel and width
            red, green, blue = img.getpixel((i, j))

            # calculating grayscale with  601-7 formule
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

            # setting the grayscale at the given width and height
            pixels[i, j] = (int(gray), int(gray), int(gray))


    return img

'''
def bilinear_interpolate(img, x, y):
    pixels = img.load()

    x = np.asarray(x)
    y = np.asarray(y)

    x0 = int(np.floor(x))
    x1 = x0 + 1
    y0 = int(np.floor(y))
    y1 = y0 + 1

    x0 = int(np.clip(x0, 0, img.size[0]-1))
    x1 = int(np.clip(x1, 0, img.size[0]-1))
    y0 = int(np.clip(y0, 0, img.size[1]-1))
    y1 = int(np.clip(y1, 0, img.size[1]-1))

    Ia = pixels[ y0, x0 ]
    Ib = pixels[ y1, x0 ]
    Ic = pixels[ y0, x1 ]
    Id = pixels[ y1, x1 ]

    wa = (x1-x) * (y1-y)
    wb = (x1-x) * (y-y0)
    wc = (x-x0) * (y1-y)
    wd = (x-x0) * (y-y0)

    return wa*Ia + wb*Ib + wc*Ic + wd*Id

def downscale(path):
    img = open_image(path)
    width, height = img.size

    pixels = img.load()
    for i in range(width-1):
        for j in range(height-1):
            pixels[i, j] = bilinear_interpolate(img, i, j)

    imgSmall = img.resize((250, 250))
    result = imgSmall.resize(img.size, Image.NEAREST)
    save_image(result, "/Users/elev/Desktop/d.png")


downscale("hero.jpg")

'''

def pixelate(path, width, height):
    img = open_image(path)

    # Resize smoothly down to 16x16 pixels
    imgSmall = img.resize((width, height), Image.BILINEAR)

    #Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size,Image.NEAREST)

    save_image(result, "/Users/elev/Desktop/d.png")

pixelate("hero.jpg", 50, 50)

#grayscaleImg = convert_grayscale("hero.jpg")
#save_image(grayscaleImg, "/Users/elev/Desktop/grayscale.png")






