import noise
import numpy as np
import math
from scipy.misc import toimage

#scale width and height
shape = (1024,1024)
# at what distance to view the noisemap
scale = 100.0
# number of detail the perlin noise should have
octaves = 6
# how much each octave contributes to the overall shape
# octave 1 could be mountains and octave could be boulders
persistence = 0.5
# how much detail is added or removed at each octave
# value more than 1 will increase deatil at each octave
# value of 1 octave will have same detail at each octave
# value less than 1 will have each octave get smoother
lacunarity = 2.0

# shape will be changed to zeros
world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        # we get an image with white and dark spots
        #dark spots are more closer to -1 and whiter closer to 1
        # the value differs from 1 to -1
        world[i][j] = noise.pnoise2(i/scale, j/scale, octaves, persistence, lacunarity, 1024, 1024, 0)

lightblue = [0,191,255]
blue = [65,105,225]
green = [34,139,34]
darkgreen = [0,100,0]
sandy = [210,180,140]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]

threshold = 0

def add_color2(world):
    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < threshold + 0.05:
                color_world[i][j] = blue
            elif world[i][j] < threshold + 0.055:
                color_world[i][j] = sandy
            elif world[i][j] < threshold + 0.1:
                color_world[i][j] = beach
            elif world[i][j] < threshold + 0.25:
                color_world[i][j] = green
            elif world[i][j] < threshold + 0.6:
                color_world[i][j] = darkgreen
            elif world[i][j] < threshold + 0.7:
                color_world[i][j] = mountain
            elif world[i][j] < threshold + 1.0:
                color_world[i][j] = snow

    return color_world

island_world_grad = add_color2(world)
toimage(island_world_grad).show()


