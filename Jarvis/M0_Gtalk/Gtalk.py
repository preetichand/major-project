import datetime
import sys  
sys.path.append('C:\Project Git Hub\Jarvis_Assitant')  
from M2_VTTV.VTTV import text_voice as v
from M9_SentToUser.mail import Email_Sent as es
    
class gtalk(object):
    
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            v.speak("Good Morning!")

        elif hour>=12 and hour<18:
            v.speak("Good Afternoon!")   

        else:
            v.speak("Good Evening!")  

        v.speak("I am Jarvis. Please tell me how may I help you") 

        
            
    def askformail():
        v.speak("Can I send this PDF file to the patient's mail?")
        while True:
            str2 = v.takeCommand().lower()
            if 'y' in str2 or 'jarvis' in str2 or 'send' in str2:
                with open("name.txt","r") as f:
                    name = f.read()
                es.sendPDF(name)
                break
            
            elif 'None' in str2:
                v.speak("Sorry, can you please repeat")

            else:
                break
