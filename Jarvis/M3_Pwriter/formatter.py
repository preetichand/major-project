import sys
sys.path.append('C:\Project Git Hub\Jarvis_Assistant\Jarvis')  
from M2_VTTV.VTTV import text_voice as v

class format:
    def set_format():
        info={}
        v.speak("Hello Doctor, what is Patient's name")
        info.update({"Name":v.takeCommand().title()})

        v.speak("What is the gender")
        s=v.takeCommand().title()
        if 'M' in s:
            info.update({"Gender":"Male"})
        else:
            info.update({"Gender":"Female"})
        v.speak("What is the age")
        info.update({"Age":v.takeCommand().title()})

        v.speak("What are the Symptons")
        info.update({"Problem":v.takeCommand().title()})

        v.speak("What are the Diagnosis")
        info.update({"Diagnosis":v.takeCommand().title()})

        v.speak("What are the Prescriptions")
        info.update({"Prescriptions":v.takeCommand().title()})

        v.speak("Any advice doctor")
        info.update({"Advice":v.takeCommand().title()})
        v.speak("Thanks for the information") 

        return info

class dr_detail:
    def set_detail():
        pers_detail=[]
        v.speak("Hi Doctor , what is your Clinic name")
        pers_detail.append("        "+v.takeCommand().upper())
        v.speak("Doctor, what is your name")
        str = v.takeCommand()
        if str[0]=='D' and str[1]=='r':
            pers_detail.append(str.title())
        else:
            pers_detail.append("Dr."+str.title())
        v.speak("What is your qualifications")
        pers_detail.append(v.takeCommand().upper())
        v.speak("What is your Phone number")
        num = list(v.takeCommand())
        sp=' '
        for i in num:
            if i == sp:
                num.remove(i)
        str1=''
        str1 = str1.join(num)
        pers_detail.append(str1)
        v.speak("Your Clinic Address")
        pers_detail.append(v.takeCommand().title())
        v.speak("Any other information doctor")
        pers_detail.append(v.takeCommand().title())

        return pers_detail


