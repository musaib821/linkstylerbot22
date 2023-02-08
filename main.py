import telebot
from pytube import YouTube
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
my_secret = "5699136129:AAE_Cd0DlRUHlGExGFpJJ_pxhvcFpS5q_6Q"
bot = telebot.TeleBot(my_secret)
@bot.message_handler(commands=[ 'start'])
def send_welcome(message):
 bot.reply_to(message,"Hi Master") 
@bot.message_handler(commands=[ 'help'])
def send_help(m):
 bot.reply_to(m,text="Hello Master I Am Link Styler Bot \n Use /text To Send Me Text That Will Be Clickable \n use /link to send me Link That You Want To Style \n use /head if you want to add any text before links like a heading  \n For More Info You Can Ping My Master @ffmusaib ") 
@bot.message_handler(commands=['title'])
def set_title(t):
 global title
 cut_title=t.text.split()
 cut_title.remove("/title")
 title=" ".join(map(str,cut_title)) 
 if len(title)>0: 
  global title2
  title2=title
 else:
  title2=" "
  bot.reply_to(title,"Done "+"Text1 Set To ["+title2+"] Now Send Links")
@bot.message_handler(regexp='((https?):((//)|(\\\\))+(\w\d:#@%/;$()~_?\+-=\\\.&?)*)')
def link(links):
  #bot.reply_to(message2,"keyboard")
  global split_links
  split_links=links.text.split()
  def get_links(x):
   return x[0:4] in 'https' 
  global only_links
  only_links= filter(get_links,split_links)
  global var 
  var=[]
  for i,x in enumerate(only_links,start=1):
   raw_btn=f"InlineKeyboardButton('{str(i) }',url='{str(x)}')"
   btn_obj=eval(raw_btn)
   var.append(btn_obj)
  li =''.join(map(str,var))
  #def extractDigits(lst):
  pygh=InlineKeyboardButton("Yes",url="www.google.com")
  res = [] 
  global keyboard
  keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")]
    ]
  NewList= [[x] for x in var]
  m = InlineKeyboardMarkup(NewList,row_width=4)
  
  #m.row = 2
  #m.add(keyboard)
  #print(keyboard)
#  jaka ="Google"
 # kaj=eval(jaka)
  print (li)
  def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(li)
    return markup
  #for el in var: 

  # sub = el.split(',') 

  # res.append(sub) 

      
 # print (li)
  #  return(res) 
 # new_lp=extract
  bot.reply_to(links,"Li",reply_markup=m)
@bot.message_handler(content_types=['photo'])
def get_text1hh(ggh):
 hh=ggh.photo.file_id.file_id
 bot.reply_to(ggh,hh)
 bot.send_photo(ggh.chat.id,photo="AgACAgUAAxkBAAEc6qBj4pyVxo3kpEuZBq80qg32P4y86AACdrgxGzCYkFa4zujaLBqiYwEAAwIAA3kAAy4E")

 


bot.infinity_polling()
