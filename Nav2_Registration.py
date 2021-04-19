from tkinter import *
import sqlite3
import datetime
import tkinter
from tkinter import messagebox
import PIL
from PIL import Image,ImageTk
import pyttsx3

def log_out_1():
    root = Tk()
    root.title("Survey Data Analysis")
    #root.config()
    root.state('z')
    root.resizable(0, 0)
    USERNAME = StringVar()
    PASSWORD = StringVar()
    Name = StringVar()
    Age = StringVar()
    Phone = StringVar()

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
        speak("hELLO i m Albina Welcome you in breast cancer prediction system developed by naveen and kartiik saini")

    # ==============================FRAMES=========================================
    Top = Frame(root, bd=2,relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    # ==============================BUTTON WIDGETS=================================
    def register(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "" and Name.get() =="" and Phone.get()=="" and Age.get()=="":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",(USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                messagebox.showinfo("Information", "Registration Successful")
                root.destroy()
                import Login as lg
                lg.log_out()
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
        conn = sqlite3.connect("maindata.db")
        cursor = conn.cursor()
        #cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        #cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
        #if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES(?,?)",(username.get(),password.get()))
        conn.commit()

    #===============================================back===================================

    def back():
        back = tkinter.messagebox.askyesno("Breast Cancer Prediction", "Do you want to back?")
        if (back == True):
            root.destroy()
            import Nav1_Login as lg
            lg.log_out()

    # ==============================LABELS=========================================
    lbl_title = Label(Top, text="Breast Cancer Prediction", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_name = Label(Form, text="Name:", font=('arial', 10), bd=15)
    lbl_name.grid(row=0, column=0)
    lbl_age = Label(Form, text="Age:", font=('arial', 10), bd=15)
    lbl_age.grid(row=1, column=0)
    lbl_username = Label(Form, text="ID*:", font=('arial', 10), bd=15,fg="red")
    lbl_username.grid(row=2, column=0)
    lbl_password = Label(Form, text="Password*:", font=('arial', 10), bd=15,fg="red")
    lbl_password.grid(row=3, column=0)
    lbl_phone = Label(Form, text="Phone No.:", font=('arial', 10), bd=15)
    lbl_phone.grid(row=4, column=0)
    lbl_text = Label(Form)
    lbl_text.grid(row=5, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    name = Entry(Form, textvariable=Name, font=14)
    name.grid(row=0, column=1)
    age = Entry(Form, textvariable=Age, font=14)
    age.grid(row=1, column=1)
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=2, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=3, column=1)
    phone = Entry(Form, textvariable=Phone, font=14)
    phone.grid(row=4, column=1)

    #=======================================Buttons============================
    btn_register = Button(Form,bg="red", text="Register", width=15, command=register)
    btn_register.grid(row=6, columnspan=2)
    btn_register.bind('<Return>', register)

    btnback = Button(Form, bg="red", text="Back", width=15, command=back)
    btnback.grid(row=6, column=3)
    btnback.bind('<Return>',back)

    root.mainloop()
if __name__ == '__main__':
    log_out_1()
