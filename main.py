import os
from variables import *
from text import  *
import json
import schedule 
import time 
from telebot import * 
from load_data import*  
print (get_users())
schedule.every(1).minutes.do(remove_sub)
from datetime import datetime, timedelta
from buttons import *
import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')
requests=[]
filename = "new.json"
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup 
from telebot.types import *
from links import *
from telebot import custom_filters
#my_secret = os.environ['BOT_TOKEN']
my_secret = "5699136129:AAE_Cd0DlRUHlGExGFpJJ_pxhvcFpS5q_6Q"
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage 
state_storage = StateMemoryStorage()
dict = {}
bot = telebot.TeleBot(my_secret, state_storage=state_storage)
class MyStates(StatesGroup):
  title = State()
  user_id = State()
  row_length = State()
  text = State()
  text1 = State()
  id=State()
class MyStates2(StatesGroup):
  user_id = State()
  text = State()
  id=State()
class MyStates3(StatesGroup):
  user_id = State()
  photo = State()
  id=State()
class MyStates4(StatesGroup):
  title = State()
  user_id = State()
  row_length = State()
  text = State()
  text1 = State()
  id=State()
class MyStates5(StatesGroup):
  user_id = State()
  photo = State()
  id=State()
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == "start":
   if check_pro(call.from_user.id) :
      bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=next_1,reply_markup=gen_markup2())
   else:
     bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=next_1,reply_markup=gen_markup21())
  elif call.data == "back2":
    bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=next_1,
                          reply_markup=gen_markup2(),parse_mode='Html')
  elif call.data == "back1":
    bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,
