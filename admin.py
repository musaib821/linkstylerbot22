import json
import sqlite3
import database 
def admin_req(text)
 if text.startswith("/add_premium"):
  li=text.split()
  id=li[1]
  days=li[2]
 elif text.startswith("get_user_info"):
  li=text.split()
  id=li[1]
 elif text.startswith("remove_pro"):
  li=text.split()
  id=li[1]
 