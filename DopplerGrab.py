#DopplerGrab
#Matthew Swartz
# Grabs the latest doppler radar gif

from PIL import Image
import urllib
import datetime

#sets name of file format, you can change the filename variable if you want it
#to be less verbose
now = datetime.datetime.now()
filename = "currentradar"+ str(now.year) + "_"+ str(now.month) + "_"+ str(now.day) +"_" + str(now.hour) + "_"+ str(now.minute) + ".gif"

#displays current doppler image 
def showCurrDopp():
    urllib.urlretrieve("https://radar.weather.gov/ridge/Conus/RadarImg/latest_radaronly.gif", filename)
    im = Image.open(filename)
    im.show()

#only downloads the picture and saves it under currentrader.gif
def setCurrDopp():
    urllib.urlretrieve("https://radar.weather.gov/ridge/Conus/RadarImg/latest_radaronly.gif", filename)
    

#returns the image
def getCurrDopp():
    urllib.urlretrieve("https://radar.weather.gov/ridge/Conus/RadarImg/latest_radaronly.gif", filename)
    im = Image.open(filename)
    return im

#returns the name
def CurrDoppName():
    urllib.urlretrieve("https://radar.weather.gov/ridge/Conus/RadarImg/latest_radaronly.gif",filename)
    return filename
