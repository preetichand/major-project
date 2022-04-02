import sys
sys.path.append('D:\major project\Jarvis')
from  tkinter import*
from tkinter.filedialog import*
from M5_PDFG.pdfg import pdf_converter as pdf  

def editor():
    master=Tk()
    pt=pytext(master)
    master.mainloop()

def editor2():
    master=Tk()
    pt=pytext2(master)
    master.mainloop()



class menubar():
    def __init__(self,parent):
       font_specs=("ubuntu",14) 
       self.menubar=Menu(parent.master,font=font_specs)
       parent.master.config(menu=self.menubar)
       
       file_dropdown=Menu(self.menubar,font=font_specs,tearoff=0)
       file_dropdown.add_command(label="okay ",command=parent.okay)
       file_dropdown.add_separator()
       file_dropdown.add_command(label="Exit",command=parent.master.destroy)
      
       self.menubar.add_cascade(label="file",menu=file_dropdown)

class pytext:
    
    def __init__(self,master):
       master.title("doc.txt")
       master.geometry("1200x700")
      
       font_specs=("ubuntu",18)
       self.master=master #to access it from menubar class
       self.filename=None
       self.textarea=Text(master,font=font_specs)
       self.scroll=Scrollbar(master,command=self.textarea.yview)#scroll it through y axis
       self.textarea.configure(yscrollcommand=self.scroll.set)
       self.textarea.pack(side=LEFT,fill=BOTH,expand=True)
       self.scroll.pack(side=RIGHT,fill=Y)
       self.menubar=menubar(self) #creating object to class
       with open('doc.txt','r') as f:
         self.textarea.insert(1.0,f.read())
    
        
    def okay(self):
        try:
               textarea_content=self.textarea.get(1.0,END)
               with open('doc.txt','w') as f:
                   f.write(textarea_content)
               pdf.generate_pdf()
 
        except Exception as e:
                print(e)



class pytext2:
    
    def __init__(self,master):
       master.title("pers.txt")
       master.geometry("1200x700")
      
       font_specs=("ubuntu",18)
       self.master=master #to access it from menubar class
       self.filename=None
       self.textarea=Text(master,font=font_specs)
       self.scroll=Scrollbar(master,command=self.textarea.yview)#scroll it through y axis
       self.textarea.configure(yscrollcommand=self.scroll.set)
       self.textarea.pack(side=LEFT,fill=BOTH,expand=True)
       self.scroll.pack(side=RIGHT,fill=Y)
       self.menubar=menubar(self) #creating object to class
       with open('pers.txt','r') as f:
         self.textarea.insert(1.0,f.read())
    
        
    def okay(self):
        try:
               textarea_content=self.textarea.get(1.0,END)
               with open('pers.txt','w') as f:
                   f.write(textarea_content)
               #pdf.generate_pdf()
 
        except Exception as e:
                print(e)
    