text=starting_message.format(telebot.util.user_link(call.from_user)),reply_markup=gen_markup(),parse_mode='Html')
  elif call.data == "customize":
    bot.edit_message_text(message_id=call.message.message_id,chat_id=call.from_user.id,text=next_2, reply_markup=gen_markup10())

  elif call.data == 'setting':
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_3,
                          reply_markup=gen_markup3())
  elif call.data == 'back3':
   # jj = call.data
    #snd_cl(call.from_user.id, jj)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_2,
                          reply_markup=gen_markup10())

  elif call.data == '1':
    jj = call.data
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "1"
 
    bot.edit_message_reply_markup(message_id=call.message.message_id,
                                  chat_id=call.from_user.id,
                                  reply_markup=gen_markup4())
  elif call.data == '2':
    jj = call.data
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "2"
 

    bot.edit_message_reply_markup(message_id=call.message.message_id,
                                  chat_id=call.from_user.id,
                                  reply_markup=gen_markup5())
  elif call.data == '0':
    jj = call.data
    bot.answer_callback_query(call.id,
                              show_alert=True,
                              text="Not Supported Yet")

    bot.edit_message_reply_markup(message_id=call.message.message_id,
                                  chat_id=call.from_user.id,
                                  reply_markup=gen_markup3())

  elif call.data == 'title':
    #print (call)
    bot.set_state(call.from_user.id, MyStates4.user_id, call.from_user.id)
    bot.set_state(call.from_user.id, MyStates4.id,call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
     data['id'] = call.message
    

    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_4,
                          reply_markup=gen_markup12())
  elif call.data == "3":
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup6())
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "3"
  elif call.data == "4":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup7())
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "4"
  elif call.data == "5":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup8())
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "5"
  elif call.data == "others":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_6,
                          reply_markup=gen_markup11())
  elif call.data == "text":
    #  print (call)
    bot.set_state(call.from_user.id, MyStates2.user_id, call.from_user.id)
    

    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_5,
                          reply_markup=gen_markup12())
  elif call.data == "bacgk4":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_2,
                          reply_markup=gen_markup10())
  elif call.data == "about":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=about.format(get_users()),
                          reply_markup=gen_markup13(),parse_mode='html',disable_web_page_preview=True)
  elif call.data == "back4":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_6,
                          reply_markup=gen_markup11())
  elif call.data == "faq":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup13())
  elif call.data == "account":
    # print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=get_pro_dt(call.from_user.id),
                          reply_markup=gen_markup13())
  elif call.data == "upih":
    #print (call.data)
   #￼in# media=￼in 
    s= InputMediaPhoto(photo_id2,caption="See")
    bot.edit_message_media(chat_id=call.from_user.id, media=s, message_id=call.message.message_id,reply_markup=gen_markup11())
    bot.set_state(call.from_user.id, MyStates3.user_id, call.from_user.id) 
  elif call.data == "back2":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup())
  elif call.data == "customize1":
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_2,
                          reply_markup=gen_markup101())

  elif call.data == 'setting1':
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_3,
                          reply_markup=gen_markup31())
  elif call.data == 'back31':
    jj = call.data
    #snd_cl(call.from_user.id, jj)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_2,
                          reply_markup=gen_markup101())

  elif call.data == '11':
    jj = call.data
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "1"
  
    bot.edit_message_reply_markup(message_id=call.message.message_id,
                                  chat_id=call.from_user.id, 
                                  reply_markup=gen_markup41())
  elif call.data == '21':
    jj = call.data
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "2"
  

    bot.edit_message_reply_markup(message_id=call.message.message_id,
                                  chat_id=call.from_user.id,
                                  reply_markup=gen_markup51())
  elif call.data == '01':
    jj = call.data
    bot.answer_callback_query(call.id,
                              show_alert=True,
                              text="Not Supporred Yet")

    bot.edit_message_reply_markup(message_id=call.message.message_id,
                                  chat_id=call.from_user.id,
                                  reply_markup=gen_markup31())

  elif call.data == 'title1':
    #print (call)
    bot.set_state(call.from_user.id, MyStates.user_id, call.from_user.id)
    bot.set_state(call.from_user.id, MyStates.id, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
     data['id'] = call.message
    # print (data)


      #data["id"]=call.mesdage.id
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_4,
                          reply_markup=gen_markup121())
  elif call.data == "31":
    #elif call.data == '21':
    jj = call.data
    bot.set_state(call.from_user.id, MyStates.row_length, call.from_user.id)
    with bot.retrieve_data(call.from_user.id, call.from_user.id) as data:
      data['row_length'] = "3"
      bot.edit_message_reply_markup(message_id=call.message.message_id,
                                  chat_id=call.from_user.id,
                                  reply_markup=gen_markup61())
 
  elif call.data == "41":
    #  print (call)
    bot.answer_callback_query(call.id, text=" This Is A Premium Feature!! \n Join Premium First 🥇")
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup31())
    
    #  print (call)
  elif call.data=="51":
    bot.answer_callback_query(call.id, text=" This Is A Premium Feature!! \n Join Premium First 🥇")
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup31())
    
  elif call.data == "others1":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_6,
                          reply_markup=gen_markup111())
  elif call.data == "text1":
    bot.answer_callback_query(call.id, text=" This Is A Premium Feature!! \n Join Premium First 🥇")
    

    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_2,
                          reply_markup=gen_markup101())
  elif call.data == "back311":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_2,
                          reply_markup=gen_markup101())
  elif call.data == "back31_pro":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_2,
                          reply_markup=gen_markup2())
  elif call.data == "about1":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=about.format(get_users()),
                          reply_markup=gen_markup131(),parse_mode='html',disable_web_page_preview=True)
  elif call.data == "back41":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_6,
                          reply_markup=gen_markup111())
  elif call.data == "faq1":
    #  print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=call.message.text,
                          reply_markup=gen_markup131())
  elif call.data == "premium":
    # print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=premium,
                          reply_markup=gen_markup141(),parse_mode='Html')
  elif call.data == "back21":
    # print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=starting_message.format(telebot.util.user_link(call.from_user)),
                          reply_markup=gen_markup(),parse_mode='Html')
  elif call.data == "back61":
    # print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_1,
                          reply_markup=gen_markup21()) 
  elif call.data == "back71":
    # print (call)
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=next_6,
                          reply_markup=gen_markup111()) 
  elif call.data == "upi":
    bot.send_photo(chat_id=call.from_user.id, photo=photo_id2,reply_markup=gen_markup119(),caption=upi_text,parse_mode='html')
    bot.set_state(call.from_user.id, MyStates3.user_id, call.from_user.id) 
  elif call.data =="proof":
    bot.answer_callback_query(call.id, text="Send Payment Screenshot ")
    bot.set_state(call.from_user.id, MyStates5.user_id, call.from_user.id)
  elif call.data=="Cancel":
    bot.delete_message (message_id=call.message.message_id,chat_id=call.from_user.id)
  elif call.data=='Cancel1':
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=premium,
                          reply_markup=gen_markup141()) 
  elif call.data=='crypto':
    bot.edit_message_text(message_id=call.message.message_id,
                          chat_id=call.from_user.id,
                          text=crypto,
                          reply_markup=gen_markup129())
  elif call.data=='dev':
   if call.from_user.id==admins[0]:
     bot.send_message (admins[0],text=devcom)
   else :
     bot.answer_callback_query(call.id, text="🚫 This Option Is Available Only For Developers ")
