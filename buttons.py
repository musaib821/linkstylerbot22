from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

stripe = "https://checkout.stripe.com/c/pay/cs_live_a1oSTluquwQoMPAAmsS1j63odkbgigtZwqciayDd0MONhAdHfSBn76O2A8#fidkdWxOYHwnPyd1blppbHNgWjA0SHBpb1RWRlVXTFJ3UmBPd2dGbU1GU1FfT19uUz1VUENkQDVMTkdcb1dCRnFyMXNkcEB2ZD02NzNHZlYwVVZxVTBDUUBkYkxTal9CbmdKb2dCPGk0VGZhNTVGZ2pCfWJMcScpJ3VpbGtuQH11anZgYUxhJz8nZ0xcMW9NNnE2YmpmM3VCMWJiJ3gl"
import json
cha="chache.json" 
def back_to_first():
    buttons = [[
        InlineKeyboardButton('Featured Channel ®️',
                             url='https://t.me/DevSavior')
    ], [InlineKeyboardButton('◀️', callback_data='back_to_first')]]
    m = InlineKeyboardMarkup(buttons)
    return m

def back_to_others():
    buttons = [[
        InlineKeyboardButton('Featured Channel ®️',
                             url='https://t.me/DevSavior')
    ], [InlineKeyboardButton('◀️', callback_data='back_to_others')]]
    m = InlineKeyboardMarkup(buttons)
    return m

def first_markup():
    buttons = [
        InlineKeyboardButton('Need Help 🤔', callback_data='need_help_1')
    ], [InlineKeyboardButton('Others', callback_data='others')], [
        InlineKeyboardButton('Featured Channel', url='t.me/devsavior') ]
    m = InlineKeyboardMarkup(buttons)
    return m
def others1():
    buttons =[
        [InlineKeyboardButton('About', callback_data='about'),InlineKeyboardButton('Faqs', callback_data='faqs')],
        [InlineKeyboardButton('Featured Channel', url='t.me/devsavior'),InlineKeyboardButton('Back',callback_data='back_to_first')]]
    m = InlineKeyboardMarkup(buttons)
    return m
def faq_btn():
    pages=6 
    btns=[]
    for i in range( pages) :
     faq=InlineKeyboardButton(str(i+1),callback_data='faq_page_'+str(i+1))
     btns.append(faq)
    sbtns=[[InlineKeyboardButton('➡️',callback_data='faq2')],[InlineKeyboardButton('Back', callback_data='back_to_others')]]
    key=InlineKeyboardMarkup()
    key.add(*btns)
    key.add(InlineKeyboardButton('Back', callback_data='back_to_others'))
    return key 
def faq_back():
    btns=InlineKeyboardButton('Back', callback_data='back_to_faq')
    key=InlineKeyboardMarkup()
    key.add(btns)
    return key
def get_row_width_pro():
    buttons = [[InlineKeyboardButton('1 In Row', callback_data="row_width1"),
        InlineKeyboardButton('2 In Row ', callback_data='row_width2'),InlineKeyboardButton("3 In Row",callback_data="row_width3")],[InlineKeyboardButton('4 In Row', callback_data="row_width4"),
        InlineKeyboardButton('5 In Row ', callback_data='row_width5')],[
        InlineKeyboardButton('◀️', callback_data="back_to_main"),
        InlineKeyboardButton('NEXT', callback_data='to_title_pro')
    ]]
    m = InlineKeyboardMarkup(buttons)
    return m
def get_row_width_free():
    buttons = [[InlineKeyboardButton('1 In Row', callback_data="row_width1"),
        InlineKeyboardButton('2 In Row ', callback_data='row_width2'),InlineKeyboardButton("3 In Row",callback_data="row_width3")],[InlineKeyboardButton('4 In Row❎', callback_data="row_width4"),
        InlineKeyboardButton('5 In Row ❎', callback_data='row_width5')],[
        InlineKeyboardButton('◀️', callback_data="back_to_main"),
        InlineKeyboardButton('NEXT', callback_data='way_to_text')
    ]]
    m = InlineKeyboardMarkup(buttons)
    return m
