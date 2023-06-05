import sqlite3 
from text import account as ac
import datetime 
#from datetime import * 
#from datetime import datetime, timedelta
import json
import ast
def add_user(user_id):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key support

    # Create a table if it doesn't exist
    create_table = '''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            channels TEXT ,
            plan TEXT DEFAULT 'FREE',
            purchase_date DATE DEFAULT 'N.A',
            Expiry_date DATE DEFAULT 'N.A',
            days INTEGER DEFAULT 0,
            free_trail INTEGER DEFAULT 0 
            
        );
    '''
    conn.execute(create_table)

    # Check if the user_id already exists
    check_query = "SELECT user_id FROM users WHERE user_id = ?"
    check_cursor = conn.cursor()
    check_cursor.execute(check_query, (user_id,))
    existing_user = check_cursor.fetchone()
    check_cursor.close()

    if existing_user:
        print("User already present")
    else:
        # Insert the new user_id into the table
        insert_query = "INSERT INTO users (user_id) VALUES (?)"
        insert_cursor = conn.cursor()
        insert_cursor.execute(insert_query, (user_id,))
        conn.commit()
        insert_cursor.close()
        print("User added successfully")

    # Fetch the count of user_ids in the table
   # count_query = "SELECT COUNT(user_id) FROM users"
   # count_cursor = conn.cursor()
    #count_cursor.execute(count_query)
  #  count = count_cursor.fetchone()[0]
   # count_cursor.close()

  #  print(f"Total user IDs in the table: {count}")

    # Close the connection
    conn.close()
#import sqlite3

def add_channel(user_id, channel):
    # Connect to the database
     conn = sqlite3.connect('database.db')
  #  conn.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key support

    # Check if the user_id already exists
    #check_query = "SELECT user_id FROM users WHERE user_id = ?"
   # check_cursor = conn.cursor()
   # check_cursor.execute(check_query, (user_id,))
 #  ₹ existing_user = check_cursor.fetchone()
  #  check_cursor.close()

    #if existing_user:
     l_p=conn.cursor()
     l_p.execute(f"SELECT channels,plan FROM users WHERE user_id=?", (user_id, )) 
     ps=l_p.fetchone() 
        #pus=l_p.fetchall()
     #print("This Is From Database")
       # print(ps[0])
    # pre=ps[1]
     print (ps[0])
     try:
      s=ast.literal_eval(ps[0]) 
     except :
        s=[] 
     if ps=='FREE' and len(s)>=2:
      #print ("Join Premium To Add More Links") 
      return "limited "
     channels=[channel]
     if channel in s :
       print( "Already added") 
       return "Already "
     else:
         for ch in s :
            channels.append(ch) 
         string=str(channels)
         update_query = "UPDATE users SET channels = ? WHERE user_id = ?"
         update_cursor = conn.cursor()
         update_cursor.execute(update_query, (string, user_id))
         conn.commit()
         update_cursor.close()
         print("Channel added/updated successfully")
   # else:
     #   print("User not found in the database")

    # Close the connection
     conn.close()
def fetch_channel(id,check=False):
 conn=sqlite3.connect('database.db')
 fetch_query="SELECT channels FROM users WHERE user_id=? "
 fetch_cursor=conn.cursor()
 fetch_cursor.execute(fetch_query, (id,))
 channel=fetch_cursor.fetchone()
# print (channel)
 fetch_cursor.close()
 conn.close()  
 if channel[0]==None: 
   if check==True: 
    li=[]
   # print (len(li)) 
    
    return len(li)
   return [] 
 else :
  # print(type(channel[0]))
   li=ast.literal_eval(channel[0])
   if check==True:
   # print (len(li)) 
    
    return len(li)
  #print("This Is List")
  # print(li) 
   return li
