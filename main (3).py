import os
from variables import *
from text import  *
import json 
did = 1070433131
#did =1351325333
developer_chat_id=1070433131
import schedule 
from telebot import types  
old_users=230
from urllib.parse import urlparse 
import re
import validators 
def load_his_setting(id):
 settings=load_settings(id)
 row_width=settings[0]
 label=settings [1]
 headings=settings [2]
 #settings=ss(id)
 channel=settings[3]
 auto_dec=settings[4]
 if channel==0:
  chn='Disabled' 
 else:
     chn='Enabled' 
 if auto_dec==0:
     atd='Allowed'
 else :
     atd='Disabled'
 text=f' Your Settings\n Row Width :{row_width}\n Label:{label}\n Headings:{headings} \n Add Channel Link :{chn} \n Numbering :{atd}'
 return text
def validate(m):
 s=validators.url(m)
 
 #print (s)
 return s 
def check_sub():
 kk=InlineKeyboardMarkup()
 btn=InlineKeyboardButton('Check ', callback_data='check_subscriber')
 btn2=InlineKeyboardButton('Close', callback_data='Close_msg')
 kk.add(btn,btn2)
 return kk

def contains_url(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return bool(re.search(url_pattern, text))

button1 = types.InlineKeyboardButton(1)
button2 = types.InlineKeyboardButton(2)
button3 = types.InlineKeyboardButton(3)
button4 = types.InlineKeyboardButton(4)
button5 = types.InlineKeyboardButton(5)
button2 = types.InlineKeyboardButton(2) 
# Create the inline keyboard markup
markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
markup.row(button1, button2,button3)
markup.row(button4,button5)# 
spp=[] 
av_offer='No offers available right now.Please stay tuned'
pro_set=buy_pro_df
#job()

import time 
from chache1 import *
from telebot import * 
#chedule.every(1).minutes.do(job)
def run_pending_jobs():
 while True:
    schedule.run_pending()
    time.sleep(1)
#from load_data import*  
from telebot import apihelper 
#os.remove("5510280828.json")
#print (get_users())  
#
from datetime import datetime, timedelta 
from buttons import *
import datetime
#import pytz 
from database import * 
#auto_remove()
import threading
thread = threading.Thread(target=run_pending_jobs)
thread.start()
VERSION="4.0.2" 
L_DATE="24-03-2023" 
#job()
#get_user_ids()
tz = pytz.timezone('Asia/Kolkata')
def likk():
    keyboard=InlineKeyboardMarkup()
    btn=InlineKeyboardButton('🌹',callback_data='lok')
    keyboard.add(btn)
    return (keyboard )
#auto_remove()
def clks(text):
    words = text.split()
    for word in words:
        parsed_url = urlparse(word)
        if parsed_url.scheme and parsed_url.netloc:
            return True
    
    return False
def channel_btn_to_remove(id):
 channels=fetch_channel(id)
 keyboard=InlineKeyboardMarkup () 
 row=[]
 here=InlineKeyboardButton("cancel ", callback_data="Close_msg")
 for channel in channels :
  name=bot.get_chat(channel).title
  btn=InlineKeyboardButton (text=name,callback_data="remove_channel"+str(channel))
  row.append(btn) 
 keyboard.add (*row)
 keyboard.add(here)
 return keyboard 
def channel_btn(id):
 channels=fetch_channel(id)
 keyboard=InlineKeyboardMarkup () 
 row=[]
 here=InlineKeyboardButton("Post Here ", callback_data="poster"+str(id))
 for channel in channels :
  name=bot.get_chat(channel).title
  btn=InlineKeyboardButton (text=name,callback_data="poster"+str(channel))
  row.append(btn) 
 keyboard.add (*row)
 keyboard.add(here)
 
 return keyboard 
# print (s) 
U_DATE=str(datetime.datetime.now().date()) 
#print (date)  
faqs="t.me/devsavior"
requests=[]
filename = "new.json"
with open("channel.json",'w') as f:
 f.write(" ")
#regexp=
 # r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
#print (l)
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup 
from telebot.types import *
from links import *
from telebot import custom_filters
#my_secret = os.environ['BOT_TOKEN']
my_secret = "5953623379:AAEjIaN6UsCxtCg0BmmReNWchPwKLtBEOAE"
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage 
state_storage = StateMemoryStorage()
dict = {} 


    
class MyStates4(StatesGroup):
  title = State()
  user_id = State()
  after_proof=State()
  cancel_proof=State()
  row_width = State()
  headings = State()
  links = State()
  id=State()
  st_edit_link=State()
  st_edit_label=State()
  edit_label=State()
  edit_link=State()
  edit_btn=State()
  new=State()
  st_rw=State()
  st_hd=State()
  st_rw1=State()
  st_hd1=State() 
  support=State()
  done=State()
  proof=State()
  set_def_label=State()
  set_def_row_width=State()
  set_def_headings=State ()
  ccc=State()
bot = telebot.TeleBot(my_secret, state_storage=state_storage) 
def notify_before_3days():
 users=notify_users_3()
 if  users==None or len(users)==0:
     pass
 else :
  for user in users: 
   try :
    bot.send_message(user,"Your Premium Is Expiring In 3 days \n Buy Now and Get extra 3 days")
   except:
       pass
def notify_before_r():
 users=auto_remove()
 if  users==None or len(users)==0 :
     pass
 else :
  for user in users:
   bot.send_message(user,"Your Premium Is Expired \n buys now and get 1 day extra " )
#print (bot)
def job():
    notify_before_3days()
    notify_before_r()
  #  print("Running scheduled task...")

schedule.every().day.at("00:00").do(job)
def sub_check(id):
    not_found = False

    try:
     join = bot.get_chat_member(-1001381749386, id)
    except Exception as e:
     if 'user not found' in str(e): not_found = True    

    if (join.status == "kicked") or (join.status == "left") or not_found == True:
      return False
    else: 
       return True
def send_db():
  #  if m.from_user.id == 1070433131:
 with open('database.db', 'rb') as file:
  bot.send_document(document=file, chat_id=did)
 #bot.send_file(did,)
#send_db()
#@bot.message_handler(com)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
 if call.data=='need_help_1':
   bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=tutorial, reply_markup=back_to_first()) 
 elif call.data=='check_subscriber':
  if sub_check(call.from_user.id)==False:
    bot.answer_callback_query(call.id,"Please Join Channel First ",show_alert=True)
  #  bot.edit_message_text(chat_id=call.from_user.id,message_id=call.message.message_id,text= 'This feature is only available for subscribers \n join <a href="t.me/musaibofficial" >channel </a> to use this featurhe ',reply_markup=check_sub(),parse_mode='html')
  else: 
    
    bot.delete_message(chat_id=call.from_user.id,message_id=call.message.message_id)
    bot.answer_callback_query(call.id,"Now You Can use settings ") 
    # print("User is present in group/channel ✅")  
 elif call.data.startswith('channellink_'):
   if call.data=='channellink_0':
    a_c_l(call.from_user.id) 
   else:
    d_c_l(call.from_user.id)
   check_for_autodec(call.from_user.id)
