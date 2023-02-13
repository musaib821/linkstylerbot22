import os
import os
#my_secret = os.environ['BOT_TOKEN']
my_secret = os.environ['BOT_TOKEN']
import os
import telebot
import re
from pytube import YouTube
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:@%/;$()~_?\+-=\\\.&](!)?)*)', re.DOTALL)
#my_secret = "5613612d0DlRUHlGExGFpJJ_pxhvcFpS5"
bot = telebot.TeleBot(my_secret)
def check_member(id,):
 chat_id="1381749386"
 user_id=id
 ChatMember=bot. get_chat_member(chat_id="@musaibofficial",user_id=user_id) 
 if ChatMember.status=="member" :
  return True
 else :
   return False 


#@bot.message_handler(commands=[ 'start'])
#def send_welcome(message):
# bot.reply_to(message,"Hi Master") 
@bot.message_handler(commands=[ 'help','start'])
def send_help(m):
 global mt 
 mt=m.from_user.id
  
 bot.reply_to(m,text="Hello Master I Am Link Styler Bot \n Use /text To Send Me Text That Will Be Clickable \n use /link to send me Link That You Want To Style \n use /head if you want to add any text before links like a heading  \n For More Info You Can Ping My Master @ffmusaib ") 
 chat_id="1381749386"
 user_id=mt
 ChatMember=bot. get_chat_member(chat_id="@musaibofficial",user_id=user_id) 
 #if ChatMember.status=="member" :
@bot.message_handler(commands=['title']) 
   #if check_member():
def get_text1(m):
   global text1
   text_in=m.text.split()
   text_in.remove("/title")
   text1=" ".join(map(str,text_in)) 
   if len(text1)>0: 
    global text2
    text2=text1
   else:
    text2=" "
  
   if check_member(m.from_user.id):
    bot.reply_to(m,"Done "+"Text1 Set To ["+text1+"] Now Send Links")
   else :
    bot.reply_to(m, "Join Channel First @musaibofficial")
#@bot.message_handler(commands=['rg'])
#def rhh(m):
  
@bot.message_handler(commands=['rlength'])
def row(v):
 row=[InlineKeyboardButton('1', callback_data="1")], [InlineKeyboardButton('2', callback_data="2")]
 m2 =InlineKeyboardMarkup(row)
 @bot.callback_query_handler(func=lambda call: True)
 def callback_query(call):
    if call.data == "1":
     global rrr
     rrr=1 
     bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "2":
     global rr
     rr=2
    bot.answer_callback_query(call.id, "Answer is No")
   
 bot.reply_to(v,text=" tex heu susueu hesheh jeueeu sueus hseh t",reply_markup=m2)
 
@bot.message_handler(commands=['link']) 
def link(m2):
 global sorted
 sorted=m2.text.split()
 def srt_link(x):
  return x.startswith("https") 
 global get_links
 get_links= filter(srt_link,sorted)
 global var 
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
   row_length=rr 
 except NameError:
   row_length=rrr 
 except NameError:
   row_length=2
 if row_length ==1:
  legth=NewList
 else :
  legth=list4
 m =InlineKeyboardMarkup(legth,row_width=2)
 if check_member(m2.from_user.id):
   bot.reply_to(m2,text=m2.chat.id,reply_markup=m)
 else:
  bot.reply_to(m2, "Join Channel First @musaibofficial")
    

# else:
  #bot.send_message(m.chat.id, "Please Join Channel First")
@bot.message_handler(commands=['default'])
def reply_fast(m):
  bot.reply_to(m, " Invalid Command 😕😕")
   
                 
@bot.message_handler(commands=['cht'])
def checkid(msg):
 
    global chat_id 
    chat_id="1381749386"
    user_id=msg.from_user.id
    ChatMember=bot. get_chat_member(chat_id="@musaibofficial",user_id=user_id) 
    if ChatMember.status=="left" :
     bot.send_message (msg.chat.id, 'Not Joined')
    else:  
      bot.send_message(msg.chat.id,'Joined')
@bot.message_handler(content_types=['text']) 
def default(hm):
  if hm.text[0] =='/':
   bot.reply_to(hm,text="Invalid Command 😕😕")
  else :
    bot.reply_to(hm, "Text Is Not Allowed")
bot.infinity_polling()