@bot.message_handler(state=MyStates5.user_id, content_types=['photo'])
def name_get(message):
  bot.send_message(message.chat.id,"Thanks For Purchase ❤\n Your Request Will Be Processed ASAP!!")
  bot.set_state(message.from_user.id, MyStates3.photo, message.chat.id)
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
   # print (data)

    deta=data['photo'] =message.json['photo'][0]['file_id']
    #print (message.from_user.first_name)
  user=telebot.util.user_link(message.from_user) 
  caption=telebot.util.user_link(message.from_user)+" "+str(message.from_user.id) 
  bot.send_photo (chat_id=admins[0],photo=deta,caption=caption,parse_mode='html')
 
@bot.message_handler(state=MyStates2.user_id)
def name_get(message):
  bot.send_message(message.chat.id, "Label Added")
  bot.set_state(message.from_user.id, MyStates2.text, message.chat.id)
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    data['text'] = message.text

@bot.message_handler(state=MyStates4.id)
def name_get(message):
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    id=data["id"]
  
  bot.reply_to(message, "Title Added")
 
  bot.set_state(message.from_user.id, MyStates4.title, message.chat.id)
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    data['title'] = message.text 
@bot.message_handler(state=MyStates.id)
def name_get(message):
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    id=data["id"]
  """
    State 1. Will process when user's state is MyStates.name.
    """
  bot.reply_to(message, "Title Added")
 # bot.send_message(chat_id=message.chat.id,text=" okg",reply_markup=gen_markup121())
  bot.set_state(message.from_user.id, MyStates.title, message.chat.id)
  with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    data['title'] = message.text 

@bot.message_handler(commands=['start', 'help'])
def reply(m):
  try:
    user_name = m.from_user.first_name + " " + m.from_user.last_name
  except TypeError:
    user_name = m.from_user.first_name
  except TypeError:
    user_name = m.from_user.last_name
  except TypeError:
    user_name = "user" 
  user=telebot.util.user_link(m.from_user) 
  #print (user_name) 
  s=starting_message.format(user)
  
  bot.send_message(m.chat.id, 
                       text=s,
                       reply_markup=gen_markup(),
                       parse_mode='Html')
  bot.delete_state(m.from_user.id, m.chat.id)
  check_sub(m.from_user.id)

# print (v)
@bot.message_handler(content_types=['photo'])
def vvv(m):
  

 photo_id = m.json['photo'][0]['file_id']
 newtext = m.caption
 till_h = newtext.index('https') 
 
 try:
  with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
      bv = data['title']
 except KeyError:
  if till_h==0:
   bv="Your Links" 
  else:
   caption = newtext[:till_h]
   bv=caption 
 
 try:
  with bot.retrieve_data(m.from_user.id, m.from_user.id) as data:
          row_length = data['row_length']
 except:
        row_length = '2'
 try:
   with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
          echo = data['text']
 except:
        echo = ''
    
    #print (row_length)
 bot.send_photo(m.chat.id,
                   photo=photo_id,
                   caption=bv,
                   reply_markup=btn(newtext, row_length, echo))


@bot.message_handler(
  regexp=
  r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
)
def get_text(m):
 newtext = m.text
 #try:
 till_h = newtext.index('https') 
 try:
  with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
      bv = data['title']
 except KeyError:
  if till_h==0:
    bv="Your Links"
 #except :
  # bv="Your Links"
  else:
   caption = newtext[:till_h]
   bv=caption 
  
 try:
  with bot.retrieve_data(m.from_user.id, m.from_user.id) as data:
          row_length = data['row_length']
 except:
        row_length = '2'
 try:
   with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
          echo = data['text']
 except:
        echo = ''
 
 bot.send_message(m.chat.id,
                   text=bv,
                   reply_markup=btn(newtext, row_length, echo))


@bot.message_handler(content_types=['video', 'document'])
def say_no(m):
  bot.reply_to(m,
               "No Links Detected Please Use /help Or /start To Get Started ")


