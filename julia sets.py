from PIL import Image

if __name__ == "__main__":
    
    # setting width, height and zoom of picture
    w, h, zoom = 1920, 1080, 1

    # creating new image with rgb mode 
    bitmap = Image.new("RGB", (w, h), "white")

    pix = bitmap.load()

    #setting the variabels accrorind to the equation
    cX, cY = -0.7, 0.27015
    moveX, moveY = 0.0, 0.0
    MaxIter = 255

    for x in range(w):
        for y in range(h):
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
            i = MaxIter
            while zx*zx + zy*zy < 4 and i > 1:
                tmp = zx*zx - zy*zy + cX
                zy,zx = 2.0*zx*zy + cY, tmp 
                i -= 1

            pix[x,y] = (i << 21) + (i << 10) + i*8

    bitmap.show()