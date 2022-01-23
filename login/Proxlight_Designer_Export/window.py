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





      
        
def btn_clicked():
     testcw=False
     i=0
     test1=entry0.get()
     test2=entry1.get()
     entry1.delete(0,END)
     entry0.delete(0,END)
    
 
     while(1):
        result=(db.collection('account').document(str(i)).get()).to_dict()
        #print(a,b)
        if result==None:
            break

        user=result['user']
        pas=result['password']
        if (test1== user ) and (test2==pas):
            testcw=True
            
        
       

        i=i+1
    
     if testcw:
        print('good')
        window.destroy()
        main_page(test1)
     else:
        print('wrong')




 
def login():
 global window  
 window = Tk()
 global entry0
 global entry1
 entry0=str()
 entry1=str()
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

 background_img = PhotoImage(file = f"backgroundlogin.png")
 background = canvas.create_image(
    475.5, 244.5,
    image=background_img)

 canvas.create_text(
    140.5, 245.5,
    text = "PASSWORD",
    fill = "#2f3a8f",
    font = ("RosarioRoman-SemiBold", int(30.0)))

 entry0_img = PhotoImage(file = f"img_textBox0login.png")
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

 entry1_img = PhotoImage(file = f"login.png")
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

 
 
 img0 = PhotoImage(file = f"img0login.png")
 b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

 b0.place(
    x = 75, y = 368,
    width = 138,
    height = 69)


 window.resizable(False, False)

 window.mainloop()
def my_upd_0():
    print('0')
    if b0['bd']==0:
        b0.config(image=active,bd=1)

    else :
        b0.config(image=inactive,bd=0)
def my_upd_1():
    print('1')
    if b1['bd']==0:
        b1.config(image=active,bd=1)

    else :
        b1.config(image=inactive,bd=0)
def my_upd_2():
    print('2')
    if b2['bd']==0:
        b2.config(image=active,bd=1)

    else :
        b2.config(image=inactive,bd=0)
def my_upd_3():
    print('3')
    if b3['bd']==0:
        b3.config(image=active,bd=1)

    else :
        b3.config(image=inactive,bd=0)
def my_upd_4():
    print('4')
    if b4['bd']==0:
        b4.config(image=active,bd=1)

    else :
        b4.config(image=inactive,bd=0)

def my_upd_5():
    print('5')
    if b5['bd']==0:
        b5.config(image=active,bd=1)

    else :
        b5.config(image=inactive,bd=0)
def my_upd_6():
    print('6')
    if b6['bd']==0:
        b6.config(image=active,bd=1)

    else :
        b6.config(image=inactive,bd=0)
def my_upd_7():
    print('7')
    if b7['bd']==0:
        b7.config(image=active,bd=1)

    else :
        b7.config(image=inactive,bd=0)
def my_upd_8():
    print('8')
    if b8['bd']==0:
        b8.config(image=active,bd=1)

    else :
        b8.config(image=inactive,bd=0)
def my_upd_9():
    print('9')
    if b9['bd']==0:
        b9.config(image=active,bd=1)

    else :
        b9.config(image=inactive,bd=0)
 
