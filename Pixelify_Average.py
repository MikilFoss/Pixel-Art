'''
This file averages the pixel values of the image to "pixelify" the image
The final output does maintain the original size of the image but it has appears like an n x m pixel image.
Where n and m are the desiredWidth and desiredHeight respectively.
'''
#import the necessary libraries
from PIL import Image
import math

desiredWidth = 16 # Desired width of the image in pixels
desiredHeight = 16 # Desired height of the image in pixels

#Open and Load the image
filename = "AppleImageOriginal.jpeg" # Image file path
im = Image.open(filename) 
loadedImage = im.load() 

#Get the width and height of the original image
width, height = im.size


widthRatio = width / desiredWidth
heightRatio = height / desiredHeight

#iterate through the image one desired pixel at a time averaging values then updating the pixel values of the original image
for i in range(desiredWidth):
    for j in range(desiredHeight):
        pixelsum = [0, 0, 0]

        #iterate through the pixels in the original image that correspond to the current desired pixel
        for k in range(math.ceil(widthRatio*i), math.ceil(widthRatio*(i+1))): 
            for l in range(math.ceil(heightRatio*j),math.ceil(heightRatio*(j+1))):
                pixelsum[0] += loadedImage[k, l][0]
                pixelsum[1] += loadedImage[k, l][1]
                pixelsum[2] += loadedImage[k, l][2]

        #average the pixel values
        for k in range(0,3):
            pixelsum[k] /= (math.ceil(heightRatio*j)-math.ceil(heightRatio*(j+1))) * (math.ceil(widthRatio*i)-math.ceil(widthRatio*(i+1)))
            pixelsum[k] = int(pixelsum[k])
        
        #update the pixel values of the original image
        for k in range(math.ceil(widthRatio*i), math.ceil(widthRatio*(i+1))):
            for l in range(math.ceil(heightRatio*j),math.ceil(heightRatio*(j+1))):
                loadedImage[k, l] = tuple(pixelsum)

#save the image
im.save("AppleImageAverage.jpeg")



