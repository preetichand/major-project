import datetime as dt
class file_op:
  def write_text(query):
    try:
      with open("pers.txt") as f:
        with open("doc.txt", "w") as f1:
          for line in f:
            f1.write(line)
          f1.write("Patient Details-"+"\n\n")
          for x, y in query.items():
            f1.write(x+':-'+y+'\n')
          f1.write('Date:-%s'%(dt.date.today()))
          f1.write('\n')
          str1=str(dt.datetime.now().time())[0:8] 
          f1.write('Time:-%s'%(str1)) 
    except:
      f1=open("doc.txt", "w")
      f1.write("Patient Details-"+"\n\n")
      for x, y in query.items():
        f1.write(x+':-'+y+'\n')
      f1.write('Date:-%s'%(dt.date.today()))
      f1.write('\n')
      str1=str(dt.datetime.now().time())[0:8]
      f1.write('Time:-%s'%(str1)) 

  def write_detail(query):
    myfile = open('pers.txt', 'w+')
    myfile.write("___________________________"+"\n"+"----------------------"+"\n")
    for x in query:
      if x != 'None' and 'No' not in x:
        myfile.write(x+"\n")
    myfile.write("___________________________"+"\n"+"----------------------"+"\n\n")
    