# print(m)
  # settings=load_settings(call.from_user.id)
   #row_width=settings[0]
   #label=settings [1]
  # headings=settings [2]
   #text=f' Your Settings\n Row Width :{row_width}\n Label:{label}\n Headings:{headings}'
   bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=load_his_setting(call.from_user.id),reply_markup=give_settings(call.from_user.id))


  # bot.send_message(call.from_user.id,)
 elif call.data.startswith('autodec_'):
  if call.data=='autodec_1':
      a_auto_dec(call.from_user.id) 
  else:
    d_auto_dec(call.from_user.id)
  check_for_autodec(call.from_user.id)
# print(m)
  #settings=load_settings(call.from_user.id)
  #=settings[0]
  #label=settings [1]
 # headings=settings [2]
  #text=f' Your Settings\n Row Width :{row_width}\n Label:{label}\n Headings:{headings}'
  bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=load_his_setting(call.from_user.id),reply_markup=give_settings(call.from_user.id))

 elif call.data=='channel_link':
  pass
 elif call.data=='Close_msg':
    bot.delete_message(call.from_user.id,call.message.message_id)

 elif call.data=='set_label':
     bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
     bot.send_message(call.from_user.id,"Set Label")
     bot.set_state(call.from_user.id, MyStates4.set_def_label, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
     with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['set_def_label'] = 'get_data'
 elif call.data=='set_row_width':
     bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
     bot.send_message(call.from_user.id,"Row Width")
     bot.set_state(call.from_user.id, MyStates4.set_def_row_width, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
     with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['set_def_row_width'] = 'set_row_width' 
 elif call.data=='set_heading':
     bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
     bot.send_message(call.from_user.id,"Row Width")
     bot.set_state(call.from_user.id, MyStates4.set_def_headings, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
     with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['set_def_headings'] = 'set_headings'
 elif call.data=='back_to_first':
   user=telebot.util.user_link(call.from_user) 
   s=starting_message.format(user)  
   bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=s,reply_markup=first_markup(),parse_mode='Html')  
 elif call.data=='others':
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=others_text,reply_markup=others1(),parse_mode='Html')  
 elif call.data=='about':
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=about.format(L_DATE,U_DATE,old_users+get_user_ids(True),VERSION, faqs),reply_markup=back_to_others(),parse_mode='Html',disable_web_page_preview=True)  
 elif call.data=='back_to_others':
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=others_text,reply_markup=others1(),parse_mode='Html')  
# elif call.data=='feedback':
 elif call.data=='faqs':
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=faq,reply_markup=faq_btn(),parse_mode='Html')  
 elif call.data=='back_to_faq':
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=faq,reply_markup=faq_btn(),parse_mode='Html')  
     
 elif call.data.startswith("remove_channel"):
   ch=call.data[14:]
 #  print(ch)
   remove_channel(call.from_user.id,ch)
   bot.answer_callback_query(call.id,"DELETED CHANNEL")
   bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,reply_markup=channel_btn_to_remove(call.from_user.id))
 elif call.data =='to_title_pro':
     bot.set_state(call.from_user.id, MyStates4.user_id, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
     with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['user_id'] = call.message.from_user.id
     # print (data['id'])
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=next_2, reply_markup=get_title_pro())
 elif call.data.startswith('faq_page'):
     page=call.data[9]
     s="faq_"+str(page)
     #print(s)
     ttt=faqyys[s]
    # print (ttt)
    # faq_
     bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,text=ttt,reply_markup=faq_back(),parse_mode='Html')
 elif call.data =='to_headings_pro':
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=next_2, reply_markup=get_headings_pro())
 elif call.data.startswith("edit"):
     try:
         bot.edit_message_text (message_id =call.message.message_id, chat_id =call.from_user.id,text=get_heading(call.from_user.id),reply_markup =to_edit(call.from_user.id ))
     except:
         bot.edit_message_caption (message_id =call.message.message_id, chat_id =call.from_user.id,caption=get_heading(call.from_user.id),reply_markup =to_edit(call.from_user.id ))
   #  except:
   #  bot.edit_message_reply_markup (message_id =call.message.message_id, chat_id =call.from_user.id, reply_markup =to_edit(call.from_user.id ))
 elif call.data.startswith("ssr"):
     try:
      bot.edit_message_text(message_id=call.message.message_id,chat_id =call.from_user.id, text=send_to_edit (call.from_user.id, call.data ),reply_markup =send_btn_to_edit(call.from_user.id, call.data),disable_web_page_preview=True)
     except:
      bot.edit_message_caption (message_id =call.message.message_id,caption=send_to_edit(call.from_user.id,call.data), chat_id =call.from_user.id, reply_markup =send_btn_to_edit(call.from_user.id,call.data))
 elif call.data=="confirm":
     try:
         bot.edit_message_text (message_id =call.message.message_id, chat_id =call.from_user.id,text=get_heading(call.from_user.id),reply_markup =gen_new_markup(call.from_user.id ))
     except:
         bot.edit_message_caption (message_id =call.message.message_id, chat_id =call.from_user.id,caption=get_heading(call.from_user.id),reply_markup =gen_new_markup(call.from_user.id ))
    # except:
 elif call.data=="back_to_confirm":
     try:
         bot.edit_message_text (message_id =call.message.message_id, chat_id =call.from_user.id,text=get_heading(call.from_user.id),reply_markup =gen_new_markup(call.from_user.id ))
     except:
         bot.edit_message_caption (message_id =call.message.message_id, chat_id =call.from_user.id,caption=get_heading(call.from_user.id),reply_markup =gen_new_markup(call.from_user.id ))
    # except:
   #  bot.edit_message_reply_markup (message_id =call.message.message_id, chat_id =call.from_user.id,reply_markup =gen_new_markup(call.from_user.id ))
 elif call.data =="confirm_data":
   try:
      bot.edit_message_text (message_id =call.message.message_id,text=get_heading(call.from_user.id), chat_id =call.from_user.id, reply_markup =confirmed_btn(call.from_user.id ))
   except :
    bot.edit_message_caption(message_id =call.message.message_id,caption=get_heading(call.from_user.id), chat_id =call.from_user.id, reply_markup =confirmed_btn(call.from_user.id ))
      # bot.edit_message_caption()
 elif call.data =="channel_post":
    try:
        bot.edit_message_text (message_id =call.message.message_id,text=topi, chat_id =call.from_user.id, reply_markup =channel_btn(call.from_user.id )) 
    except :
        bot.edit_message_caption (message_id =call.message.message_id,caption=topi, chat_id =call.from_user.id, reply_markup =channel_btn(call.from_user.id )) 
   # except TypeError:
        
     #   bot.answer_callback_query (call.id,"You Don't Have Any Added Channels Yet")
 elif call.data =="con_rem":
    # try: 
      bot.send_message (chat_id =call.from_user.id ,photo="",text=get_heading(call.from_user.id) , reply_markup =confirmed_btn(call.from_user.id,post=True ))
 elif call.data.startswith ("poster") :
 #else: 
   id=int(call.data[6:]) 
  # print(type(id ))
  # print('owner')
  # print(type(call.from_user.id))
 #  print(id==call.from_user.id)
   chat = bot.get_chat(id)
   title=chat.title
   btns=confirmed_btn(call.from_user.id,post=True)
   if check_for_channel_link(call.from_user.id) and id!=int(call.from_user.id):
    btns.add(InlineKeyboardButton(title,url=chat.invite_link))