def main_page(x):
 window = Tk()
 global active
 global inactive
 active = PhotoImage(file = f"img10.png")
 inactive=  PhotoImage(file = f"imgr.png")
 window.geometry("1355x691")
 window.configure(bg = "#325288")
 canvas = Canvas(
    window,
    bg = "#325288",
    height = 691,
    width = 1355,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
 canvas.place(x = 0, y = 0)
 
 canvas.create_text(
    1290.0, 38.0,
    text = 'Hi   '+x,
    fill = "#ffffff",
    font = ("None", int(17.0)))

 background_img = PhotoImage(file = f"background.png")
 background = canvas.create_image(
    702.5, 378.0,
    image=background_img)

 img0 = PhotoImage(file = f"img0.png")
 global b0
 global b1
 global b2
 global b3
 global b4
 global b5
 global b6
 global b7
 global b8
 global b9

 b0 = Button(
    bd=0,
    image = active,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_0(),
    relief = "flat")

 b0.place(
    x = 1099, y = 334,
    width = 120,
    height = 48)

 img1 = PhotoImage(file = f"img1.png")
 b1 = Button(
    bd=0,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_1(),
    relief = "flat")

 b1.place(
    x = 1097, y = 275,
    width = 120,
    height = 48)

 img2 = PhotoImage(file = f"img2.png")
 b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_2(),
    relief = "flat")

 b2.place(
    x = 1097, y = 217,
    width = 120,
    height = 48)

 img3 = PhotoImage(file = f"img3.png")
 b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_3(),
    relief = "flat")

 b3.place(
    x = 1097, y = 160,
    width = 120,
    height = 48)

 img4 = PhotoImage(file = f"img4.png")
 b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_4(),
    relief = "flat")

 b4.place(
    x = 1097, y = 97,
    width = 120,
    height = 48)

 img5 = PhotoImage(file = f"imgr.png")




 img5 = PhotoImage(file = f"img6.png")
 b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_5(),
    relief = "flat")

 b5.place(
    x = 430, y = 97,
    width = 120,
    height = 48)

 img6 = PhotoImage(file = f"img7.png")
 b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_6(),
    relief = "flat")

 b6.place(
    x = 430, y = 272,
    width = 120,
    height = 48)

 img7 = PhotoImage(file = f"img8.png")
 b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_7(),
    relief = "flat")

 b7.place(
    x = 424, y = 220,
    width = 120,
    height = 48)

 entry0_img = PhotoImage(file = f"img_textBox0.png")
 entry0_bg = canvas.create_image(
    994.0, 129.0,
    image = entry0_img)

 entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry0.place(
    x = 891, y = 111,
    width = 206,
    height = 34)

 entry1_img = PhotoImage(file = f"img_textBox1.png")
 entry1_bg = canvas.create_image(
    994.0, 190.0,
    image = entry1_img)

 entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry1.place(
    x = 891, y = 172,
    width = 206,
    height = 34)

 entry2_img = PhotoImage(file = f"img_textBox2.png")
 entry2_bg = canvas.create_image(
    994.0, 247.0,
    image = entry2_img)

 entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry2.place(
    x = 891, y = 229,
    width = 206,
    height = 34)

 entry3_img = PhotoImage(file = f"img_textBox3.png")
 entry3_bg = canvas.create_image(
    994.0, 304.0,
    image = entry3_img)

 entry3 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry3.place(
    x = 891, y = 286,
    width = 206,
    height = 34)

 entry4_img = PhotoImage(file = f"img_textBox4.png")
 entry4_bg = canvas.create_image(
    994.0, 366.0,
    image = entry4_img)

 entry4 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry4.place(
    x = 891, y = 348,
    width = 206,
    height = 34)

 entry5_img = PhotoImage(file = f"img_textBox5.png")
 entry5_bg = canvas.create_image(
    327.0, 127.0,
    image = entry5_img)

 entry5 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry5.place(
    x = 224, y = 109,
    width = 206,
    height = 34)

 entry6_img = PhotoImage(file = f"img_textBox6.png")
 entry6_bg = canvas.create_image(
    327.0, 188.0,
    image = entry6_img)

 entry6 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry6.place(
    x = 224, y = 170,
    width = 206,
    height = 34)

 entry7_img = PhotoImage(file = f"img_textBox7.png")
 entry7_bg = canvas.create_image(
    327.0, 245.0,
    image = entry7_img)

 entry7 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry7.place(
    x = 224, y = 227,
    width = 206,
    height = 34)

 entry8_img = PhotoImage(file = f"img_textBox8.png")
 entry8_bg = canvas.create_image(
    327.0, 302.0,
    image = entry8_img)

 entry8 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry8.place(
    x = 224, y = 284,
    width = 206,
    height = 34)

 entry9_img = PhotoImage(file = f"img_textBox9.png")
 entry9_bg = canvas.create_image(
    327.0, 364.0,
    image = entry9_img)

 entry9 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry9.place(
    x = 224, y = 346,
    width = 206,
    height = 34)

 entry10_img = PhotoImage(file = f"img_textBox10.png")
 entry10_bg = canvas.create_image(
    994.0, 423.0,
    image = entry10_img)

 entry10 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry10.place(
    x = 891, y = 405,
    width = 206,
    height = 34)

 entry11_img = PhotoImage(file = f"img_textBox11.png")
 entry11_bg = canvas.create_image(
    327.0, 426.0,
    image = entry11_img)

 entry11 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

 entry11.place(
    x = 224, y = 408,
    width = 206,
    height = 34)

 img8 = PhotoImage(file = f"img9.png")
 b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_8(),
    relief = "flat")

 b8.place(
    x = 430, y = 335,
    width = 120,
    height = 48)



 img9 = PhotoImage(file = f"img12.png")
 b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:my_upd_9(),
    relief = "flat")

 b9.place(
    x = 430, y = 157,
    width = 120,
    height = 48)

 canvas.create_text(
    200.5, 131.0,
    text = "RS ",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    200.5, 195.5,
    text = "TFP",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    155.5, 245.0,
    text = "FOPROLOS",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    182, 300.0,
    text = "TVA",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    189.5, 360.0,
    text = "TCL",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
   859.0, 129.0,
    text = "DC",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    769.0, 189.0,
    text = "AUTRES TAXES/CA",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    789.5, 245.0,
    text = "TAXE HOTELIERE",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    810.5, 300.0,
    text = "D.LICENCE",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    768.0, 365.5,
    text = "DROIT DE TIMBRE",
    fill = "#000000",
    font = ("Inter-Medium", int(17.0)))

 canvas.create_text(
    118.0, 430.5,
    text = "JOUR D ENTREE EN PENALITE",
    fill = "#000000",
    font = ("Inter-Bold", int(12.0)))

 canvas.create_text(
    769.5, 425.0,
    text = "DATE DE PAEMENT",
    fill = "#000000",
    font = ("Inter-Bold", int(15.0)))

 canvas.create_text(
    328.0, 577.5,
    text = "PENALITES=",
    fill = "#000000",
    font = ("Inter-Bold", int(20.0)))

 canvas.create_text(
    946.0, 577.5,
    text = "TOTAL A PAYER =",
    fill = "#000000",
    font = ("Inter-Bold", int(20.0)))

 canvas.create_text(
    640.0, 35.5,
    text = "CALCULE PENALITE DE RETARD DECLARATIONS MENSUELLES",
    fill = "#ffffff",
    font = ("Inter-Medium", int(24.0)))

 window.resizable(False, False)
 window.mainloop()
login()