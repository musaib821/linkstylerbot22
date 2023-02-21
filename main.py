import os
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from links import *
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup

from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()  #

my_secretsecret="5989308938:AAFrPoIHzm3KlIlPCsIIVQEu0uGd9RtmDb4"
bot = telebot.TeleBot(my_secret, state_storage=state_storage)


class MyStates(StatesGroup):
  # Just name variables differently
  name = State()  # creating instances of State class is enough from now
  user_id = State()
  param = State()


def gen_markup():
  buttons = [[InlineKeyboardButton('Join Channel', url='t.me/botarcheive')],
             [InlineKeyboardButton('Lets Start', callback_data='start')]]
  m = InlineKeyboardMarkup(buttons)
  return m


def gen_markup2():
  buttons = [[InlineKeyboardButton('Setting', callback_data='setting')],
             [InlineKeyboardButton('Set Icon', callback_data='links')]]
  m = InlineKeyboardMarkup(buttons)
  return m


def gen_markup3():
  buttons = [[InlineKeyboardButton('HTML ', callback_data='html')],
             [
               InlineKeyboardButton('1', callback_data='1'),
               InlineKeyboardButton('2', callback_data='2')
             ], [InlineKeyboardButton('Back', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m


def gen_markup4():
  buttons = [[InlineKeyboardButton('HTML ', callback_data='html')],
             [
               InlineKeyboardButton('1✅', callback_data='1'),
               InlineKeyboardButton('2', callback_data='2')
             ], [InlineKeyboardButton('Back', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m


def gen_markup5():
  buttons = [[InlineKeyboardButton('HTML ', callback_data='html')],
             [
               InlineKeyboardButton('1', callback_data='1'),
               InlineKeyboardButton('2 ✅', callback_data='2')
             ], [InlineKeyboardButton('Back', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m


def snd_cl(m, jj):
  bot.set_state(m, MyStates.param)
  with bot.retrieve_data(m) as data:
    data['param'] = jj
    data['id'] = m
# print(m)


#  id=m.from_user.id
  Data = data
  news = f"From User {Data['id']} {Data['param']}"
  bot.send_message(chat_id='-1001784188368', text=news)


def gen_markup6():
  buttons = [[InlineKeyboardButton('HTML✅', callback_data='html')],
             [
               InlineKeyboardButton('1', callback_data='1'),
               InlineKeyboardButton('2', callback_data='2')
             ], [InlineKeyboardButton('Back', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  # print (call)
  if call.data == "start":
    bot.edit_message_text(message_id=v.id,
                          chat_id=call.from_user.id,
                          text="Answer is Yes",
                          reply_markup=gen_markup2())
  elif call.data == "No":
    bot.send_message(v.chat.id, "Answer Is No")
  elif call.data == "links":
    bot.edit_message_text(message_id=v.id,
                          chat_id=call.from_user.id,
                          text=" Set Your Name")
    #if text=='vv':
    #  bot.reply_to(v,"vv coicker")

  elif call.data == 'setting':
    bot.edit_message_text(message_id=v.id,
                          chat_id=v.chat.id,
                          text="Settings",
                          reply_markup=gen_markup3())
  elif call.data == 'back':
    jj = call.data
    snd_cl(call.from_user.id, jj)
    bot.edit_message_text(message_id=v.id,
                          chat_id=v.chat.id,
                          text='Hi',
                          reply_markup=gen_markup2())

  elif call.data == '1':
    jj = call.data
    snd_cl(call.from_user.id, jj)
    # print(call)
    bot.edit_message_reply_markup(message_id=v.id,
                                  chat_id=v.chat.id,
                                  reply_markup=gen_markup4())
  elif call.data == '2':
    jj = call.data
    snd_cl(call.from_user.id, jj)
    #  snd_cl(call)

    bot.edit_message_reply_markup(message_id=v.id,
                                  chat_id=v.chat.id,
                                  reply_markup=gen_markup5())
  elif call.data == 'html':
    jj = call.data
    snd_cl(call.from_user.id, jj)
    # snd_cl(call)
    bot.edit_message_reply_markup(message_id=v.id,
                                  chat_id=v.chat.id,
                                  reply_markup=gen_markup6())
    #bot.edit_message_text(message_id=v.id, chat_id=v.chat.id,text='Hi',reply_markup=gen_markup2())
    #bot.answer_callback_query(call.id, "Answer is No")


@bot.message_handler(commands=['start'])
def reply(m):
  #bot.set_state(message.from_user.id, MyStates.name, message.chat.id
  #bot.set_state(m.from_user.id, MyStates.name, m.chat.id)
  global v
  v = bot.reply_to(m, "Ok ", reply_markup=gen_markup())


# bot.send_message (chat_id='-1001784188368',text=" h")
@bot.channel_post_handler(content_types=['text'])
def cx(m):
  bot.reply_to(m, m.chat.id)


# print (v)
@bot.message_handler(commands=['link'])
def vvv(m):
  # print (m)
  # btn(m)
  bot.reply_to(m, "Links are", reply_markup=btn(m))


@bot.message_handler(commands=['create'])
def create_file(m):
  bot.reply_to(m, "File Created")
  f = open("guru99.txt", "w")
  f.write(m.text)
  # f.close()
  bot.send_document(m.chat.id, document=f)
  f.close()


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.infinity_polling(skip_pending=True)