def add_pro (id,days,plan=False):
  days=int(days) 
  print (plan)
  n_date=datetime.datetime.now()
  p_date=n_date.strftime("%d-%m-%Y")
 # print(p_date)
  conn = sqlite3.connect('database.db')
  cr=conn.cursor()
  old_data=f" SELECT Expiry_date FROM users WHERE user_id=? "
  cr.execute(old_data,(id, ))
  s=cr.fetchone() 
  cr.close()
  print(s)
  if s[0]=='N.A':
     # print("It's Zero")
      d_cr=conn.cursor ()
      new_date=n_date + datetime.timedelta(days=days)
      uii=new_date.strftime("%d-%m-%Y")
     # print(f"uii = {uii}")
     # print (f"p Date ={p_date}")
      update_days=f"UPDATE users SET Expiry_date=?,purchase_date=?, plan ='PREMIUM' WHERE user_id =? "
      d_cr.execute(update_days, (uii,p_date,id,))
      if plan==True:
       exetrail=conn.cursor()
       exetrail.execute(f"UPDATE users SET free_trail=? WHERE user_id=?",(1,id,))
     #  print ("Free Trail Given")
       conn.commit()
       exetrail.close()
      conn.commit() 
     # py=conn.cursor()
     # py.execute(f"SELECT Expiry_date , purchase_date FROM users WHERE user_id = ?",(id,))
      d_cr.close()
      conn.close()
     # print (" updated successfully ")
  else :
     #  print ("already pro as ")
     #  print (s[0])
       d_cr=conn.cursor ()
      
       total_dys=datetime.datetime.strptime(s[0],"%d-%m-%Y")
       tds=total_dys.strftime("%d-%m-%Y")   
       print(f"total {total_dys} \n New Line {tds}")
      # ₹datetime_object = datetime.strptime(
       total_days=datetime.datetime.strptime(tds,"%d-%m-%Y")+datetime.timedelta(days=days)
       print (total_days) 
       tdys=total_days.strftime("%d-%m-%Y")
       print (tdys)
       update_days=f"UPDATE users SET Expiry_date=?,purchase_date=? WHERE user_id =? "
       d_cr.execute(update_days, (tdys,p_date,id,))
       conn.commit()
       d_cr.close()
       conn.close() 
def fetch_channel(id,check=False):
 conn=sqlite3.connect('database.db')
 fetch_query="SELECT channels FROM users WHERE user_id=? "
 fetch_cursor=conn.cursor()
 fetch_cursor.execute(fetch_query, (id,))
 channel=fetch_cursor.fetchone()
# print (channel)
 fetch_cursor.close()
 conn.close()  
 if channel[0]==None: 
   if check==True: 
    li=[]
   # print (len(li)) 
    
    return len(li)
   return [] 
 else :
  # print(type(channel[0]))
   li=ast.literal_eval(channel[0])
   if check==True:
   # print (len(li)) 
    
    return len(li)
  #print("This Is List")
  # print(li) 
   return li
def dec_pro (id,days):
  days=int(days) 
  #print (plan)
  n_date=datetime.datetime.now()
  p_date=n_date.strftime("%d-%m-%Y")
 # print(p_date)
  conn = sqlite3.connect('database.db')
  cr=conn.cursor()
  old_data=f" SELECT Expiry_date FROM users WHERE user_id=? "
  cr.execute(old_data,(id, ))
  s=cr.fetchone() 
  cr.close()
  print(s)
  if s[0]=='N.A':
     # print("It's Zero")
      d_cr=conn.cursor ()
      new_date=n_date - datetime.timedelta(days=days)
      uii=new_date.strftime("%d-%m-%Y")
     # print(f"uii = {uii}")
     # print (f"p Date ={p_date}")
      update_days=f"UPDATE users SET Expiry_date=?,purchase_date=?, plan ='PREMIUM' WHERE user_id =? "
      d_cr.execute(update_days, (uii,p_date,id,))
      #if plan==True:
       #exetrail=conn.cursor()
       #exetrail.execute(f"UPDATE users SET free_trail=? WHERE user_id=?",(1,id,))
     #  print ("Free Trail Given")
       #conn.commit()
      # exetrail.close()
      conn.commit() 
     # py=conn.cursor()
     # py.execute(f"SELECT Expiry_date , purchase_date FROM users WHERE user_id = ?",(id,))
      d_cr.close()
      conn.close()
     # print (" updated successfully ")
  else :
     #  print ("already pro as ")
     #  print (s[0])
       d_cr=conn.cursor ()
      
       total_dys=datetime.datetime.strptime(s[0],"%d-%m-%Y")
       tds=total_dys.strftime("%d-%m-%Y")   
       print(f"total {total_dys} \n New Line {tds}")
      # ₹datetime_object = datetime.strptime(
       total_days=datetime.datetime.strptime(tds,"%d-%m-%Y")-datetime.timedelta(days=days)
       print (total_days) 
       tdys=total_days.strftime("%d-%m-%Y")
       print (tdys)
       update_days=f"UPDATE users SET Expiry_date=?,purchase_date=? WHERE user_id =? "
       d_cr.execute(update_days, (tdys,p_date,id,))
       conn.commit()
       d_cr.close()
       conn.close() 
def fetch_user_details (id):
    conn = sqlite3.connect('database.db')
    f=conn.cursor() 
    f.execute(f" SELECT plan ,Expiry_date ,purchase_date,channels FROM users WHERE user_id={id}")
    result =f.fetchone()
   # print (result )
    plan,e_data,p_data,channel=result
   # print(type(channel))
    if channel==None:
    # print ("No Channels Found")
     channel=0
    else :
     channel=len(ast.literal_eval(channel))
   # print("New Added Data")
    
  #  print(result) 
   # g=ac.format(result[0], result [1], result [2])
   # print (g)
    return [plan,p_data,e_data,channel]
