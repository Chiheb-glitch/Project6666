from tkinter import *
import base64
import firebase_admin
from firebase_admin import credentials
import pyrebase
import time
from datetime import datetime
import os
from firebase_admin import firestore


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firebaseConfig = {
  'apiKey': "AIzaSyBeLb68tT5ux4dBKrGpeVeE5XjcrdZcRi4",
  'authDomain': "test-c835b.firebaseapp.com",
  'databaseURL': "https://test-c835b-default-rtdb.firebaseio.com",
  'projectId': "test-c835b",
  'storageBucket': "test-c835b.appspot.com",
  'messagingSenderId': "355005510230",
  'appId': "1:355005510230:web:c189ee21ff346fc844c1f7",
  'measurementId': "G-49871VRBEB"
}
db=firestore.client()


class account:
    def __init__(self,pas,user):
        self.pas=pas
        self.user=user



def btn_clicked(a,b):
    testcw=False
    i=0
    while(1):
        result=(db.collection('account').document(str(i)).get()).to_dict()
        
        if result==None:
            break

        user=result['user']
        pas=result['password']
        if (a.get()== user ) and (b.get()==pas):
            testcw=True
            
        
       

        i=i+1
    if testcw:
        print('good')
    else:
        print('wrong')
      
        

def login():
 window = Tk()

 window.geometry("931x490")
 window.configure(bg = "#2f3a8f")
 canvas = Canvas(
    window,
    bg = "#2f3a8f",
    height = 490,
    width = 931,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
 canvas.place(x = 0, y = 0)

 background_img = PhotoImage(file = f"background.png")
 background = canvas.create_image(
    475.5, 244.5,
    image=background_img)

 canvas.create_text(
    140.5, 245.5,
    text = "PASSWORD",
    fill = "#2f3a8f",
    font = ("RosarioRoman-SemiBold", int(30.0)))

 entry0_img = PhotoImage(file = f"img_textBox0.png")
 entry0_bg = canvas.create_image(
    222.5, 171.5,
    image = entry0_img)

 entry0 = Entry(
    bd = 0,
    font=("Andalus",20,'bold'),
    bg = "#feece9",
    highlightthickness = 0)

 entry0.place(
    x = 85.5, y = 142,
    width = 274.0,
    height = 57)

 entry1_img = PhotoImage(file = f"img_textBox1.png")
 entry1_bg = canvas.create_image(
    222.5, 302.5,
    image = entry1_img)

 entry1 = Entry(
    show='*',
    bd = 0,
    bg = "#feece9",
    font=("Andalus",24,'bold'),
    highlightthickness = 0)

 entry1.place(
    x = 85.5, y = 273,

    width = 274.0,
    height = 57)

 canvas.create_text(
    113.5, 115.5,
    text = "USER_ID",
    fill = "#2f3a8f",
    font = ("RosarioRoman-SemiBold", int(30.0)))


 img0 = PhotoImage(file = f"img0.png")
 b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked(entry0,entry1),
    relief = "flat")

 b0.place(
    x = 75, y = 368,
    width = 138,
    height = 69)


 window.resizable(False, False)
 window.mainloop()


login()
