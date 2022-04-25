from pymongo import MongoClient
from M2_VTTV.VTTV import text_voice as v

class Database_Insert:

    def Insert(): 
        
        client = MongoClient('localhost',27017)
        mydb = client["Jarvis"]
        mycol = mydb["details"]

        d = {}
        with open("doc.txt") as f:
            while True: 
                a = f.readline()
                if not a:
                    break
                else:
                    a = a.split(':-')
                    try:
                        key = a[0]
                        val = a[1].strip('\n')
                        d.update({key:val})
                    except:
                        pass
            #print(d)
        x = mycol.insert_one(d)
    
class Database_Retrieve:

    def retrieve():
        client = MongoClient('localhost',27017)
        mydb = client["Jarvis"]
        mycol = mydb["details"]
        
        print("Enter 1 for Single keyword\nEnter 2 for Multiple Keyword")
        choice=int(input("Enter your choice:"))
        try:
          if(choice==1):
             v.speak('here are the keywords')
             print('1.Name\n2.Gender\n3.Age\n4.Diagnosis\n5.Date')
             query=input('Enter the keyword:').title()
             value=input('Enter the corrosponding value:').title()
             myquery={query:{"$regex":value}}
             
          elif(choice==2):
              list=[]
              n=int(input('Enter no of keywords:'))
              for _ in range(n):
                  dict={}
                  key=input("Enter key:").title()
                  value=input("Enter value:").title()
                  dict.update({key:value}) 
                  list.append(dict) 
              myquery={"$and":list}
              
        except :
            print("Wrong choice")

        else:
            for x in mycol.find(myquery):
                 print(x)
       
class Database_update:
      
      def update(object):
          client = MongoClient('localhost',27017)
          mydb = client["Jarvis"]
          mycol = mydb["details"]
          object.retrieve()
          try:
            n=int(input('Enter the no of fields to be changed:'))
            dict={}
            for _ in range(n):
               key=input('Enter the field to be changed:').title()
               value=input('Enter the new value of the field:').title() 
               dict.update({key:value})
          
            time_value=input('Enter the time field:')
            mycol.update_one({'Time':time_value},{"$set":dict})
          
          except  Exception as e:
            print(e)
          
          else:
            print('Record updated successfully')
         
         

class Database_delete:
      
    def delete():
          client = MongoClient('localhost',27017)
          mydb = client["Jarvis"]
          mycol = mydb["details"]

          try:
            time_value=input('Enter the time field of the record to be deleted:')
            mycol.delete_one({'Time':time_value})
          
          except Exception as e:
            print(e)

          else:
            print ('Deletion successful') 
        

          
              
      