filename="new.json" 

from datetime import datetime, timedelta
import json
import os 
import pytz 
tz = pytz.timezone('Asia/Kolkata')  
def check_channel(h):
  id = str(h)
  filename = "new.json"
  if os.path.isfile(filename):
    with open(filename, 'r') as file:
      content = file.read()
      cont = json.loads(content)

      # print (content)
      if id in cont['channel']:
        return True 
      else:
        return False
def get_users():
  #if os.path.isfile(filename):
    with open(filename, 'r') as file:
      content = file.read()
      cont = json.loads(content) 
      return  len(cont['subs'])+600       
def add_channel(h):
  id = str(h)
  filename = "new.json"
  if os.path.isfile(filename):
    with open(filename, 'r') as file:
      content = file.read()
      cont = json.loads(content)

      # print (content)
      if id in cont['channel']:
        pass
      else:
        x = id
        cont['channel'].append(x)
        with open('new.json', 'w') as f:
          json.dump(cont, f)
def check_sub(h):
  id = str(h)
  filename = "new.json"
  if os.path.isfile(filename):
    with open(filename, 'r') as file:
      content = file.read()
      cont = json.loads(content)

      # print (content)
      if id in cont['subs']:
        pass
      else:
        x = id
        cont['subs'].append(x)
        with open('new.json', 'w') as f:
          json.dump(cont, f)
          
  else:
    with open(filename, 'w') as file:
      x = {'subs': [id]}
      json.dump(x, file)


#check_sub('ghh6')
def check_pro(h):
  id = str(h)
  filename = "new.json"
  #if os.path.isfile(filename):
  with open(filename) as file:

    content = json.load(file)
    b = content["premium"]
    result = any(id in sublist for sublist in b)
    return result


#print(check_pro(1234))

def add_proc(h, days):
  id = str(h)
  tz = pytz.timezone('Asia/Kolkata')

  date = datetime.now(tz).isoformat()
  #expiry=datetime.
  # date=
  #print (date)
  filename = "new.json"

  with open(filename) as file:
    data = json.load(file)
    x = [id, date, days]
    b = data["channel"]
    if any(id in sublist for sublist in b ) :
     pass
    else:
     data['channel'].append(x)
    with open('new.json', 'w') as f:
      json.dump(data, f)
def add_pro(h, days):
  id = str(h)
  tz = pytz.timezone('Asia/Kolkata')

  date = datetime.now(tz).isoformat()
  #expiry=datetime.
  # date=
  #print (date)
  filename = "new.json"

  with open(filename) as file:
    data = json.load(file)
    x = [id, date, days]
    b = data["premium"]
    if any(id in sublist for sublist in b ) :
     pass
    else:
     data['premium'].append(x)
    with open('new.json', 'w') as f:
      json.dump(data, f)

def remove_pro(h):
 # id = str(h)
  with open(filename) as file:
    data = json.load(file)
    id=str(h)
    b = data["premium"]
    bb = [
      "{}".format(index1) for index1, value1 in enumerate(b)
      for index2, value2 in enumerate(value1) if value2 == id
    ]
    print (str(b)) 
   # print (str(bb)) 
    c = int(bb[0])
    print (f" c={c}")
    p_date = b[c][1]
    h=b[c]
    r=b.pop(c)
    with open(filename,'r') as file:
     deta=json.load(file)
     r=deta["premium"].pop(c)
     # bh.append(r
     with open (filename,'w') as f:
      json.dump(deta,f)    
    print (r) 
    print (deta)
def remove_sub():
 with open (filename) as file:
  data=json.load(file)
  pre=data["premium"]
  users=[]
  for h in pre:
   now=datetime.now(tz)
   #print (now)
   pd=h[1]
   days=h[2]
   ph_date = datetime.fromisoformat(pd)
   expiry_date = ph_date + timedelta(days=int(days))
   if expiry_date<now:
    id=h[0]
    remove_pro(id)
def get_pro_dt(h):
  with open(filename) as file:
    data = json.load(file)
    id=str(h)
    b = data["premium"]
    bb = [
      "{}".format(index1) for index1, value1 in enumerate(b)
      for index2, value2 in enumerate(value1) if value2 == id
    ]
    #print (bb)
    c = int(bb[0])
    p_date = b[c][1]
    id=b[c][0]
    ph_date = datetime.fromisoformat(p_date)
    days = b[c][2]
    r = f"Purchase Date{p_date} Validity {days}"
    expiry_date = ph_date + timedelta(days=int(days))
    current_time = datetime.now(tz)
    
    h =expiry_date-current_time

    print (h)
    format_string = "%Y-%m-%d %H:%M:%S"
    bh=h-timedelta(microseconds=h.microseconds)
    expiry_date=str(expiry_date.strftime('%m/%d/%Y'))
    purchase_date=str(ph_date.strftime('%m/%d/%Y'))
    days_left=str(bh)
    message = f'╒════════════════════════✰°\n ➥ Purchase Date :- {purchase_date}\n ➥ EXPIRY DATE :-  {expiry_date}\n ➥ TIME LEFT :-  {days_left} Hours\n°✰════════════════════════╛'
    return message 