#print('@'+chat.username, chat.invite_link)
   try :
     s=get_photo(call.from_user.id)
   #  print(s)
     #print(int(call.data[6:]))
     if get_video(call.from_user.id)!=None:
      #   bot.send_video()
      bot.send_video (chat_id =int(call.data[6:]),caption=get_heading(call.from_user.id) , reply_markup =confirmed_btn(call.from_user.id,post=True ),video=get_video(call.from_user.id))
     elif get_photo(call.from_user.id)!=None:
      #   bot.send_video()
      bot.send_photo (chat_id =int(call.data[6:]),caption=get_heading(call.from_user.id) , reply_markup =confirmed_btn(call.from_user.id,post=True ),photo=get_photo(call.from_user.id))
     else:
      bot.send_message (chat_id =int(call.data[6:]),text=get_heading(call.from_user.id) , reply_markup =btns)
    # os.remove(str(call.from_user.id)+".json")
     bot.answer_callback_query (call.id,text="Posted To Channel") 
     #try:
     bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
   except apihelper.ApiTelegramException as e:
    # Check if the error code is 400
    if e.error_code == 400:
     error_message = f"Bad Request: {e.description}"
     bot.send_message(call.from_user.id,"Bot Is Not Able To Post In Channel Check Bot Rights Please")   
     #os.remove(str(call.from_user.id)+".json")
 elif call.data=="ed_row_width":
   #  if call.data.startswith("cust_link"):
     
      bot.send_message(call.message.chat.id,"Send Me Row Width ",reply_markup=markup)
      bot.set_state(call.from_user.id, MyStates4.st_rw, call.from_user.id)
      bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
     # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
      with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
       data['st_rw'] = call.data 
 elif call.data=="ed_heading":
   #  if call.data.startswith("cust_link"):
     
      bot.send_message(call.message.chat.id,"Send Me  Heading ")
      bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
     # https://sbface.com/dl?1
      bot.set_state(call.from_user.id, MyStates4.st_hd, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
      with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
       data['st_hd'] = call.data 
 #elif call.data=="free_trail":
  
 elif call.data.startswith("cust_"):
     if call.data.startswith("cust_link"):
     
      bot.send_message(call.message.chat.id,"Send Me A new Link ")
      bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
      bot.set_state(call.from_user.id, MyStates4.st_edit_link, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
      with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
       data['st_edit_link'] = call.data
      #Sbot.set_state(call.from_user.id, MyStates4.st_edit_user, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
   #   with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
     #  data['st_edit_link'] = str(call.message.from_user.id) +call.data
     else:
      bot.send_message (call.message.chat.id, "send me a new label ")
      bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
      bot.set_state(call.from_user.id, MyStates4.st_edit_label, call.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
      with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
       data['st_edit_label'] = call.data 
 elif call.data=='lok':
   #  print (call.message.json.reply_markup)
     #print(call.message.entities)
     bot.reply_to(call.message,call.message.json.reply_markup)
     #bot.reply_to(call.message,call.message)
    # print (call.message.reply_markup.keyboard)
 elif call.data=='close_support_chat':
  bot.answer_callback_query(call.id,"Report Send Successfully")
  bot.delete_state(call.from_user.id, call.from_user.id)
  bot.delete_message(message_id=call.message.message_id,chat_id=call.from_user.id)
 elif call.data=='free_trail': 
    print (check_for_trail(call.from_user.id))
    if check_for_trail(call.from_user.id)==False:
      bot.send_message(chat_id=did,text="New Request "+telebot.util.user_link(call.from_user)+"\n ID:<code>"+str(call.from_user.id)+"</code>",parse_mode='Html') 
      bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,text="Request To Free Trail Was Successful ✅ \n Please wait For Confirmation")
    else :
     bot.answer_callback_query(call.id,"You Have Already Availed Free trail")
@bot.message_handler(commands=['restart'])
def restart_user(m):
 if m.from_user.id==did:
  user=m.text.split()[1]
  bot.delete_state(user,user)
  bot.send_message(m.chat.id,'Restarted')
@bot.message_handler(commands=['cancel'])
def cancelprocess(m):
    bot.reply_to(m,"cancelled process ")
    return 
@bot.message_handler(commands=["settings"])
def set_settings(m):
 #Check if a user is present in a group/channel 👉🏻
 
# if (join.status == "kicked") or (join.status == "left") or not_found == True:
  #  print("User not in group/channel ❌") 
 print(sub_check(m.from_user.id))
 if sub_check(m.from_user.id)==False:

    bot.send_message(m.chat.id,'This feature is only available for subscribers \n join <a href="t.me/musaibofficial" >channel </a> to use this feature ',reply_markup=check_sub(),parse_mode='html')
    return 
 check_for_autodec(m.from_user.id)
# print(m)
 bot.send_message(m.chat.id,text=load_his_setting(m.from_user.id),reply_markup=give_settings(m.from_user.id))

@bot.message_handler(state=MyStates4.set_def_row_width)
def get_rw_db(m):
 if m.text: 
  rw=['1','2','3','4','5']
  if m.text in rw :
   
   add_row_width_db(m.from_user.id,m.text)
  # bot.reply_to(m,"Done")
 #  bot.send_message
 #  print('Not_yet')
   bot.send_message(m.chat.id,text=load_his_setting(m.from_user.id),reply_markup=give_settings(m.from_user.id))
  # print('Done')
   bot.set_state(m.from_user.id, MyStates4.ccc, m.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
   with bot.retrieve_data(m.from_user.id, m.from_user.id) as data:
      data['ccc'] = m.from_user.id 
  else:
      s=bot.reply_to(m,"Send a number between 1-5") 
      bot.register_next_step_handler(s,get_rw_db)
@bot.message_handler(state=MyStates4.set_def_label)
def get_label(m):
 if m.text:
  add_label_db(m.from_user.id,m.text)
 # bot.reply_to(m,"Done")
  bot.send_message(m.chat.id,text=load_his_setting(m.from_user.id),reply_markup=give_settings(m.from_user.id))

  bot.set_state(m.from_user.id, MyStates4.ccc, m.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
  with bot.retrieve_data(m.from_user.id, m.from_user.id) as data:
      data['ccc'] = m.from_user.id
@bot.message_handler(state=MyStates4.set_def_headings)
def get_heq(m):
 if m.text:
  add_heading_db(m.from_user.id,m.text)
 # bot.reply_to(m,"Done")
  bot.send_message(m.chat.id,text=load_his_setting(m.from_user.id),reply_markup=give_settings(m.from_user.id))

  bot.set_state(m.from_user.id, MyStates4.ccc, m.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
  with bot.retrieve_data(m.from_user.id, m.from_user.id) as data:
      data['ccc'] = m.from_user.id

@bot.message_handler(commands=['get_user_info'])
def gju(m):
 if m.from_user.id==did:
     id=m.text.split()[1]
     tex=fetch_user_details(id)
    # print(tex)
     #i₹f tex
    #print(tex)
     ch=tex[3]
     #print(tex)
    # print(ac) 
     s=bot.get_chat(id)
     print(s)


     user=telebot.types.User(id=id,first_name=bot.get_chat(id).first_name,is_bot=False)   
     user=telebot.util.user_link(user)
    # print(user)
     if ch==0:
      ch=0
        
     text=ac.format(user,tex[0],tex[1],tex[2],ch)
   #  print(text)
     bot.reply_to(m,text,parse_mode='html')
@bot.message_handler(state=MyStates4.st_rw)
def get_rw(m):
 rows=['1','2','3','4','5'] 
 if m.text=="/cancel":
  bot.reply_to(m,"Process Cancelled ")
  return 
 if m.text in rows:
       
 # bot.reply_to(m,"Trying to change row wodth")
  add_row_width(m.from_user.id,m.text)
  s=bot.reply_to(m,"Trying to change row wodth",reply_markup=ReplyKeyboardRemove())
  bot.delete_message(m.chat.id,s.id)
     # else:
    #if m.text in ['1','2','3']:
     #bot.reply_to(m,"Trying to change row wodth")
  #  add_row_width(m.from_user.id,m.text) 
  if get_video(m.from_user.id)!=None:
      # print (s)
       bot.send_video(m.chat.id,video=get_video(m.from_user.id),caption=get_heading(m.from_user.id),reply_markup=to_edit(m.from_user.id))  
  elif get_photo(m.from_user.id)!=None:
     bot.send_photo(m.chat.id,photo=get_photo(m.from_user.id),caption=get_heading(m.from_user.id),reply_markup=to_edit(m.from_user.id))  
  else :
       bot.send_message(chat_id=m.from_user.id,text=get_heading(m.from_user.id),reply_markup=to_edit(m.from_user.id))
 # break 
 else :
    s=bot.reply_to(m,"Not Possible ")
    bot.register_next_step_handler(s,get_rw) 
 bot.set_state(m.from_user.id, MyStates4.st_rw1, m.chat.id)
 with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
    data['st_rw1'] = m.text  
@bot.message_handler(commands=['commands'])
def reply_com(m):
 bot.send_message(m.chat.id, commands,reply_markup=close_msg() )

@bot.message_handler(state=MyStates4.st_hd)
def get_hd(m):
# rows=['1','2','3','4','5']
 if m.text:
  if m.text=='/cancel':
   bot.reply_to(m,'Process Cancelled ')
   return 
  bot.reply_to(m,"Trying to change Heading")
  add_heading(m.from_user.id,m.text) 
  if get_video(m.from_user.id)!=None:
      # print (s)
       bot.send_video(m.chat.id,video=get_video(m.from_user.id),caption=get_heading(m.from_user.id),reply_markup=to_edit(m.from_user.id))  
  elif get_photo(m.from_user.id)!=None:
     bot.send_photo(m.chat.id,photo=get_photo(m.from_user.id),caption=get_heading(m.from_user.id),reply_markup=to_edit(m.from_user.id))  
  else :
       bot.send_message(chat_id=m.from_user.id,text=get_heading(m.from_user.id),reply_markup=to_edit(m.from_user.id))
 # break 
 #else :
   # s=bot.reply_to(m,"Not Possible ")
   # bot.register_next_step_handler(s,get_rw) 
  bot.set_state(m.from_user.id, MyStates4.st_hd1, m.chat.id)
  with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
    data['st_hd1'] = m.text  
@bot.message_handler(state=MyStates4.user_id)
def name_get(message):
  bot.reply_to(message, "Title Added")
 
  bot.set_state(message.from_user.id, MyStates4.title, message.chat.id)
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    data['title'] = message.text 
@bot.message_handler(state=MyStates4.st_edit_link)
def get_new_link(message):
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
   data=data['st_edit_link']
  #import re 
   
 #  if validate (message.text):
    
  #print(contains_url(message.text))
   # url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
   # return bool(re.search(url_pattern, text))

  if validate(message.text)==True:
   p=edit_btn_link(message.from_user.id,data,message.text,check_for_pre(message.from_user.id))
   text=get_btn_text(message.from_user.id, data)
   if get_video(message.from_user.id)!=None:
    #   print (s)
       bot.send_video(message.chat.id,video=get_video(message.from_user.id),caption=text,reply_markup=p)  
   elif get_photo(message.from_user.id)!=None:
    bot.send_photo(message.chat.id,photo=get_photo(message.from_user.id),caption=text,reply_markup=p)  
   else: 
    bot.send_message (message.chat.id, text=text,reply_markup=p,disable_web_page_preview=True)
 # bot.send_message (message.chat.id, text=text,reply_markup=p) 
   bot.set_state(message.from_user.id, MyStates4.new, message.chat.id)
   with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    data['new'] = "ok"
  else :
   s= bot.reply_to(message,"This Is Not A Valid Link Please Send A New Link")
   bot.register_next_step_handler(s,get_new_link)
@bot.message_handler(state=MyStates4.st_edit_label)
def name_get(message):
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
   data=data['st_edit_label']
  #print (message.text) 
    
  s=bot.reply_to(message, "Trying To Change Label")
  #print (data)
  p=edit_btn_label(message.from_user.id,data,message.text,check_for_pre(message.from_user.id))
  text=get_btn_text(message.from_user.id, data) 

  if get_video(message.from_user.id)!=None:
    #   print (s)
       bot.send_video(message.chat.id,video=get_video(message.from_user.id),caption=text,reply_markup=p)  
  elif get_photo(message.from_user.id)!=None:
    bot.send_photo(message.chat.id,photo=get_photo(message.from_user.id),caption=text,reply_markup=p)  
  else: 
   bot.send_message (message.chat.id, text=text,reply_markup=p,disable_web_page_preview=True) 
  bot.set_state(message.from_user.id, MyStates4.new, message.chat.id)
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
   data['new'] = "ok"

@bot.message_handler(commands=['create_buttons'])
#def ss(m) :
 #set=[0,1,2,3,4]
def st(m):
    #print(m) 
    s=bot.reply_to (m, "Send Any Video or Photo else /skip or /cancel ")
    bot.register_next_step_handler(s,attach_file)
 #s=bot.reply_to()
def attach_file(m):
# print(m) 
 if m.text=="/cancel": 
   bot.reply_to(m,"Process Cancelled")
   return 
 elif m.text=="/skip":
   p=bot.reply_to(m,"Set Row Width Now \n 1-3 -Free plan \n 1-5 For Premium Plan \n /skip or /cancel",reply_markup=markup)
   add_photo(m.from_user.id)
   bot.register_next_step_handler (p,process_row_width)
  # add_f(m.from_user.id)
 elif m.content_type=="photo":
   fd= m.json['photo'][0]['file_id']
   add_photo(m.from_user.id,fd) 
   file=bot.get_file(fd)
  # print(file)
   s=bot.reply_to(m, " Set Row Width 1-3 For Free Plan \n 1-5 For Premium \n use /skip or /cancel",reply_markup=markup)
   bot.register_next_step_handler (s,process_row_width)
 elif m.content_type=="video":
   #fd= m.json['photo'][0]['file_id']
   #  print(m) 
     fd=m.video.file_id
     s=bot.reply_to(m,"Attached Video \n Set Row Width 1-3 For Free Plan \n 1-5 For Premium \n use /skip To Set Default Value \n /cancel To Cancel Process",reply_markup=markup)
     
     add_video(m.from_user.id,fd)
     bot.register_next_step_handler (s,process_row_width)
 else:
     v=bot.reply_to(m,"Please Send Video or photo \n /skip or /cancel ")
     bot.register_next_step_handler (v,attach_file)
def process_row_width(m):
  if m.text=="/cancel": 
   bot.reply_to(m,"Process Cancelled")
   return 
  if m.text=="/skip":
   p=bot.reply_to(m,"Set label on links \n /skip or /cancel",reply_markup=ReplyKeyboardRemove())
   bot.register_next_step_handler (p,process_title)
   add_row_width(m.from_user.id,2)
   print ("Row width ")
  else:
   try:
    row_width=int(m.text.split()[0])
    #print(check_pro(m.from_user.id))
    if check_for_pre(m.from_user.id):
     row_width=row_width
    else :
     if row_width>3:
      row_width=2
     #else :
    # row_width=row_width
    s=bot.send_message(m.chat.id,f"Alright! Set The Label On The Links \n /skip or /cancel",reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(s, process_title)
    add_row_width(m.from_user.id,row_width)
   except ValueError:
    s=bot.reply_to (m,"Please Enter a valid number (1 to 5)")
    bot.register_next_step_handler(s, process_row_width)
   except IndexError:
    s=bot.reply_to (m,"Please Use Numerical Value  ")
    bot.register_next_step_handler(s, process_row_width)
   except :
    s=bot.reply_to(m,"Send A Number Please ")
    bot.register_next_step_handler(s, process_row_width)
def process_title(m) : 
  telebot.types.ReplyKeyboardRemove()
  if m.text=="/cancel": 
   bot.reply_to(m,"Process Cancelled")
   return 
  if m.text=="/skip":
  # p=bot.reply_to(m,"OK Skipped This Step \n Set Headings ")
  # bot.register_next_step_handler (p,process_headings)
   add_title(m.from_user.id)
 #if m.text=="/skip":
  #p=bot.reply_to(m,"OK Skipped This Step ")
 # bot.register_next_step_handler (p,process_heading)
  try:
   title =m.text 
   if m.text=="/skip":
    title=None
   s= bot.reply_to(m,' Now Send Headings Else /skip or /cancel' )
   bot.register_next_step_handler(s, process_headings)
  # s= bot.reply_to(m,f'Title Set To {title} \n Now Send Headings Else /skip' )
  #bot.register_next_step_handler(s, process_headings) 
   if title!=None:
       
    add_title(m.from_user.id,title) 
  except :
   bot.reply_to (m, "No Title Added ")
   bot.register_next_step_handler(s, process_title)
def process_headings(m) :
  if m.text=="/cancel": 
   bot.reply_to(m,"Process Cancelled")
   return 
  if m.text=="/skip":
   #bot.register_next_step_handler (p,process_t)
   heading="Your Links"
  # add_heading(m.from_user.id,"Your Links") 
  else:
  #try:
   heading =m.text
  v=bot.reply_to(m,f'Now Send Links' )
  add_heading(m.from_user.id,heading)
  bot.register_next_step_handler(v,get_links)
def get_links(m):
   s=get_video(m.from_user.id)
   if get_video(m.from_user.id)!=None:
       print (s)
       bot.send_video(m.chat.id,video=get_video(m.from_user.id),caption=get_heading(m.from_user.id),reply_markup=btn(m.from_user.id,m.text,ins=False,sub=sub_check(m.from_user.id)))  
   elif get_photo(m.from_user.id)!=None:
     bot.send_photo(m.chat.id,photo=get_photo(m.from_user.id),caption=get_heading(m.from_user.id),reply_markup=btn(m.from_user.id,m.text,ins=False,sub=sub_check(m.from_user.id)))  
   else :
       bot.send_message(chat_id=m.from_user.id,text=get_heading(m.from_user.id),reply_markup=btn(m.from_user.id,m.text,ins=False,sub=sub_check(m.from_user.id)))
@bot.message_handler(commands=['premium'])
def pju(m):
    bot.send_message(m.chat.id,pro_set,parse_mode='html', disable_web_page_preview=True)
@bot.message_handler(commands=['broadcast'])
def post_user(m):
 if m.from_user.id==did:
#  user=m.text.split()[1]
 # print(m.text.split())
  text=m.text[10:]
 # text= ' '.join(text)
  users=get_user_ids()
  for user in users :
   try:
    bot.send_message(user,text)
   except :
       pass
@bot.message_handler(commands=['send_me_db'])
def post_user(m):
 if m.from_user.id==did:
 # user=m.text.split()[1]
    send_db()
@bot.message_handler(commands=['post_user'])
def post_user(m):
 if m.from_user.id==did:
  user=m.text.split()[1]
  print(m.text.split())
  text=m.text.split()[2:]
  text= ' '.join(text)
 # print(text)
 # s=bot.reply_to(m,"Send Text to Post To Usrrr")
#  bot.register_next_step_handler=(s,get_text_message)
  bot.send_message(user,text)
@bot.message_handler(commands=['dec_premium'])
def addguui(m):
 if m.from_user.id==did:
  id =m.text.split()[1]
  days=m.text.split()[2]
 # plan=m.text.split()[3]
  dec_pro(id,days)
  bot.reply_to(m,"Premium Decreased")
@bot.message_handler(commands=['add_premium'])
def addguui(m):
 if m.from_user.id==did:
  id =m.text.split()[1]
  days=m.text.split()[2]
 # plan=m.text.split()[3]
  add_pro(id,days)
  bot.reply_to(m,"Premium Added")
@bot.message_handler(commands=['free_trail'])
def addgi(m):
 if m.from_user.id==did:
  id =m.text.split()[1]
  days=m.text.split()[2]
  #plan=m.text.split()[3]
  add_pro(id,days,True)
  bot.reply_to(m,"Premium Added")
@bot.message_handler(commands=['set_premium'])
def addgi(m):
 if m.from_user.id==did:
 # id =m.text.split()[1]
  text=m.text[12:]
  global pro_set
  pro_set=text 
  bot.reply_to(m,"Premium Page Updated")
@bot.message_handler(commands=['set_users'])
def addgi(m):
 if m.from_user.id==did:
 # id =m.text.split()[1]
  text=int(m.text.split()[1])
  global old_users
  old_users=text
  #plan=m.text.split()[3]
  #add_pro(id,days,True)
  bot.reply_to(m,"Premium Details Updated")
@bot.message_handler (commands =['add_channel'])
def get_channel(m):
 if check_for_pre(m.from_user.id)==False and fetch_channel(m.from_user.id,check=True)==2:
    
    bot.send_message(m.chat.id,"You Already Have 2 Channels Added \n But Premium To Add more Channels")
    return 
 if len(fetch_channel(m.from_user.id))==5:
    bot.send_message(m.chat.id,"Already 5 Channels Added")
    return 
 adc=InlineKeyboardMarkup ()
 adc.add(InlineKeyboardButton ("Add Bot To Channel",url="http://t.me/buttonizebot?startchannel=start"))
 s=bot.reply_to(m, "Please Add Bot To Channel And Forward any message from channel",reply_markup=adc)
 bot.register_next_step_handler(s,check_edit) 
def check_edit(m):
 if m.text =='/cancel': 
  bot.reply_to(m,'Process Cancelled ')
  return 
 #print (m)
 if m.forward_from_chat==None:
  s=bot.reply_to (m,"Please Forward Message From Channel ")
  bot.register_next_step_handler(s,check_edit)
 else:
  p= m.forward_from_chat.type=="channel"
  id= m.forward_from_chat.id 
#  s=bot.get_chat(id)
 # print(s)
  #print(m.forward_from_chat)
 #print (p) 
  #try :
  if p==True: 
   try:
    name=bot.get_chat(id).title
    bot.reply_to (m,name+' added')
   #print(m.forward_from_chat) 
    add_channel(m.from_user.id,m.forward_from_chat.id)
   except:
       bot.reply_to(m,"Make Sure Bot Is Added To Channel as admin with post messages rights")
  else:
    s=bot.reply_to (m, "only channels are allowed to be added")
    bot.register_next_step_handler(s,check_edit)
@bot.message_handler(commands=['start'])
def start(m):
 user=telebot.util.user_link(m.from_user) 
 s=starting_message.format(user)
 add_user(m.from_user.id)
 #if check_pro(m.from_user.id):
 bot.send_message(m.chat.id,text=s,reply_markup=first_markup(),parse_mode='Html')
@bot.message_handler(state=MyStates4.support)
def gju(m):
  bot.forward_message(from_chat_id=m.chat.id,chat_id=did, message_id=m.id)
@bot.message_handler(func=lambda message: message.text.startswith('/support'))
def user_message(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Save the user's chat ID to allow communication
    bot.send_message(developer_chat_id, f"New support request from {telebot.util.user_link(message.from_user)}",parse_mode='Html')
     
    # Send a response to the user
    s= bot.send_message(chat_id, "You are in interaction with Developer \n please report your problem ",reply_markup=close_chat())
    bot.set_state(message.from_user.id, MyStates4.support, message.from_user.id)
    # bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
    with bot.retrieve_data(message.from_user.id, message.from_user.id) as data:
       data['support'] =True 
@bot.message_handler(commands=['account'])
def close(m):
    # Get the user's chat ID
   # check_pre(m.from_user.id)
  #  chat_id = message.chat.id
  #  remove_channel(m.from_user.id)
    tex=fetch_user_details(m.from_user.id)
    print(tex)
    ch=tex[3]
    
    if ch==0:
     ch=[0]
    user=telebot.util.user_link(m.from_user)
    text=ac.format(user,tex[0],tex[1],tex[2],tex[3])
  #  s=
    # Check if the chat is associated with a support request
   # if chat_id == developer_chat_id:
        # Respond to the developer indicating the chat is closed
    bot.send_message(m.chat.id,text,reply_markup=get_free_trail(),parse_mode="Html")
@bot.message_handler(func=lambda message: message.from_user.id == did and message.reply_to_message)
def user_message(m):
    # Your code here

  #  print("Working ")
    if m.chat.id==did:
     try: 
        bot.send_message (m.reply_to_message.forward_from.id,m.text)
     except:
      pass
@bot.message_handler(commands=['remove_channel'])
def close(m):
  #  check_pre(m.from_user.id)
    bot.send_message(m.chat.id,"Select channel to remove \n Channel will be instantly removed ",reply_markup=channel_btn_to_remove(m.from_user.id))
@bot.message_handler(commands=['set_offers'])
def set_offer(m):
    if m.chat.id==did:
      offer=m.text[11:]
      global av_offer
      av_offer=offer
@bot.message_handler(commands=['offers'])
def give_offers (m):
    bot.send_message(m.chat.id,av_offer,reply_markup=close_msg(),parse_mode='Html')
@bot.message_handler(commands=['send_proof'])
def fetch_proof(m):
    bot.reply_to(m,"Please Send A Photo of payment screenshot else use /cancel")
    bot.set_state(m.from_user.id, MyStates4.proof, m.chat.id)
    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
     data['proof'] = "pending"
@bot.message_handler(state=MyStates4.proof, content_types=['photo'])
def fory(m):
    bot.reply_to(m,"Processing your Payment \n Please wait for confirmation")
    bot.send_photo(chat_id=did,photo=m.json['photo'][0]['file_id'],caption="New Premium request : "+telebot.util.user_link(m.from_user) +"\n ID :<code>"+str(m.from_user.id)+"</code>",parse_mode="Html")
    bot.set_state(m.from_user.id, MyStates4.after_proof, m.chat.id)
    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
     data['after_proof'] = "requested"
@bot.message_handler(state=MyStates4.proof, content_types=['text'])
def get_proof(m):
    if m.text=='/cancel':
        bot.reply_to(m,"Process Cancelled ")
        bot.set_state(m.from_user.id, MyStates4.cancel_proof, m.chat.id)
        with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
         data['cancel_proof'] = "True"
    else :
        bot.reply_to(m,"Please Send a photo of payment proof or use /cancel ")
@bot.message_handler(commands=['remove_pro'])
def rrr(m):
    if m.from_user.id==did:
     id=m.text.split()[1]
     remove_pro(id)
     bot.send_message(m.chat.id, 'removed pro')
@bot.message_handler (func=lambda message :True)
def process_links(m):
# add_photo(m.from_user.id,photo_id)
 newtext = m.text
 
 if clks(newtext ):
    path=path='sessions/'+str(m.from_user.id)+'.json'
    if os.path.exists(path):
     os.remove('sessions/'+str(m.from_user.id)+".json")
 else :
     bot.reply_to(m,"No Links Detected ")
     return 
 add_photo(m.from_user.id)
 add_video(m.from_user.id)
 till_h = newtext.index('https') 
 if till_h==0:
   bv="YOUR LINKS " 
 else:
   caption = newtext[:till_h]
   bv=caption 
 #  print (bv)
# add_heading(m.from_user.id,bv)
 add_heading(m.from_user.id,bv)
 #print (m.forward_from_chat)
 bot.reply_to (m,text=bv,reply_markup=btn(m.from_user.id,m.text,ins=True,sub=sub_check(m.from_user.id)),disable_web_page_preview=True)
 

@bot.message_handler(content_types=['photo'])
def vvv(m):
 

 photo_id = m.json['photo'][0]['file_id']

 newtext = m.caption 
 #print ("New Text")
 #print (newtext)
 if newtext==None:
     bot.reply_to(m,"No links Found ")
     return 
 if clks(newtext ):
     try:
      path='sessions/'+str(m.from_user.id)+'.json'
      if os.path.exists(path):
       os.remove('sessions/'+str(m.from_user.id)+ ".json")
     except:
         pass
 else :
     bot.reply_to(m,"No Links Detected ")
     return 
 till_h = newtext.index('https') 
 if till_h==0:
   bv="Your Links" 
 else:
   caption = newtext[:till_h]
   bv=caption 
 add_photo(m.from_user.id,photo_id)
 add_heading(m.from_user.id,bv)
 bot.send_photo(m.chat.id,
                   photo=photo_id,
                   caption=bv,
                   reply_markup=btn(m.from_user.id,m.caption,ins=True,sub=sub_check(m.from_user.id)))
@bot.message_handler(content_types=['video'])
def vvv(m):
 video_id = m.video.file_id
 newtext = m.caption 
 if clks(newtext ):
     path='sessions/'+str(m.from_user.id)+'.json'
     if os.path.exists(path):
      os.remove(path)
 else :
     bot.reply_to(m,"No Links Detected ")
     return 
 till_h = newtext.index('https') 
 if till_h==0:
   bv="Your Links" 
 else:
   caption = newtext[:till_h]
   bv=caption 
 add_video(m.from_user.id,video_id)
 add_heading(m.from_user.id,bv)
 bot.send_video(m.chat.id,
                   video=video_id,
                   caption=bv,
                   reply_markup=btn(m.from_user.id,m.caption,ins=True,sub=sub_check(m.from_user.id)))
@bot.inline_handler(func=lambda query:True)
def query_text(query):
    #print (query.query)
   # print (query) 
    m=query.query

    text=query.query.split()
    #print(text) 
    till_h = None  # Initialize the index variable
    last_h=None
    for i, item in enumerate(text):
     if item.startswith("https://"):
        index = i
        break 
    rev=text [::-1]
    for i, item in enumerate(rev):
     if item.startswith("https://"):
        last_h = i
        break 
    if till_h==None:
     pass
    else:
     label=' '.join(text[:till_h])
    if last_h==None:
     heading=' '.join(text[till_h:])
    else:
     heading=' '.join(text[last_h:])
    
    #till_h=text.index('https')
    #print(till_h)
   # label=text[:till_h] 
    #print (label)
   # try:
     #last_h=text[::-1].index("https")-1 
  #  except:
     #last_h=till_h
  #  tg=text[last_h+1:]
  #  print (tg)
    url=text[1]
    label=text[0]
    results=[]
   # try :
    #    tg=text[2]
  #  except:
       # tg=label
   # print (label)
   # keyboard = telebot.types.InlineKeyboardMarkup()
  #  button = telebot.types.InlineKeyboardButton(text=label,url=url)
  #  keyboard.add(button)
    keyboard=btn(query.from_user.id,m,ins=True,inline_mode=True,label=label)
    # Create an inline query result with the keyboard
    result = telebot.types.InlineQueryResultArticle(
        id='1',
        title="Button ✅",
        input_message_content=telebot.types.InputTextMessageContent(heading),
        reply_markup=keyboard,
        description=" Label: "+ label +  "\n Link: " + url +" \n Text: " + heading
    )
    results.append(result)

    # Return the results to the user
    bot.answer_inline_query(query.id, results)

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.enable_save_next_step_handlers(delay=2)
bot.infinity_polling()
thread.join()