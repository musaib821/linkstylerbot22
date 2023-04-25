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
