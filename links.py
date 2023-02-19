import os 
from telebot import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup 
my_secret = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(my_secret)
#from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup 
def btn(text):
 with bot.retrieve_data(text.from_user.id,text.chat.id) as data:
     data['param']=row_length2
 #row_length="rr"

# global sorted
 sorted=text.text.split()
 def srt_link(x):
  return x.startswith("https" or "www.") 
 #global get_links
 get_links= filter(srt_link,sorted)
 #global var 
 var=[]
 for i,x in enumerate(get_links,start=1):
  by=f"InlineKeyboardButton('{str(i) }',url='{str(x)}')"
  bytt=eval(by)
  var.append(bytt)
 global zz 
 zz=len(var)
 li =','.join(map(str,var))
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
   row_length=row_length2
 #except NameError:
  # row_length=rrr
 except NameError:
   row_length=2
 if row_length ==1:
  legth=NewList
 else :
  legth=list4 
 m=InlineKeyboardMarkup(legth)
 return m