def get_title_free():
    buttons = [[InlineKeyboardButton('◀️', callback_data='back_to_rw_free'),InlineKeyboardButton('Next',callback_data ='to_headings_free')]]
    m = InlineKeyboardMarkup(buttons)
    return m 
def get_title_pro():
    buttons = [[InlineKeyboardButton('◀️', callback_data='back_to_rw_pro'),InlineKeyboardButton('Next',callback_data ='to_headings_pro')]]
    m = InlineKeyboardMarkup(buttons) 
    return m 
def get_headings_free():
    buttons = [[InlineKeyboardButton('◀️', callback_data='back_to_rw_free'),InlineKeyboardButton('Next',callback_data ='next_to_title_free')]]
    m = InlineKeyboardMarkup(buttons)
    return m 
def get_headings_pro():
    buttons = [[InlineKeyboardButton('◀️', callback_data='back_to_rw_pro'),InlineKeyboardButton('Next',callback_data ='next_to_title_pro')]]
    m = InlineKeyboardMarkup(buttons)
    return m  
def to_edit(id): 
        path='sessions/'+str(id)+'.json'
        with open(path, 'r') as file:
         keyboard_data = file.read()
         confirm=InlineKeyboardButton ("DONE",callback_data ="confirm_data")
         rw=InlineKeyboardButton("Edit Row Width",callback_data="ed_row_width")
         hd=InlineKeyboardButton("Edit Headings ", callback_data="ed_heading")
         kerd = json.loads(keyboard_data) 
         keyboard = InlineKeyboardMarkup(row_width=int(kerd["row_width"]))
           # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"]
       #  print(b)
         all=len(b)
         sa=[]
         for i in range (all):
          o=b[i]
          
         # print (o)
          btn=InlineKeyboardButton(text=o[1],callback_data ="ssr"+o[0])
          sa.append(btn)
         keyboard.add (*sa)
         keyboard.add(rw,hd)
         keyboard.add (confirm)

        return keyboard 
def send_to_edit(id, data):
 #print (data)
 #fetch_data=data.split()
 print(data)
 try:
  link_index=data[3:5]
 except: 
  link_index=data[3] 
 print(link_index)
 path='sessions/'+str(id)+".json"
 with open(path, 'r') as file:
         keyboard_data = file.read()
        # keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
           # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"]
         print(b)
         s=b[int(link_index) ]
       #  print (s)
         text="text :" +str(s[1]) +" Link: "+str(s[2])
        # keyboard.add (btn)
         return (text) 
def get_btn_text(id,data):
# try:
 link_index=data[9:]
 #except: 
  #link_index=data[3] 
 path='sessions/'+str(id)+".json"
 with open(path, 'r') as file:
         keyboard_data = file.read()
         
         kerd = json.loads(keyboard_data)
         keyboard = InlineKeyboardMarkup()
           # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"]
         s=b[int(link_index) ]
       #  print (s)
         text="text :" +str(s[1]) +" Link: "+str(s[2])
         return text
def send_btn_to_edit(id, data):
 #print (data)
 #fetch_data=data.split()
 try:
  link_index=data[3:5]
 except: 
  link_index=data[3] 
 path='sessions/'+str(id)+".json"
 with open(path, 'r') as file:
         keyboard_data = file.read()
         
         kerd = json.loads(keyboard_data)
         keyboard = InlineKeyboardMarkup()
           # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"]
         s=b[int(link_index) ]
         #print (s)
         text="text :" +str(s[1]) +" Link: "+str(s[2])
         edit_label =InlineKeyboardButton ("Edit Label", callback_data ="cust_lebl"+str(s[0]))
         edit_link =InlineKeyboardButton ("Edit Link", callback_data ="cust_link"+str(s[0]))
         confirm=InlineKeyboardButton ("Confirm ", callback_data ="edit21")
         #back=InlineKeyboardButton ("Back",)
         keyboard.add (edit_label,edit_link)
         keyboard.add (confirm )
         return (keyboard) 
def edit_btn_link(id,data,link,plan):
 path='sessions/'+str(id)+".json"
# print(link)
 index=int(data[9:]) 
# print(plan)
 #print (index) 
