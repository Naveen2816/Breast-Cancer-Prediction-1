from tkinter import *
import sqlite3
import datetime
import tkinter
from tkinter import messagebox
import PIL
from PIL import Image,ImageTk
import pyttsx3

def log_out():
    root = Tk()
    root.title("Survey Data Analysis")
    #root.config()
    root.state('z')
    root.resizable(0, 0)
    USERNAME = StringVar()
    PASSWORD = StringVar()

    #------------------------------------------AI VOICE-----------------------------------------------


    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[1].id)
    engine.setProperty('voice',voices[1].id)
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        #speak("I am Monika sir. Please tell me how can i help you")
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    if __name__=="__main__":
        wishMe()
        speak("HELLO i m Albina Welcome you in breast cancer prediction system developed by naveen and kartiik saini")

    # ==============================FRAMES=========================================
    Top = Frame(root, bd=2,relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    # ==============================BUTTON WIDGETS=================================
    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",(USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                window_3()
                USERNAME.set("")
                PASSWORD.set("")
#                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    #==========================================Database Create==========================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("maindata_2.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `member` (username, password) VALUES(2816001, 'admin')")
            conn.commit()

    #=============================================Calling another window============================

    def window_3():
        root.destroy()
        import  Nav3_Detection as win

        win.demo("opening breast cancer prediction system")

    # =======================================Exit function========================================

    def log_out0():
        qExit = tkinter.messagebox.askyesno("Breast Cancer Prediction", "Do you want to log out from the system")
        if qExit > 0:
            root.destroy()
            return

    #============================================Registration====================================

    def register_window():
        root.destroy()
        import Nav2_Registration as rf
        rf.log_out_1()
    # ==============================LABELS=========================================
    lbl_title = Label(Top, text="Breast Cancer Prediction",font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text="ID:", font=('arial', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    lblImage = Label(root, height=1000, width=1400, bd=0)
    lblImage.pack()
    img = Image.open("P41.jpg")
    photoImg = ImageTk.PhotoImage(img)
    # photoImg=PhotoImage(file="5948.jpg")
    lblImage["image"] = photoImg


    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)


    #=======================================Buttons============================
    btn_login = Button(Form,bg="red", text="Login", width=15, command=Login)
    btn_login.grid(row=3, column=0)
    btn_login.bind('<Return>', Login)

    btnExit = Button(Form,bg="red", text="Exit", width=15, command=log_out0)
    btnExit.grid(row=3, column=1)
    btnExit.bind('<Return>', Login)

    btnregister = Button(Form, bg="red", text="Registration", width=15, command=register_window)
    btnregister.grid(row=3, column=2)
    btnregister.bind('<Return>', Login)
    root.mainloop()
if __name__ == '__main__':
    log_out()
