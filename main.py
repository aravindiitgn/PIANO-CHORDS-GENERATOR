from tkinter import *
from pydub import AudioSegment
from pydub.playback import play
def cleartext():
    T.delete("1.0","end")

sound={1:'C.wav',2:'C#.wav',3:'D.wav',4:'D#.wav',5:'E.wav',6:'F.wav',7:'F#.wav',8:'G.wav',9:'G#.wav',10:'A.wav',11:'A#.wav',12:'B.wav'}
sound_1={1:'C',2:'C#',3:'D',4:'D#',5:'E',6:'F',7:'F#',8:'G',9:'G#',10:'A',11:'A#',12:'B'}
#Function to close the program
def mod(x):
    if x>12:
     return(x%12)
    else:
     return(x)

def closewindow():
    exit()
#Creating the function for identifying KEY and TYPE

def Play_Sound(p,q,r):
    T.insert(END,'Notes:     '+sound_1[p]+'    '+sound_1[q]+'    '+sound_1[r])
    audio_1=AudioSegment.from_file(sound[p])
    audio_2=AudioSegment.from_file(sound[q])
    audio_3=AudioSegment.from_file(sound[r])
    mixed=audio_1.overlay(audio_2)
    mixed1=mixed.overlay(audio_3)
    mixed1.export("mixed.wav",format='wav')
    play(mixed1)


def Play_Sound1(p,q,r,s):
    T.insert(END,'Notes:     '+sound_1[p]+'    '+sound_1[q]+'    '+sound_1[r]+'    '+sound_1[s])
    audio_1=AudioSegment.from_file(sound[p])
    audio_2=AudioSegment.from_file(sound[q])
    audio_3=AudioSegment.from_file(sound[r])
    audio_4=AudioSegment.from_file(sound[s])
    mixed=audio_1.overlay(audio_2)
    mixed1=mixed.overlay(audio_3)
    mixed2=mixed1.overlay(audio_4)
    mixed2.export("mixed.wav",format='wav')
    play(mixed2)


def Play_Major(k):
    key_1=mod(k)
    key_2=mod(k+4)
    key_3=mod(k+7)

    Play_Sound(key_1,key_2,key_3)
def Play_Minor(k):
    key_1=mod(k)
    key_2=mod(k+3)
    key_3=mod(k+7)
    Play_Sound(key_1,key_2,key_3)
def Play_Diminished(k):
    key_1=mod(k)
    key_2=mod(k+3)
    key_3=mod(k+6)
    Play_Sound(key_1,key_2,key_3)
def Play_7th(k):
    key_1=mod(k)
    key_2=mod(k+4)
    key_3=mod(k+7)
    key_4=mod(k+10)
    Play_Sound1(key_1,key_2,key_3,key_4)

def Play_Min7th(k):
    key_1=mod(k)
    key_2=mod(k+3)
    key_3=mod(k+7)
    key_4=mod(k+10)
    Play_Sound1(key_1,key_2,key_3,key_4)
def Play_Maj7th(k):
    key_1=mod(k)
    key_2=mod(k+4)
    key_3=mod(k+7)
    key_4=mod(k+11)
    Play_Sound1(key_1,key_2,key_3,key_4)
def playchord():
 key=str(KEY.get())
 type=str(TYPE.get())
 keys={'C':1,'C#':2,'D':3,'D#':4,'E':5,'F':6,'F#':7,'G':8,'G#':9,'A':10,"A#":11,'B':12}
 for k,v in keys.items():
     if key==k:
         a=v
 cleartext()
 if type=='Major':
     Play_Major(a)
 elif type=='Minor':
    Play_Minor(a)
 elif type=='Diminished':
   Play_Diminished(a)
 elif type=='7th':
   Play_7th(a)
 elif type=='Min.7th':
   Play_Min7th(a)
 elif type=='Maj.7th':
   Play_Maj7th(a)

#Creating the window
window=Tk()

Back=Canvas(window,bg="lemon chiffon",height=800,width=800)
Back.pack()
window.maxsize(800,500)
window.title("PIANO CHORDS")
#Creating the Headings
Heading=Label(window,text="PIANO CHORD PRODUCER",font=("Times",30))
Heading.pack()
Heading.place(x=225,y=10)
Heading_1=Label(window,text="*************************",font=("Times",30))
Heading_1.pack()

Heading_1.place(x=225,y=40)

Heading1=Label(window,text="KEY:",font=("Courier",15))
Heading1.pack()
Heading1.place(x=100,y=200)

Heading1=Label(window,text="TYPE:",font=("Courier",15))
Heading1.pack()
Heading1.place(x=500,y=200)
#Creating the DROP DOWN LISTS
KEY=StringVar()
set1=OptionMenu(window,KEY,"C","C#","D","D#","E","F","F#","G","G#","A","A#","B")
set1.configure(font=("Arial",25))
set1.pack()
set1.place(x=225,y=190)

TYPE=StringVar()
set2=OptionMenu(window,TYPE,"Major","Minor","Diminished","7th","Min.7th","Maj.7th")
set2.configure(font=("Arial",25))
set2.pack()
set2.place(x=600,y=190)
#Creating the Buttons
button=Button(window,text="PRODUCE",font=("Times",20),command=playchord)
button.pack()

button.place(x=275,y=300)
"""
button=Button(window,text="CLEAR",font=("Times",10),command=cleartext)
button.pack()

button.place(x=300,y=350)
"""

button=Button(window,text="EXIT",font=("Times",20),command=closewindow)
button.pack()
button.place(x=500,y=300)
T=Text(window,height=3,width=25)
T.pack()

T.place(x=275,y=450)

T.configure(font=("Arial",25))

mainloop()
