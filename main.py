import os
import telebot

my_secret = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(my_secret)

# Handle '/start' and '/help'
@bot.message_handler(commands=[ 'start'])
def send_welcome(message):
# bid=user.chat_id
 bot.reply_to(message,"Hi Master") 
@bot.message_handler(commands=[ 'help'])
def send_help(m):
    bot.reply_to(m,text="Hello Master I Am Link Styler Bot \n Use /text To Send Me Text That Will Be Clickable \n use /link to send me Link That You Want To Style \n use /head if you want to add any text before links like a heading  \n For More Info You Can Ping My Master @ffmusaib ") 
@bot.message_handler(commands=['text'])
def get_text1(m):
 global text1
 text_in=m.text.split()
 text_in.remove("/text")
 text1=" ".join(map(str,text_in)) 
# global text2
 bot.reply_to(m,"Done "+"Text1 Set To "+text1+" Now Send Links")
@bot.message_handler(regexp='((https?):((//)|(\\\\))+(\w\d:#@%/;$()~_?\+-=\\\.&?)*)')
def link(message2):
 sorted=message2.text.split()
 
 var=[]
 for i, x in enumerate(sorted,start=1):
   active ="<a href='"+str(x) +"'>            Download Episode "+str(i)+"  📥</a>"
   #print(active) 
   if len(text1)>0: 
    global text2
    text2=text1
   else:
  # global text2
    text2=" "
   var.append(active)
   var.insert(0,text2)
 li = '               \n'.join(map(str,var))

 li+="\n"+"                        <a href='@ffmusaib' >Join Main Channel</a>"
 bot.reply_to(message2,li,parse_mode='Html') 
# bot.reply_to(message,text=var)    
#bot.edit_message_text(text=var,chat_id=message.chat.id,message_id=new_msg,)
bot.polling()