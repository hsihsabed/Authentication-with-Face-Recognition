import pyttsx3
def Say(y):
    y = str(y)
    
    engine = pyttsx3.init()
    engine.say(y)
    engine.setProperty('rate',60)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()
