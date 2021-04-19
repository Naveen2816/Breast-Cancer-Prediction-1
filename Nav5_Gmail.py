import smtplib
import email.mime.multipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import tkinter
from tkinter import *
import tkinter.messagebox as box
from tkinter import ttk

global ephone,eage,eaddress,ename

#===================================================Send Email=======================================

def SendEmail():
    v1 = ephone.get()
    v2 = ename.get()
    v3 = eaddress.get()
    v4 = eage.get()
    if (ephone.get()!="" and ename.get()!="" and eaddress.get()!="" and eage.get!="" and v1.isdigit()==True and
            v2.isalpha()==True and v4.isdigit()==True):
        if (len(v1)<=12 or len(v1)==10 and len(v1!=11)):
        #Create Email Details
            msgMultiPart=email.mime.multipart.MIMEMultipart()
            msgMultiPart["subject"]="Appointment Notification"
            msgMultiPart["From"]="nvnpunia001@gmail.com"
            msgMultiPart["To"]=etxtTo.get()
            #Create Body may be plain or html
            body="Dear Sir I want a appointment, My name is "+ename.get()+"\n"+ "My age is "+eage.get()+"\n"+"My Phone Number is "+ephone.get()+"\n"+"I m from "+eaddress.get()
            msgMultiPart.attach(MIMEText(body,'plain'))

            smtpobj=smtplib.SMTP(host="smtp.gmail.com",port=587)

            smtpobj.starttls()
            smtpobj.login("nvnpunia001@gmail.com","8222050457")
            smtpobj.sendmail("nvnpunia001@gmail.com",etxtTo.get(),msgMultiPart.as_string())
            box.showinfo("Info","Email send successfully")
            root.destroy()
            print("Sucess")
        else:
            box.showerror("Error","Please enter the valid phone number")
    else:
        box.showerror("Warning","Please fill all the required entry in correct way")
#=========================================Back function for doctor list================================

def back():
    root.destroy()
    import Nav4_Doctorlist_1 as dc_1
    dc_1.doctor_appointment("please wait, Opening list of best doctors for breast cancer treatment")

#=================================================================================================================

def GMIL():
    global root
    global To
    global etxtTo,e,ename,eaddress,eage,ephone
    root=Tk()
    root.title("Gmail")
    root.config(bg="pink")
    root.state('z')

    #=================================================Frame============================================================

#    Tops0 = Frame(root, width=1380, height=1000, bg="white", bd=0, relief="raise")
#    Tops0.place(x=0, y=0)
    Tops = Frame(root, width=1400, height=90, bg="blue", relief="raise")
    Tops.pack(side=TOP)

    #======================================================Variable==================================================

    To=StringVar()
    Name=StringVar()
    Age=StringVar()
    Phone=StringVar()
    Address=StringVar()

    #=========================================================Labels========================================================

    lblFrom = Label(Tops, text="From", font=('aria', 16, 'bold'),bg="blue", fg="black", bd=20).grid(row=0, column=0)
    lblTo = Label(Tops, text="To", font=('aria', 16, 'bold'),height=2,bg="blue", fg="black", bd=20).grid(row=1, column=0)
    lblFrom1 = Label(Tops, text="nvnpunia001@gmail.com", font=('aria', 16, 'bold'),bg="blue" ,bd=16, width=30, justify='left')
    lblFrom1.grid(row=0, column=1)

    lblName = Label(Tops, text="Name", font=('aria', 16, 'bold'), bg="blue", fg="black", bd=20).grid(row=2, column=0)
    lblFrom = Label(Tops, text="Age", font=('aria', 16, 'bold'), bg="blue", fg="black", bd=20).grid(row=3, column=0)
    lblFrom = Label(Tops, text="Phone No.", font=('aria', 16, 'bold'), bg="blue", fg="black", bd=20).grid(row=4, column=0)
    lblFrom = Label(Tops, text="Address", font=('aria', 16, 'bold'), bg="blue", fg="black", bd=20).grid(row=5, column=0)

    #======================================================Text Part=======================================================
    etxtTo = Entry(Tops,textvariable=To, font=('aria', 16, 'bold'), width=30, justify='left')
    etxtTo.grid(row=1, column=1)
    ename = Entry(Tops, textvariable=Name, font=('aria', 16, 'bold'), width=30, justify='left')
    ename.grid(pady=20,row=2, column=1)
    eage = Entry(Tops, textvariable=Age, font=('aria', 16, 'bold'), width=30, justify='left')
    eage.grid(pady=20,row=3, column=1)
    ephone = Entry(Tops, textvariable=Phone, font=('aria', 16, 'bold'), width=30, justify='left')
    ephone.grid(pady=20,row=4, column=1)
    ephone.insert(0,"91")
    eaddress = Entry(Tops, textvariable=Address, font=('aria', 16, 'bold'), width=30, justify='left')
    eaddress.grid(pady=20,row=5, column=1)


    #=======================================================Button=======================================================

    btnSendMail = ttk.Button(Tops, text='Send Mail',width=15,command=SendEmail)
    btnSendMail.grid(row=6, column=1)
    btnback=ttk.Button(Tops,text="Back",width=15,command=back)
    btnback.grid(row=6,column=2)
    root.mainloop()
if __name__=="__main__":
    GMIL()