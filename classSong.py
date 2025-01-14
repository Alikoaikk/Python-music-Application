from mutagen.mp3 import MP3

class song () :
    def __init__ (self , row , name , img , file) :
        self.row = row 
        self.name = name 
        self.img = img 
        self.file = file

    def length (self) : 
        audio = MP3(self.file)
        length = audio.info.length
        return length