#Final tribehacks submission
#Matthew Swartz

from mido import MidiFile, Message, MidiTrack
from PIL import Image
import ImageSlicer
import DopplerGrab

imagename = DopplerGrab.CurrDoppName()

# DONE: Grab automatically off the net
# imagename = input("Enter image name to convert: ")

# remove need for user input

inputarray = ImageSlicer.imagetocol(imagename)

#singe track from array of piano
def SingleTrack(array):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    for pix in inputarray:
        
        r = hash1(pix)
        track.append(Message('note_on', channel = 10, note= r, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= r, velocity=64, time=32))
        #time attribute is actually superflous in this particular library 
        #but whatever

    
    savefile = imagename[:-4] +"_st" + ".mid"
    mid.save(savefile)

#two piano tracks 
def DoubleTrack(array):
    mid = MidiFile(type=2)
    track = MidiTrack()
    track2 = MidiTrack()
    mid.tracks.append(track)
    mid.tracks.append(track2)
    
    for pix in inputarray:
        r = hash1(pix)
        s = hash4(pix)
        track.append(Message('note_on', channel = 10, note= r, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= r, velocity=64, time=32))
        track2.append(Message('note_on', channel = 0, note= s, velocity=64, time=32))
        track2.append(Message('note_off',channel = 0,  note= s, velocity=64, time=32))          
    
        
    savefile = imagename[:-4] +"_dt" + ".mid"
    mid.save(savefile)  
    
#piano track and percussion track
def DoublePercuss(array):
    mid = MidiFile(type=2)
    track = MidiTrack()
    track2 = MidiTrack()
    mid.tracks.append(track)
    mid.tracks.append(track2)
    
    for pix in inputarray:
        r = hash1(pix)
        s = hash4(pix)
        track.append(Message('note_on', channel = 10, note= r, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= r, velocity=64, time=32))
        track2.append(Message('note_on', channel = 9, note= s, velocity=64, time=32))
        track2.append(Message('note_off',channel = 9,  note= s, velocity=64, time=32))    
        
    savefile = imagename[:-4] +"_dp" + ".mid"
    mid.save(savefile)
    
#like single track but with pauses to slow it
def SlowTrack(array):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    for pix in inputarray:
        r = hash1(pix)
        track.append(Message('note_on', channel = 10, note= r, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= r, velocity=64, time=32))
        track.append(Message('note_on', channel = 10, note= 0, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= 0, velocity=64, time=32))        
        #time attribute is actually superflous in this particular library 
        #but whatever
    
    
    savefile = imagename[:-4] +"_slw" + ".mid"
    mid.save(savefile)
    
# like double track but with pauses to slow it
def DoubleTrackSlow(array):
    mid = MidiFile(type=2)
    track = MidiTrack()
    track2 = MidiTrack()
    mid.tracks.append(track)
    mid.tracks.append(track2)
    
    for pix in inputarray:
        r = hash1(pix)
        s = hash4(pix)
        track.append(Message('note_on', channel = 10, note= r, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= r, velocity=64, time=32))
        track.append(Message('note_on', channel = 10, note= 0, velocity=64, time=32)) #pause
        track.append(Message('note_off',channel = 10,  note= 0, velocity=64, time=32))#pause  
        track2.append(Message('note_on', channel = 0, note= s, velocity=64, time=32))
        track2.append(Message('note_off',channel = 0,  note= s, velocity=64, time=32)) 
        track2.append(Message('note_on', channel = 0, note= 0, velocity=64, time=32)) #pause
        track2.append(Message('note_off',channel = 0,  note= 0, velocity=64, time=32))#pause   
    
        
    savefile = imagename[:-4] +"_dslw" + ".mid"
    mid.save(savefile)    


#like double percussion track but with pauses to slow it
def DoublePercusslow(array):
    mid = MidiFile(type=2)
    track = MidiTrack()
    track2 = MidiTrack()
    mid.tracks.append(track)
    mid.tracks.append(track2)
    
    for pix in inputarray:
        r = hash1(pix)
        s = hash4(pix)
        track.append(Message('note_on', channel = 10, note= r, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= r, velocity=64, time=32))
        track.append(Message('note_on', channel = 10, note= 0, velocity=64, time=32)) #pause
        track.append(Message('note_off',channel = 10,  note= 0, velocity=64, time=32))#pause  
        track2.append(Message('note_on', channel = 9, note= s, velocity=64, time=32))
        track2.append(Message('note_off',channel = 9,  note= s, velocity=64, time=32)) 
        track2.append(Message('note_on', channel = 9, note= 0, velocity=64, time=32)) #pause
        track2.append(Message('note_off',channel = 9,  note= 0, velocity=64, time=32))#pause   
    
        
    savefile = imagename[:-4] +"_dpslw" + ".mid"
    mid.save(savefile)  
    
 
# makes one piano track from the column array and a backing track from 
# the row array
def CrossSong(array):
    inputarray2 = ImageSlicer.imagetorow(imagename)
    mid = MidiFile(type=2)
    track = MidiTrack()
    track2 = MidiTrack()
    mid.tracks.append(track)
    mid.tracks.append(track2)
    
    for pix in inputarray:
        r = hash1(pix)
        
        track.append(Message('note_on', channel = 10, note= r, velocity=64, time=32))
        track.append(Message('note_off',channel = 10,  note= r, velocity=64, time=32))
        
        
    for tix in inputarray2:
        s = hash4(tix)
        track2.append(Message('note_on', channel = 0, note= s, velocity=64, time=32))
        track2.append(Message('note_off',channel = 0,  note= s, velocity=64, time=32))          
    
        
    savefile = imagename[:-4] +"_crs" + ".mid"
    mid.save(savefile)     

#hashing functions for the pixel values

def hash1(x):
    j = (x^5 + 7* (x^4) - 23 * (x^3) + 13* (x^2) ) % 128
    return j

def hash2(x):
    j = (x^5 + 7* (x^4) - 23 * (x^3) + 13* (x^2) ) % 64
    return j 

def hash3(x):
    j = (x^5 + 13* (x^4) - 7 * (x^3) + 23 * (x^2) ) % 128
    return j

def hash4(x):
    j = (x^5 + 13* (x^4) - 7 * (x^3) + 23 * (x^2) ) % 64
    return j



#main function

#I ended up liking this function the best
DoublePercusslow(inputarray)
