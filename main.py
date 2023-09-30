import os 
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

#ye function aako text se 12640 karko agrument aataso filename aako wo text se 12640 boltaso
def textToSpeech(text, filename): #text- inne boltaso, file- file sech boltaso
    mytext = str(text)
    language = "ta"
    myobj = gTTS(text=mytext,lang=language, slow=False)
    myobj.save(filename)

#the function return pydub audio segment
def mergeAudio(audios):
    combine = AudioSegment.empty()#ek empty set laga lako empty hojata ek mp3 usme hamey merge karnso
    for audio in audios:
        combine += AudioSegment.from_mp3(audio)
    return combine

def generating():
    '''ek mp3 se particular second se wo second tak hona karko export hotaso
    isme second se millisecond ko convert karko haiso'''
     
    #generating payanigalin
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 159500
    finish = 162500
    audioprocessing = audio[start:finish]
    audioprocessing.export("1_Tamil.mp3", format="mp3")
     
    #2.generating train number announce like vandi en
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 162580
    finish = 163600
    audioprocessing = audio[start:finish]
    audioprocessing.export("2_Tamil.mp3", format="mp3")

   #3.creating a train number

   #4.from city

   #5.generaing via
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 170000
    finish =171000
    audioprocessing = audio[start:finish]
    audioprocessing.export("5_Tamil.mp3", format="mp3")

    #6. ye raasta se janga

   #8.generating ke raaste
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 172000
    finish = 172800
    audioprocessing = audio[start:finish]
    audioprocessing.export("8_Tamil.mp3", format="mp3")

   #7.to city

   #9.creating train name

   #10.creating a number for platform

   #11.platform name
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 177000
    finish = 178000
    audioprocessing = audio[start:finish]
    audioprocessing.export("11_Tamil.mp3", format="mp3")

   #12.generating janga
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 181000
    finish =183000
    audioprocessing = audio[start:finish]
    audioprocessing.export("12_Tamil.mp3", format="mp3") 

def generateAnnouncement(filename):
    var = pd.read_excel(filename)
    print(var)
    for index, item in var.iterrows():
        #3.creating a train number
        textToSpeech(item['Train No'], "3_Tamil.mp3")

        #4.from city
        textToSpeech(item['from'], "4_Tamil.mp3")

        #6. ye raasta se janga
        textToSpeech(item['via'], "6_Tamil.mp3")

        #7.to city
        textToSpeech(item['to'], "7_Tamil.mp3")

        #9.creating train name
        textToSpeech(item['Train name'], "9_Tamil.mp3")

        #10.creating a number for platform
        textToSpeech(item['platform'], "10_Tamil.mp3")

        audios = [f"{i}_Tamil.mp3" for i in range(1,13)]

        announcemet = mergeAudio(audios)
        announcemet.export(f"announcemet_{item['Train No']}_{index+1}.mp3", format="mp3")


print("Generating...")
generating()
print("generating Announcement")
generateAnnouncement("Book.xlsx") #pandas se read karteso ye excel file ko