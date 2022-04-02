from M2_VTTV.VTTV import text_voice as v
import os
import smtplib 
from email.message import EmailMessage

class Email_Sent:

    def sendPDF(uniq_filename):
        EMAIL_ADDRESS = os.environ.get('my_mail')
        EMAIL_PASSWORD = os.environ.get('my_password')

        doc = "Thanks and regards\n"
        msg = EmailMessage()
        msg['Subject'] = "Patient Details"
        msg['From'] = EMAIL_ADDRESS

        v.speak("Please enter Patient's Mail")
        msg['To'] = input("Enter Patient's Mail:")
        str1 = ""
        with open("pers.txt") as f:
            r = f.readlines()
            for i in range(3,len(r)):
                str1 =str1+r[i]
        
        msg.set_content(doc+str1)
        s = 'D:\\major project\\Jarvis\\'
        s = s+uniq_filename
        
        with open(s,'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype='application' , subtype='octet-stream' , filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
     
    
