import os 
from telebot import *
from telebot.types import InlineKeyboardMarkup 
#my_secret = "6294854716:AAHR19jwbCC5RtqGqBukBJY6toRojIaCAds"
#bot = telebot.TeleBot(my_secret)
def cream(row_lengt):
  global row_length2 
  row_length2=row_lengt
def btn(m,row_length,echo=""): 
 if int(row_length)>=6:
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

 #print (news)
 def srt_link(x):
  return x.startswith("https")
 #global get_links 
 var=[] 
 keyboard=InlineKeyboardMarkup(row_width=int(row_length))
 get_links= list(filter(srt_link,sorted))
 row = []
 for i,x in enumerate(get_links,start=1):
    button = telebot.types.InlineKeyboardButton(text=f"{echo} {str(i)}", url=f"{str(x)}")
    row.append(button)
    if len(row) == int(row_length):
        keyboard.add(*row)
        row = []
 if row:
     keyboard.add(*row)
 return keyboard
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