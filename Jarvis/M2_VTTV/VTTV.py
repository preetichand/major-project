import speech_recognition as sr
import pyttsx3
import speech_recognition as sr  
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  #female voice:id-[1]  #male voice :id-[0]
class text_voice:

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def takeCommand():
    #It takes microphone input from the user and returns string output
        
       
           rObject = sr.Recognizer() 
           audio = '' 
           with sr.Microphone() as source: 
               print("Listening...") 
               # recording the audio using speech recognition 
               audio = rObject.listen(source, phrase_time_limit = 8)  
           try: 
             print("Recognizing...")   
             query = rObject.recognize_google(audio, language ='en-in') 
             print(f"User said: {query}\n")
           except Exception as e:   
                print("Say that again please...")  
                return "None"
           else:
               return query    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
