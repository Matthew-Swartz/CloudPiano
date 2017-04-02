#Matthew Swartz
#TribeHacksIII
#Image Slicer
#take an image, parse it by column of pixels, return a discrete value for each 
#column based on the pixels in said column
#Supports .gif and .png
#does not support .jpg

from PIL import Image


#stores each pixel value into an array
def imagetoarray(image):
    
    im = Image.open(image)
    box = im.getbbox()
    width = box[2]
    #x value
    height = box[3]
    #y value
    masterlist = []
    
    for k in range(0,width):
        for j in range(0,height):
            if (image[-4:] == ".png"):
                tup = im.getpixel((k,j))
                temp = tup[0] + tup[1] + tup[2] + tup[3]
            else:
                temp = im.getpixel((k,j))            
            masterlist.append(temp)
        
    return masterlist


#stores the sum of the pixel values for each column in an array and returns it
def imagetocol(image):
    im = Image.open(image)
    box = im.getbbox()
    width = box[2]
    #x value
    height = box[3]
    #y value
    masterlist = []
    
    for k in range(0, width):
        temp = 0
        for j in range(0,height):
            if (image[-4:] == ".png"):
                tup = im.getpixel((k,j))
                temp = temp + tup[0] + tup[1] + tup[2] + tup[3]
            else:
                temp += im.getpixel((k,j))
        masterlist.append(temp)
    return masterlist
        
        
#stores the sum of the pixel values for each row in an array and returns it
def imagetorow(image):
    im = Image.open(image)
    box = im.getbbox()
    width = box[2]
    #x value
    height = box[3]
    #y value
    masterlist = []
    
    for k in range(0, height):
        temp = 0
        for j in range(0,width):
            if (image[-4:] == ".png"):
                tup = im.getpixel((j,k))
                temp = temp + tup[0] + tup[1] + tup[2] + tup[3]
            else:
                temp += im.getpixel((j,k))
        masterlist.append(temp)
    return masterlist