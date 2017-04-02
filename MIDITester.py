#Matthew Swartz MIDI converter
#TribeHacksIII 3/31/2017
#Goal is to grab doppler .gif off of Weather Services website
#Parse this image by column of pixels and then convert each column into a note
#for a MIDI file


from mido import MidiFile, Message, MidiTrack

#Test song
#mid = MidiFile('Test_-_test1.mid')

#for i, track in enumerate(mid.tracks):
    #print('Track {}: {}'.format(i, track.name))
    #for msg in track:
        #print(msg)
        
#Default Song
        
#mid2 = MidiFile()
#track = MidiTrack()
#mid2.tracks.append(track)

#track.append(Message('program_change', program=12, time=0))
#track.append(Message('note_on', note=64, velocity=64, time=32))
#track.append(Message('note_off', note=64, velocity=127, time=32))

#mid2.save('new_song.mid')

#Random song

mid3 = MidiFile(type=2)
track2 = MidiTrack()
mid3.tracks.append(track2)

track2.append(Message('program_change', program=12, time=0))

for x in range(0,300):
    j = (x^5 + 13* (x^4) - 7 * (x^3) + 23 * (x^2) + 17) % 64
    track2.append(Message('note_on', channel = 12, note=j, velocity=j, time=32))
    track2.append(Message('note_off',channel = 12,  note=j, velocity=j, time=32))
    
track3 = MidiTrack()
mid3.tracks.append(track3)

track3.append(Message('program_change', program=12, time=0))

for x in range(0,300):
    j = (x^5 + 7* (x^4) - 23 * (x^3) + 13* (x^2) + 19) % 64
    track3.append(Message('note_on', channel = 9, note=j, velocity=j, time=32))
    track3.append(Message('note_off',channel = 9,  note=j, velocity=j, time=32))    
    
track4 = MidiTrack()
mid3.tracks.append(track4)

track4.append(Message('program_change', program=12, time=0))

for x in range(0,300):
    j = (x^5 + 7* (x^4) - 23 * (x^3) + 13* (x^2) + 19) % 64
    track4.append(Message('note_on', channel = 7, note=j, velocity=j, time=32))
    track4.append(Message('note_off',channel = 7,  note=j, velocity=j, time=32))  
    
mid3.save('who_knows.mid')

#def TrackChecker():
    ##creates a midifile that runs through the range of each channel to get an idea
    ##of what they sound like
    #for x in range(0,16):
        #file = "channeltest" + str(x) + ".mid"
        ##print(file)
        
        #mid = MidiFile()
        #track = MidiTrack()
        #mid.tracks.append(track)
        
        #track.append(Message('program_change', program=12, time = 0))
        #for y in range(0,128):
            #track.append(Message('note_on', channel = x, note=y, velocity=64, time=32))
            #track.append(Message('note_off', channel = x, note=y, velocity=64, time=32))
            
        #mid.save(file)
        