@bot.channel_post_handler(
  regexp=
  r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
)
def channel_handler(m):
  add_channel(m.chat.id)
  
  if m.text[0:4] == '!row':
    s=m.text.split()
    print (s[1])
    index = m.text.index('!row')
    h=re.findall(r'\((.*?)\)', m.text) 
    #print( h) 
    try:
     label=h[0]
     hv=m.text.index(')')
    except:
      label=""
      hv=index+4    
      #label=m.text[6]
    #h=telebot.util.extract_arguments(m.text)
     # hv=m.text.index(')')
    newtext = m.text[hv+1:]
    till = newtext.index('https')
    caption = newtext[:till]
    #print(len(caption))
    print(label)
    row_length = m.text[4]
   # ₹₹def check():
    if check_channel(m.chat.id):
      pass 
    else:
      if int(row_length)>3:
        row_length="3"
        label=" " 

    if len(caption) <= 1:
     caption = "Links"
     bot.edit_message_text(message_id=m.id,
                            chat_id=m.chat.id,
                            text="links",
                            reply_markup=btn(newtext, row_length,label)) 
    else:
      # pass
      captain =caption
      bot.edit_message_text(message_id=m.id,
                            chat_id=m.chat.id,
                            text=caption,
                            reply_markup=btn(newtext, row_length,label))
  else:
    pass




@bot.message_handler(commands=['post'])
def post(m):
  text = m.text

  if m.from_user.id == 1070433131:
    with open(filename, 'r') as file:
      subs = file.read()
      jsn = json.loads(subs)
      ll = jsn['subs']
      for line in ll:
        print(line)
        try:
          bot.send_message(text=text, chat_id=int(line))
        except:
          with open(filename, 'r') as file:
            content = file.read()
            jsn = json.loads(content)
            ll = jsn['subs']
            ll.remove(str(id))
            #new=jsn.dump()
            with open(filename, 'w') as file:
              json.dump(jsn, file)

  else:
    bot.send_message(text='You are Not a Developer ', chat_id=m.from_user.id)


@bot.message_handler(commands=['send_file'])
def ju(m):
  if m.from_user.id == 1070433131:
    with open(filename, 'rb') as file:
      bot.send_document(document=file, chat_id=m.from_user.id)
@bot.message_handler(commands=['add_pro'])
def ju(m):
  #print (m)
  data=m.text.split()
  id=data[1]
  days=data[2]
  
  new=data[3:]
  well= ' '.join(new)
  welcome=well +f" \n Enjoy Premium For :{days}:)"
 # add_pro(id, days)
  if m.from_user.id == 1070433131:
    data=m.text.split()
    id=data[1]
    days=data[2]
    
    add_pro(id, days)
    #print (id)
    bot.send_message(chat_id=int(id),text=welcome) 
    with open(filename, 'rb') as file:
      bot.send_document(document=file, chat_id=m.from_user.id)
    print (get_pro_dt(id)) 
@bot.message_handler(commands=['add_channel'])
def ju(m):
  if m.from_user.id == 1070433131:
    data=m.text.split()
    id=data[1]
   # days=data[2]
    
    add_channel(id)
    bot.reply_to(m,"added Channel")
  else:
    pass 
@bot.message_handler(commands=['remove_pro'])
def ju(m):
  if m.from_user.id == 1070433131:
    data=m.text.split()
    id=data[1]
   # days=data[2]
    
    remove_pro(id)
    bot.reply_to(m,"Removed User")
  else:
    pass
@bot.message_handler(commands=['get_info'])
def ju(m):
  if m.from_user.id == 1070433131:
    data=m.text.split()
    id=data[1]
   # days=data[2]
    
    bot.reply_to(m,get_pro_dt(id) )
  else:
    pass
@bot.channel_post_handler(content_types=['photo'])
def boht(m):
  photo_id = m.json['photo'][0]['file_id']
    
  newtext = m.caption
 #try:
  till_h = newtext.index('https') 
  try:
   with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
      bv = data['title']
  except KeyError:
   if till_h==0:
    bv="your Links" 
   else:
    caption = newtext[:till_h]
    bv=caption 
  bot.send_message(m.chat.id, photo_id)
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.infinity_polling(skip_pending=True)
while True:
    schedule.run_pending()
    time.sleep(1)
