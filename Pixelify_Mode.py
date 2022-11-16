'''
This file finds the most common pixel values in a given block of the image to "pixelify" the image
The final output does maintain the original size of the image but it has appears like an n x m pixel image.
Where n and m are the desiredWidth and desiredHeight respectively.
'''
#import the necessary libraries
from PIL import Image
import math
import statistics

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
        pixelsum = []

        #iterate through the pixels in the original image that correspond to the current desired pixel
        for k in range(math.ceil(widthRatio*i), math.ceil(widthRatio*(i+1))): 
            for l in range(math.ceil(heightRatio*j),math.ceil(heightRatio*(j+1))):
                #append the pixel values to a list, where each set of 3 digits is an RGB value ie. (255,255,255) = 255255255
                pixelsum.append(loadedImage[k, l][0] + loadedImage[k, l][1]*1000 + loadedImage[k, l][2]*1000000)
        #average the pixel values
        pixelsum =  statistics.mode(pixelsum)
        pixelsum = (pixelsum % 1000, (pixelsum // 1000) % 1000, pixelsum // 1000000)
        
        #update the pixel values of the original image
        for k in range(math.ceil(widthRatio*i), math.ceil(widthRatio*(i+1))):
            for l in range(math.ceil(heightRatio*j),math.ceil(heightRatio*(j+1))):
                loadedImage[k, l] = tuple(pixelsum)

#save the image
im.save("AppleImageMode.jpeg")



