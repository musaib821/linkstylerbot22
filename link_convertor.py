from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
def title_ext(m) :
  text=m.text.split()
  global text1
  text_in=m.text.split()
  text_in.remove("/title")
  text1=" ".join(map(str,text_in)) 
  if len(text1)>0: 
   global text2
   text2=" Good"
  else:
    text2=" "
  return text2
def row():
 #delh(m)
 #print (v)
 #vmessageid=v.message_id+1
 row=[InlineKeyboardButton('1', callback_data="1")], [InlineKeyboardButton('2', callback_data="2")]
 m2 =InlineKeyboardMarkup(row)
 return m2
def buttons():
 buttons=[[InlineKeyboardButton ('Join Channel', url="t.me/musaibofficial"),InlineKeyboardButton ('Lets Start',callback_data='info')]]
 m=InlineKeyboardMarkup(buttons, row_width=2)
 return m 
def info_(call):
 if call.data=='info':
  bot.edit_message_text()
  
 