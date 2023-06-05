import os 
import json 
import re 
import chache1
from telebot import * 
cha="chache.json"
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#my_secret = "6294854716:AAHR19jwbCC5RtqGqBukBJY6toRojIaCAds"
#bot = telebot.TeleBot(my_secret)
def cream(row_lengt):
  global row_length2 
  row_length2=row_lengt
def btn(id,m,channel=False):
 try:
  with open ('sessions/'+str(id)+".json",'r') as f:
   data=f.read()
   sim=json.loads(data)
   row_length=sim["row_width"]
   echo=sim['title']
 #  head
 except :
   row_length =2
   echo=""
 if int(row_length)>5:
    row_length=5
 #print(row_length)
#  global sorted
 sorted=m.split()
 news=[]

 seen=set()
 #for item in sorted:
   # if item not in seen:
  #    news.append(item)
     #   seen.add(item)
 lef=[]
 #print (news)
 def srt_link(x):
#  return x.startswith("https")
  regex = r'(https?://[^\s]+)'
  links = re.findall(regex,x)
  return links
 #global get_links 
 var=[] 
 keyboard=InlineKeyboardMarkup(row_width=int(row_length))
 get_links= list(filter(srt_link,sorted)) 
 #print(len(get_links))
 lin=len(get_links)
 row = [] 
 keyboard2=InlineKeyboardMarkup(row_width=int(row_length))
 #variables = []
 row2=[]
 #for i in range(lin):
    #variables.append("variable_" + str(i + 1))
 #print (variables) 
# for i in get_links:
  # print (i)
 confirm=InlineKeyboardButton ("Post",callback_data ="channel_post") 
 #ch_=InlineKeyboardButton ("Channel Post, ")
 #rem=InlineKeyboardButton ("DONE😳 And Remove",callback_data ="con_rem")
 edy=InlineKeyboardButton (text="Edit",callback_data='edit21')
 for i, x in enumerate (get_links,start=1):
    #variables[i] = int(input("Enter the value for variable_" + str(i + 1) + ": "))
    text=f"Label {str(i)} Link:{str(x)} "
    vas= telebot.types.InlineKeyboardButton(text=f"{echo} {str(i)}", url=f"{str(x)}")
    row.append(vas )
    s=[str(i-1),f"{echo} {str(i)} ",str(x)]
    lef.append(s)
 keyboard.add (*row)
 
 #keyboard.add (edy)
# if channel==False:
   #  keyboard.add (edy) 
 #else:
 keyboard.add(edy)
 keyboard.add (confirm)
 for i, x in enumerate (get_links):
    #variables[i] = int(input("Enter the value for variable_" + str(i + 1) + ": "))
    text=f"Label {str(i)} Link:{str(x)} "
    vas= telebot.types.InlineKeyboardButton(text=text, callback_data=str(i))
    row2.append(vas)
 keyboard2.add (*row2) 
 path='sessions/'+str(id)+'.json'
 try:
  with open (path,'r') as f:
   data=f.read()
   sim=json.loads(data)
   sim['last_button']=lef
   sim['edits']=0
   jj=json.dumps(sim)
   with open (path, 'w') as f:
      f.write(jj)
 except:
  with open (path, 'w') as f:
   data=lef 
   p={
       "last_button":data,
       "row_width":row_length,
        "title":"",
         "video":None,
         "photo":None,
          "edits":0,
          "heading":"Your Links  "
   }
   l=json.dumps(p)
   f.write(l)
  # print (id)
  # l={
   #   "last_button":lef, 
    #   "row_width":int(row_length), 
     #  "title":"", 
     #  "heading":"No Heading"
  # }
  # p=json.dumps(l) 
  #  print (p)
   #f.write(p) 
  #  object=eval() 
    #print (variables) 
 #print (variable_1) 
 #variables = {}
# for i in range(lin):
   # variable_name = 'button_'+str(i) 
    #for s in get_links:
    # varia =InlineKeyboardButton (text=str(i),url=str(s))
    # keyboard.add (varia)
 #print (keyboard) 
#keyboard=InlineKeyboardMarkup(row_width=1)
# get_links= list(filter(srt_link,sorted)) 
 #print(len(get_links))
# lin=len(get_links)
# row = [] 
 return keyboard 

