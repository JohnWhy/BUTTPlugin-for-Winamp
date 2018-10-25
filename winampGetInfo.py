from winamp import *
import time

w = winamp()
#print(w.getPlayingStatus())

def UpdateArtistSong():
    string = w.getCurrentTrackName()
    string = string.split(' ')
    #print(string)
    string[0] = ''
    string[-1] = ''
    string[-2] = ''
    string = ' '.join(string)
    print(string)
    with open('BUTTInfo.txt','w') as f:
        f.write(string)
    f.close()

while(True): 
    time.sleep(5)     
    UpdateArtistSong()  
