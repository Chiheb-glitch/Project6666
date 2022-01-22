from tkinter import *


def btn_clicked():
    print(entry0.get())


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
    140.5, 257.5,
    text = "PASSWORD",
    fill = "#2f3a8f",
    font = ("RosarioRoman-SemiBold", int(30.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    222.5, 171.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
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
    bd = 0,
    bg = "#feece9",
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
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 75, y = 368,
    width = 138,
    height = 69)

window.resizable(False, False)
window.mainloop()