# variables[variable_name] = variable value
 #print (button_1)
# Print the created variables and their values
# for variable_name, variable_value in variables.items():
   # print(variable_name, "=", variable_value)
  # keyboard.add ()
#for i,x in enumerate(get_links,start=1):
   # button = telebot.types.InlineKeyboardButton(text=f"{echo} {str(i)}", url=f"{str(x)}")
    #row.append(button)
   # if len(row) == int(row_length):
    #    keyboard.add(*row)
     #   row = [] 
 
 #if row:
    #keyboard.add(*row) 
 #print (keyboard.keyboard[0])
 # print(row[1])
 #return keyboard  
#for i in range(num):
   #  var_name = "num{}".format(i+1)
 #    var_value = InlineKeyboardButton(var_name,callback_data=i)
  #   locals()[var_name] = var_value 
#def 
# Create a list of button rows by slicing the button list into groups of maximum buttons per row
 # Create a list of button rows by slicing the button list into groups of maximum buttons per row
""" button_rows = [
    [
        InlineKeyboardButton(text=str(i+1), url=str(link)) 
        for i, link in enumerate(get_links[j:j+MAX_BUTTONS_PER_ROW])
    ] 
    for j in range(0, len(get_links), MAX_BUTTONS_PER_ROW)
                      ]

 inline_keyboard = InlineKeyboardMarkup(button_rows) 
 return inline_keyboard
 #for i, link in enumerate(get_links):
   #  ""   button = InlineKeyboardButton(text=get_links, url=get_links)
       # row.append(button)
      #  if (i + 1) % 4 == 0 or i == len(get_links) - 1:
      #      keyboard.append(row)
         #   row = []
 #print (get_links) 
 #inline_keyboard=InlineKeyboardMarkup(row_width=2) 
 #for i in range(0, len(get_links), 4):
      #  row = []
      #  for j in range(i, min(i+4, len(get_links))):
            #row.append(InlineKeyboardButton(get_links[j], url=get_links[j]))
      #  inline_keyboard.row(*row)
# for i,x in enumerate(get_links,start=1):
  #anc=f"<a href={str(x)}> {str(i)}</a>"
    #button=f"InlineKeyboardButton({str(i)},url='{str(x)}')"
   # var.append(button)
 #button_data={'text':"j",'url':"t.me/devsavior"}
#button=f"InlineKeyboardButton({str(i)},url='{str(x)}')"
 #buttons =InlineKeyboardButton.from_data(button_data)
# keyboard.add(*buttons) 
# print (button) 
# print( len(button))
   # bytt=eval(button) 
  # var.append(bytt)   
   # var.append(bytt) 
# print(var) 
# my_string = ','.join(op) 
 #my_string2=eval(my_string)
# print (len(my_string)) 


# keyboard.add(my_string)
 
 # bb2=eval(anc)
   # sar.append(anc) 
 #print (sar)
  global zz 
 zz=len(var)
 li =','.join(map(str,var))
 li2=' '.join(map(str,sar))
 res = [] 
 NewList= [[x] for x in var]
 list1=[]
 list2=[]
 for x in range(zz):
  if x%2==0:
   list1.append(var[x])
  else:
   list2.append(var[x])
 global list4
 list4=[]
 length1=len(list1)
 length2=len(list2)
 if length1>=length2:
  length=length1 
 else:
  length=length2 
 try:
  for i in range(length):
   list4.append([list1[i],list2[i]]) 
 except IndexError:
   list4.append([list1[i]])
 try:
  row_length=row_length
  print (row_length)
 except NameError:
  row_length="2"
 except NameError:
   row_length=1
 if row_length =="1":
  legth=NewList 
  #bot.send_message(m.chat.id," ",reply_markup=btn(m))
 else :
  legth=list4 
 mv=InlineKeyboardMarkup(legth) 
# keyboard=InlineKeyboardMarkup()
# keyboard.add(var)
 return keyboard  
def create_inline_keyboard(links):
    keyboard = []
    row = []
    for i, link in enumerate(links):
        button = InlineKeyboardButton(text=link, url=link)
        row.append(button)
        if (i + 1) % 4 == 0 or i == len(links) - 1:
            keyboard.append(row)c
            row = []
    return InlineKeyboardMarkup """
#def html(jj):