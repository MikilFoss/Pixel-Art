'''
This file uses the built in resize function of the Pillow library to "pixelify" an image.
The final output does maintain the original size of the image but it has appears like an n x m pixel image.
Where n and m are the desiredWidth and desiredHeight respectively.
'''

from PIL import Image
import math

desiredWidth = 16 # Desired number of pixels in the width of the image
desiredHeight = 16 # Desired number of pixels in the height of the image

filename = "AppleImageOriginal.jpeg" # Image file path
im = Image.open(filename) 
loadedImage = im.load() 
width, height = im.size 
imSmall = im.resize((desiredWidth, desiredHeight), Image.Resampling.LANCZOS) # pixelify the image

#rescale the image to original size
for i in range(width):
    for j in range(height):
        x = math.floor(i * desiredWidth / width)
        y = math.floor(j * desiredHeight / height)
        loadedImage[i, j] = imSmall.getpixel((x, y))

im.save("AppleImageBuiltIn.jpeg")