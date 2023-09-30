import os 
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename): 
    mytext = str(text)
    language = "ta"
    myobj = gTTS(text=mytext,lang=language, slow=False)
    myobj.save(filename)


def mergeAudio(audios):
    combine = AudioSegment.empty()
    for audio in audios:
        combine += AudioSegment.from_mp3(audio)
    return combine

def generating():
    '''ek mp3 se particular second se wo second tak hona karko export hotaso
    isme second se millisecond ko convert karko haiso'''
     
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 159500
    finish = 162500
    audioprocessing = audio[start:finish]
    audioprocessing.export("1_Tamil.mp3", format="mp3")
     
    audio = AudioSegment.from_mp3("announce.mp3")
    start = 162580
    finish = 163600
    audioprocessing = audio[start:finish]
    audioprocessing.export("2_Tamil.mp3", format="mp3")

    audio = AudioSegment.from_mp3("announce.mp3")
    start = 170000
    finish =171000
    audioprocessing = audio[start:finish]
    audioprocessing.export("5_Tamil.mp3", format="mp3")

    audio = AudioSegment.from_mp3("announce.mp3")
    start = 172000
    finish = 172800
    audioprocessing = audio[start:finish]
    audioprocessing.export("8_Tamil.mp3", format="mp3")

    audio = AudioSegment.from_mp3("announce.mp3")
    start = 177000
    finish = 178000
    audioprocessing = audio[start:finish]
    audioprocessing.export("11_Tamil.mp3", format="mp3")

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
generateAnnouncement("Book.xlsx") 