# if plan=="FREE" and 
 with open(path, 'r') as file:
         keyboard_data = file.read()
         keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
         edits=kerd['edits']
         if plan==False and edits>=5 :
            data="ssr"+str(index)
            print ("limited ")
            return send_btn_to_edit(id,data)
           # keyboard.from_jso 
         #all=len(kerd) on on
         kerd["last_button"][int(index) ][2]=link
         #s=b[int(index) ]
        # s[1]=link 
         su=kerd["last_button"][int(index) ][2]
         kerd['edits']+=1
        # print(su)
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
         # l={"last_button":b, "row_width":kerd["row_width"]}
          p=json.dumps(kerd) 
  #  print (p)
          f.write(p)
         data="ssr"+str(index) 
         return send_btn_to_edit(id,data) 
def edit_btn_label(id,data,label,plan):
 path='sessions/'+str(id)+".json"
 print(plan)
# print(data)
 index=int(data[9:]) 
 #print (index)
 with open(path, 'r') as file:
         keyboard_data = file.read()
         keyboard = InlineKeyboardMarkup()
         kerd = json.loads(keyboard_data)
         edits=kerd['edits']
         if plan==False and edits>=5 :
            data="ssr"+str(index)
            print ("limited")
            return send_btn_to_edit(id,data)
           # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"][int(index) ][1]=label
         kerd['edits']+=1
        #s=b[int(index) ]
         #s[1]=label
         with open (path,'w') as f:
   # print (keyboard2) 
   
  # print (id)
         # l={"last_button":b, "row_width":kerd["row_width"]}
          p=json.dumps(kerd) 
  #  print (p)
          f.write(p)
         # print ("edited")
         data="ssr"+str(index)  
          
         return send_btn_to_edit(id,data)
def gen_new_markup(id): 
# try:  
        path='sessions/'+str(id)+".json"
        with open(path, 'r') as file:
         keyboard_data = file.read()
         
         kerd = json.loads(keyboard_data) 
         keyboard = InlineKeyboardMarkup(row_width=int(kerd["row_width"]))
           # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"]
       #  print(b)
         all=len(b)
         sa=[]
         for i in range (all):
          o=b[i]
          
         # print (o)
          btn=InlineKeyboardButton(text=o[1],callback_data ="ssr"+o[0])
          sa.append(btn)
         keyboard.add (*sa)
         keyboard.add (InlineKeyboardButton ("Done ",callback_data="confirm_data"))
        return keyboard 
def confirmed_btn(id,post=False):
        path='sessions/'+str(id)+".json"
        with open(path, 'r') as file:
         keyboard_data = file.read()
         
         kerd = json.loads(keyboard_data) 
         keyboard = InlineKeyboardMarkup(row_width=int(kerd["row_width"]))
         
            # keyboard.from_jso 
         #all=len(kerd)
         b=kerd["last_button"]
       #  print(b)
         all=len(b)
         sa=[]
         for i in range (all):
          o=b[i]
          
         # print (o)
          btn=InlineKeyboardButton(text=o[1],url =o[2])
          sa.append(btn)
         keyboard.add (*sa)
         confirm=InlineKeyboardButton ("Post To Channel",callback_data ="channel_post") 
 #ch_=InlineKeyboardButton ("Channel Post, ")
 
         edy=InlineKeyboardButton (text="Edit",callback_data='edit21')
         if post ==False :
          keyboard.add (edy,confirm) 
         return keyboard 
def channel_button(id):
 keyboard =InlineKeyboardMarkup () 
 
 btn=InlineKeyboardButton ()
def get_free_trail():
    keyboard=InlineKeyboardMarkup()
    btn=InlineKeyboardButton("Get Free Trail ",callback_data="free_trail")
    btn2=InlineKeyboardButton('close ', callback_data='Close_msg')
    keyboard.add(btn,btn2)
    return keyboard 
def close_msg():
    btn=InlineKeyboardButton('close ', callback_data='Close_msg')
    key=InlineKeyboardMarkup()
    key.add(btn)
    return key 
def close_chat ():
    btn=InlineKeyboardButton('Close Chat', callback_data='close_support_chat')
    key=InlineKeyboardMarkup() 
    key.add(btn)
    return key