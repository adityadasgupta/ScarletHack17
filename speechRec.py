import json
import speech_recognition as sr
r = sr.Recognizer()
r.energy_threshold = 750


def speech2text():
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)
        try:
            audio_command = r.recognize_google(audio)
            return audio_command

        except:
            pass

def toJson(audioStr) :
    obj =  open('utter.json' , 'w')
    dict1 = {
    'utter' : audioStr
    };
    json.dump(dict1, obj)
    #return jsn
# def toFile(j) :
#     obj =  open('utter.json' , 'wb')
#     obj.write(j)
#     obj.close

a = speech2text()
toJson(a)
#print(data)
#toFile(data)