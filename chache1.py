import json 
import os 
import database
def add_settings(id,rw=2,heading="",label=None,photo=None,video=None):
 path=str(id)+".json" 
 if os.path.exists(path):
#  print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"]
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          l={"last_button":b, "row_width":str(rw),"file_id":file_id,"label":label,"headings":heading}
          p=json.dumps(l) 
  #  print (p)
          f.write(p) 
 else :
  with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          l={ "row_width":str(rw),"photo":photo,"video":video,"label":label,"headings":heading}
          p=json.dumps(l) 
  #  print (p)
          f.write(p) 
def add_photo(id,rw=None):
 path='sessions/'+str(id)+".json" 
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         kerd["photo"]=rw
         kerd["video"]=None 
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          #l={"last_button":b, "row_width":str(rw),"file_id":file_id,"label":label,"headings":heading}
          p=json.dumps(kerd) 
  #  print (p)
          f.write(p) 
 else:
  with open (path, 'w') as f:
      l={
          "last_button":"", 
           "row_width":2,
           "title":"", 
           "heading":"", 
            "photo":rw, 
            "video":None
      }
      po=json.dumps(l)
      f.write(po)
def add_video(id,rw=None):
 path='sessions/'+str(id)+".json"
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         kerd["video"]=rw
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          #l={"last_button":b, "row_width":str(rw),"file_id":file_id,"label":label,"headings":heading}
          p=json.dumps(kerd) 
  #  print (p)
          f.write(p) 
 else:
  with open (path, 'w') as f:
      l={
          "last_button":"", 
           "row_width":2,
           "title":"", 
           "heading":"", 
            "video":rw, 
            "photo":None
      } 
      po=json.dumps(l)
      f.write(po)
def add_title(id,rw="Button"):
 path='sessions/'+str(id)+".json"
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         kerd["title"]=rw
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          #l={"last_button":b, "row_width":str(rw),"file_id":file_id,"label":label,"headings":heading}
          p=json.dumps(kerd) 
  #  print (p)
          f.write(p)
def add_heading(id,rd=""):
 path='sessions/'+str(id)+".json"
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         print ("rd" + rd +"done")
         kerd["heading"]=rd
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          #l={"last_button":b, "row_width":str(rw),"file_id":file_id,"label":label,"headings":heading}
          p=json.dumps(kerd) 
  #  print (p)
          f.write(p)
def add_row_width(id,rw=2):
 path='sessions/'+str(id)+".json"
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         kerd["row_width"]=rw
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          #l={"last_button":b, "row_width":str(rw),"file_id":file_id,"label":label,"headings":heading}
          p=json.dumps(kerd) 
  #  print (p)
          f.write(p)
 else :
 
  with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
          l={ "row_width":rw,"photo":None,"video":None}
          p=json.dumps(l) 
  #  print (p)
          f.write(p) 
def get_heading(id):
 path='sessions/'+str(id)+".json"
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         rd=kerd["heading"] 
         print(rd)
       #  print(rd)
         return (rd)
def get_photo(id):
 path='sessions/'+str(id)+".json"
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         r=kerd["photo"]
         return r 
def get_video(id):
 path='sessions/'+str(id)+".json"
 if os.path.exists(path):
  #print("yes")
  with open(path, 'r') as file:
         keyboard_data = file.read()
         #keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         #b=kerd["last_button"] 
         r=kerd["video"]
      #   print(r)
         return r