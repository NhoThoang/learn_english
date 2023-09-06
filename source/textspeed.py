import pyttsx4
import threading
lock = threading.Lock()
class textspeed:
    def __init__(self,pathfile1,i) -> None:
        self.i = i
        # self.gender = gender
        self.pathfile1=pathfile1
    def txt_dict(self):
        with open(self.pathfile1) as file:
            s = "".join(str(j)for j in file).replace('\n', ',')
            d = dict(enumerate(s.split(",")))
            return d
    def EN_voice(self):
        # with lock:
        d= self.txt_dict()
        engine = pyttsx4.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) # change index to change voice
        engine.setProperty('rate', 120)
        engine.say(d[self.i])
        engine.runAndWait()
# textspeed('./text/animal.txt',2,1).EN_voice()