def auto_remove():
    conn=sqlite3.connect('database.db')
    now =datetime.datetime.now()
    fr=now.strftime("%d-%m-%Y")
   # onn=sqlite3.connect('database.db')
    fetch_query="SELECT user_id ,Expiry_date FROM users "
    fetch_cursor=conn.cursor()
    fetch_cursor.execute(fetch_query)
    channel=fetch_cursor.fetchall()
    user_id=[] 
   # print("Users To Remove "+str(user_id))
    
  #  print(channel)
    for i in channel : 
     if i[1]=='N.A':
         pass 
     else:
      date1 = datetime.datetime.strptime(i[1], '%d-%m-%Y')
      date2 = datetime.datetime.strptime(fr, '%d-%m-%Y')
   #  print(i[1])
   #  print(type(date2))
      if date2>date1 :
    #  
       print("ues")
      else :
         print ("no")
      u=datetime.datetime.strptime(i[1],"%d-%m-%Y")#+ datetime.timedelta(days=30)
    # ud=datetime.datetime.strptime(, "%Y-%m-%d").date()
      if u<now:
        # print("yes it is ")
         tor=conn.cursor() 
         user_id.append(i[0])
         #idd=conn.cursor()f
         rt=f"UPDATE users SET Expiry_date=?, purchase_date=?,plan=? WHERE user_id={i[0]}"
         #idd.execute("SELECT user_id FROM users WHERE ")
         tor.execute(rt,('N.A','N.A','FREE')) 
         
         conn.commit()
         tor.close()
        
     #print(channel)
    return user_id 
def notify_users_3 ():
    conn=sqlite3.connect('database.db')
    now =datetime.datetime.now()+datetime.timedelta(days=3)
    #print(now) 
    fr=now.strftime("%d-%m-%Y") 
   # print(fr)
   # onn=sqlite3.connect('database.db')
    fetch_query="SELECT user_id FROM users WHERE Expiry_date=?"
    fetch_cursor=conn.cursor()
    fetch_cursor.execute(fetch_query,(fr,))
    ids=fetch_cursor.fetchall()
  #  print("These are ids")
   # print(ids)
    #print (len(ids))
    users=[]
    if len(ids)==0:
     return 
    else: 
     for i in ids :
      users.append(i[0])
     #print(users)
     return users 
def check_for_pre(id):
    conn = sqlite3.connect('database.db')
    f=conn.cursor() 
    f.execute(f" SELECT plan FROM users WHERE user_id={id}")
    result =f.fetchone()
    
    result=result[0]
    print (result) 
    if result=='FREE': 
       # print()
        return False
    elif result=='PREMIUM':
        return True
def check_for_trail(id):
    conn = sqlite3.connect('database.db')
    f=conn.cursor() 
    f.execute(f" SELECT free_trail FROM users WHERE user_id={id}")
    result =f.fetchone()
    
    result=result[0]
    print (result) 
    if result==0: 
       # print()
        return False
    elif result==1:
        return True

def remove_channel(id,channel):
    conn = sqlite3.connect('database.db')
    f=conn.cursor() 
    f.execute(f" SELECT channels FROM users WHERE user_id={id}")
    result =f.fetchone()
    print (result)
    s=ast.literal_eval(result[0])
    print(f"channels are {s} amd channel is {channel}")
    
    s.remove(int(channel))
    ss=str(s)
    add=conn.cursor()
    add.execute(f"UPDATE users SET channels=?  WHERE user_id={id}",(ss,))
    print ("DELETED")
    conn.commit()
    add.close()
    conn.close()
    # u=datetime.datetime.strptime(i[1],"%d-%m-%Y")#+ datetime.timedelta(days=30)
     #s=u-now
def get_user_ids(check=False):
    conn=sqlite3.connect('database.db')
    f=conn.cursor()
    f.execute(f"SELECT user_id FROM users")
    result=f.fetchall()
    #print (result )
    users=[]
    for i in result :
    # print (i[0])
     users.append(i[0])
  #  print (users) 
    if check==True:
        return (len(users))
    return users 
def remove_pro(id):
    conn=sqlite3.connect('database.db')
    tor=conn.cursor() 
        # user_id.append(i[0])
         #idd=conn.cursor()f
    rt=f"UPDATE users SET Expiry_date=?, purchase_date=?,plan=? WHERE user_id={id}"
         #idd.execute("SELECT user_id FROM users WHERE ")
    tor.execute(rt,('N.A','N.A','FREE')) 
         
    conn.commit()
    tor.close()
    conn.close() 
    