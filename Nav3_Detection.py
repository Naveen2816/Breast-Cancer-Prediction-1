import csv
from tkinter import messagebox

import tkinter.messagebox as box
from tkinter import *
from tkinter import ttk
import tkinter

from PIL import ImageTk, Image

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

cancer = pd.read_csv('newcancer_Data.csv')
print(cancer.columns)

print("dimension of cancer data: {}".format(cancer.shape))

"""preparing data for Deployment model"""
features_x = ['radius_worst',
              'texture_worst',
              'perimeter_worst',
              'area_worst',
              'smoothness_worst',
              'compactness_worst',
              'concavity_worst',
              'concave points_worst',
              'symmetry_worst',
              'fractal_dimension_worst',
              'concavity_se',
              'area_se',
              'concave points_mean',
              'texture_mean', ]
feature_y = ['diagnosis']

x = cancer[features_x]
y = cancer[feature_y]


from sklearn.model_selection import train_test_split


X_train,y_train,X_test,y_test=train_test_split(x,y,)
# ### Logistic Regression

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x, np.array(y))

#print(lr.predict(x))
#pickle.save(lr,open('logistic_regression.sav','wb'))

#print(lr)

#-------------------------------------------------------Main root window start--------------------------

def demo(audio):
    engine.say(audio)
    engine.runAndWait()
    # global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14
    root = Tk()

    root.configure(background='pink')

    root.title("CANCER PREDICTION")

    root.state("z")

    Tops = Frame(root, width=1360, height=50, bg="blue", bd=8, relief="raise")
    Tops.pack(side=TOP)

    f2 = Frame(root, width=300, height=600, bd=8, bg="Blue", relief="raise")
    f2.pack(side=RIGHT)

# -------------------------------------------------Scrollbar------------------------------------------------

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), background='steel blue', width=1155, height=600)

    fla = Frame(root, width=600, height=200, bd=11, bg="Blue", relief="raise")
    fla.pack(side=TOP)
    # myframe = Frame(root, width=600, height=200, bd=11, bg="blue", relief="raise")
    # myframe.pack(side=TOP)

    canvas = Canvas(fla)
    frame = Frame(canvas, bg='Blue')
    myscrollbar = Scrollbar(fla, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set, background='steel blue')

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((100, 100), window=frame, anchor='nw')
    frame.bind("<Configure>", myfunction)

# -------------------------------------------------------------------------------------------------------

    lblinfo = Label(Tops, font=('algerian', 35, 'bold'), width=44, text="Breast Cancer Prediction", fg="Black",
                    bg="sky blue", bd=10)
    lblinfo.grid(row=0, column=0)

# --------------------------------------Reset Function-----------------------------------------------

    def Reset():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)
        e13.delete(0, END)
        e14.delete(0, END)
        e15.delete(0, END)
        e16.delete(0, END)
        e17.delete(0, END)
        e18.delete(0, END)
        e19.delete(0, END)

#-----------------------------------------------Save Data--------------------------------------------

    def save():
        b1=e15.get()
        b2=e16.get()
        b3=e17.get()
        b4=e18.get()
        b5=e19.get()

        if (len(b3)<=12 and len(b3)==10):

            if (b1.isdigit()==True and b2.isalpha()==True and b3.isdigit()==True and b5.isdigit()==True):
                s15 = e15.get()
                s16 = e16.get()
                s17 = e17.get()
                s18 = e18.get()
                s19 = e19.get()

                s1 = e1.get()
                s2 = e2.get()
                s3 = e3.get()
                s4 = e4.get()
                s5 = e5.get()
                s6 = e6.get()
                s7 = e7.get()
                s8 = e8.get()
                s9 = e9.get()
                s10 = e10.get()
                s11 = e11.get()
                s12 = e12.get()
                s13 = e13.get()
                s14 = e14.get()
                s20 = e20.get()

                myData = (s15,s16,s17,s18,s19,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s20)

                # results=[]

                with open('New_cancer_File.csv', 'a') as myFile:
                    writer = csv.writer(myFile)
                    # myData.add(writer)
                    writer.writerow(myData)
                messagebox.showinfo("Save","Data is successfully saved")
                #print(myData)
            else:
                messagebox.showerror("Warning","Incorrect format of Patient information data please correct it")
        elif (e15.get() == "" and e16.get() == "" and e17.get() == "" and e18.get() == "" and e19.get() == ""):
            messagebox.showerror("Error", "Patient Information field are empty")
        else:
            messagebox.showerror("Warning","Please enter the valid phone number and fill all field")
    # -------------------------------Calculate Cancer Type--------------------------------------------------

    def calculate():
        v1=e1.get()
        v2=e2.get()
        v3=e3.get()
        v4=e4.get()
        v5=e5.get()
        v6=e6.get()
        v7=e7.get()
        v8=e8.get()
        v9=e9.get()
        v10=e10.get()
        v11=e11.get()
        v12=e12.get()
        v13=e13.get()
        v14=e14.get()
        v15=e15.get()
        v16=e16.get()
        v17=e17.get()
        v18=e18.get()
        v19=e19.get()

        if (v1.isdigit()==True and v2.isdigit()==True and v3.isdigit()==True and v4.isdigit()==True and v5.isdigit()==True
        and v6.isdigit()==True and v7.isdigit()==True and v8.isdigit()==True and v9.isdigit()==True and v10.isdigit()==True
        and v11.isdigit()==True and v12.isdigit()==True and v13.isdigit()==True and v14.isdigit()==True):
            a1 = int(e1.get())
            a2 = int(e2.get())
            a3 = int(e3.get())
            a4 = int(e4.get())
            a5 = int(e5.get())
            a6 = int(e6.get())
            a7 = int(e7.get())
            a8 = int(e8.get())
            a9 = int(e9.get())
            a10 = int(e10.get())
            a11 = int(e11.get())
            a12 = int(e12.get())
            a13 = int(e13.get())
            a14 = int(e14.get())
            tmp = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14]
            tmp = np.array(tmp)
            tmp = tmp.reshape(-14, 14)
            pred = lr.predict(tmp)
            prediction = "Result is = if M mean Malignant else if B mean Benign So patient report reult is :- " + str(pred)
            e20.insert(0,str(pred))
            messagebox.showinfo("Prediction of Diagnosis Report", prediction)
        elif (e1.get()=="" and e2.get()=="" and e3.get()=="" and e4.get()=="" and e5.get()=="" and e6.get()==""
              and e7.get()==""and e8.get()=="" and e9.get()=="" and e10.get()=="" and e11.get()=="" and e12.get()==""
              and e13.get()=="" and e14.get()==""):
            messagebox.showerror("Error","Please fill all required field of patient report")
        else:
            messagebox.showerror("Warning","Incorrect format of entry data please correct it")

# --------------------------------------Log out function-----------------------------------------------

    def log_out():
        sign_out = tkinter.messagebox.askyesno("Breast Cancer Prediction", "Do you want to log out from the system")
        if (sign_out == True):
            root.destroy()
            import Nav1_Login as lg
            lg.log_out()
        #qExit = tkinter.messagebox.askyesno("Breast Cancer Prediction", "Do you want to log out from the system")
        #if qExit > 0:
         #   root.destroy()
          #  return

    # ------------------------------------------Doctors List Window--------------------------------------------

    #------------------------------------------------Data Graph------------------------------------------------

#-----------------------------------------About us----------------------------------------------

    def about_us():
        root = Tk()
        root.title("Employ Salary Management System")
        root.state('z')
        ff1 = Label(root,
                    text=" About us:" + "\n\n" + "Breast cancer became the major source of mortality between women."
                    + "\n" +" The accessibility of healthcare datasets and data analysis promote the researchers to "
                    + "\n" +"apply study in extracting unknown pattern from healthcare datasets. The intention of this"
                    + "\n" +" study is to design a prediction system that can predict the incidence of the breast "
                    + "\n" +"cancer at early stage by analyzing smallest set of attributes that has been selected "
                     + "\n" +"from the clinical dataset. For breast cancer data analyst dataset have been used to "
                     + "\n" +"conduct the proposed experiment. The potential of the proposed method is obtained using "
                     + "\n" +"classification accuracy which was obtained by comparing actual to predicted values. "
                     + "\n" +"The outcome confirms that the maximum classification accuracy (99.28%) is "
                     + "\n" +"achieved for this study.",
                    font=('aria', 25, 'italic'), width=1400, height=650, bd=8, bg="yellow", relief="raise")
        ff1.pack(side=TOP)

    def contact_us():
        root = Tk()
        root.title("Employ Salary Management System")
        root.state('z')
        ff1 = Label(root,
                    text=" Contact us:" + "\n\n" + "Panipat" + "\n" + "12/4,Hooda Sector" + "\n" + "Near Grain Market Main Road" + "\n" + "HR,132101 India"
                         + "\n" + "Ph. +918572024591 / +918572024591",
                    font=('aria', 25, 'italic'), width=1400, height=650, bd=8, bg="yellow", relief="raise")
        ff1.pack(side=TOP)

    # ----------------------------------------Patient info label-----------------------------------------

    lblPatient_id = Label(frame, text="Patient ID", height="1", bg="blue", font=('aria', 16, 'bold'), fg="Black",
                          bd=20).grid(row=0, column=0)
    lblPatient_name = Label(frame, text="Patient Name", height="1", bg="blue", font=('aria', 16, 'bold'), fg="Black",
                            bd=20).grid(row=0, column=2)
    lblPatient_Ph = Label(frame, text="Patient Phone", height="2", bg="blue", font=('aria', 16, 'bold'),
                          fg="Black", bd=20).grid(row=1, column=0)
    lblPatient_address = Label(frame, text="Patient Address", height="1", bg="blue", font=('aria', 16, 'bold'),
                               fg="Black",
                               bd=20).grid(row=1, column=2)
    lblPatient_age = Label(frame, text="Age", height="1", bg="blue", font=('aria', 16, 'bold'),
                           fg="Black",
                           bd=20).grid(row=2, column=0)

    lblPatient_report = Label(frame, text="Patient Report :-", height="1", bg="blue", font=('aria', 16, 'bold'),
                           fg="yellow",
                           bd=20).grid(row=3, column=0)

# --------------------------------Labels---------------------------------------------------------------------

    lblRadius_Worst = Label(frame, text="Radius_Worst", height="1", bg="blue", font=('aria', 16, 'bold'), fg="Black",
                            bd=20).grid(row=4,
                                        column=0)
    lblTexture_Worst = Label(frame, text="Texture_Worst", height="1", bg="blue", font=('aria', 16, 'bold'), fg="Black",
                             bd=20).grid(
        row=4, column=2)
    lblPerimeter_Worst = Label(frame, text="Perimeter_Worst", height="2", bg="blue", font=('aria', 16, 'bold'),
                               fg="Black",
                               bd=20).grid(row=5, column=0)
    lblArea_Worst = Label(frame, text="Area_Worst", height="1", bg="blue", font=('aria', 16, 'bold'), fg="Black",
                          bd=20).grid(row=5, column=2)
    lblSmoothness_Worst = Label(frame, text="Smoothness_Worst", height="1", bg="blue", font=('aria', 16, 'bold'),
                                fg="Black",
                                bd=20).grid(row=6, column=0)
    lblCompactness_worst = Label(frame, text="Compactness_worst", height="1", bg="blue", font=('aria', 16, 'bold'),
                                 fg="Black",
                                 bd=20).grid(row=6, column=2)
    lblConcavity_Worst = Label(frame, text="Concavity_Worst", height="1", bg="blue", font=('aria', 16, 'bold'),
                               fg="Black",
                               bd=20).grid(row=7, column=0)
    lblConcavePoints_Worst = Label(frame, text="Concave Points_Worst", height="2", bg="blue", font=('aria', 16, 'bold'),
                                   fg="Black", bd=20).grid(
        row=7, column=2)
    lblSymmetry_Worst = Label(frame, text="Symmetry_Worst", height="1", bg="blue", font=('aria', 16, 'bold'),
                              fg="Black", bd=20,
                              anchor='w').grid(row=8, column=0)
    lblFractal_Dimension_Worst = Label(frame, text="Fractal_Dimension_Worst", height="1", bg="blue",
                                       font=('aria', 16, 'bold'), fg="Black", bd=20).grid(
        row=8, column=2)
    lblConcavity_Se = Label(frame, text="Concavity_Se", height="2", bg="blue", font=('aria', 16, 'bold'), fg="Black",
                            bd=20).grid(row=9, column=0)
    lblArea_Se = Label(frame, text="Area_Se", height="2", font=('aria', 16, 'bold'), bg="blue", fg="Black", bd=20).grid(
        row=9,
        column=2)
    lblConcave_Points_Mean = Label(frame, text="Concave Points_Mean", height="2", bg="blue", font=('aria', 16, 'bold'),
                                   fg="Black", bd=20).grid(
        row=10, column=0)
    lblTexture_Mean = Label(frame, text="Texture_Mean", height="2", bg="blue", font=('aria', 16, 'bold'), fg="Black",
                            bd=20).grid(
        row=10, column=2)
    lblresult=Label(frame, text="Patient Result :-", height="2", bg="Yellow", font=('aria', 16, 'bold'), fg="Black",
                            bd=20).grid(
        row=11, column=0)

    lblPatient_result = Label(frame, text="Patient Report :-", bg="blue", font=('aria', 16, 'bold'),
                              fg="pink",
                              bd=2).grid(row=11, column=0)
    lbldiagnosis = Label(frame, text="Diagnosis", height="1", bg="blue", font=('aria', 16, 'bold'),
                              fg="Black",
                              bd=2).grid(row=12, column=0)

    # ------------------------------------------Button space-----------------------------------------

    lblF1 = Label(f2, bg="blue").grid(
        row=1, column=0)
    lblF2 = Label(f2, bg="blue").grid(row=3, column=0)
    lblF3 = Label(f2, bg="blue").grid(row=5, column=0)
    lblF4 = Label(f2, bg="blue").grid(row=7, column=0)
    lblF5 = Label(f2, bg="blue").grid(row=9, column=0)
    lblF6 = Label(f2, bg="blue").grid(row=11, column=0)

# --------------------------------------------------Search Engine-----------------------------------


    photo = PhotoImage(file=r"C:\Users\navneen\Downloads\images.png").subsample(10, 10)
    photo_1 = PhotoImage(file=r"C:\Users\navneen\Downloads\index1.png").subsample(4, 5)
    photo_2 = PhotoImage(file=r"C:\Users\navneen\Downloads\log_out.png").subsample(3, 5)
    photo_3 = PhotoImage(file=r"C:\Users\navneen\Downloads\graph.png").subsample(3, 5)
    photo_4 = PhotoImage(file=r"C:\Users\navneen\Downloads\clear.png").subsample(3, 5)
    # label1 = ttk.Label(f2, text='Query')
    # label1.grid(row=9, column=0)


# --------------------------------------Patient text-----------------------------------------------------

    e15 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e15.grid(row=0, column=1)
    e16 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e16.grid(row=0, column=3)
    e17 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e17.grid(row=1, column=1)
    e18 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e18.grid(row=1, column=3)
    e19 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e19.grid(row=2, column=1)

    # ------------------------------------------Doctors List Window--------------------------------------------

    def doctor_appointment_1():
        import Nav4_Doctorlist_1 as dc_1
        root.destroy()
        dc_1.doctor_appointment("please wait, Opening list of best doctors for breast cancer treatment")


# ---------------------------------------Text Entry-----------------------------------------------------------------------

    e1 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e1.grid(row=4, column=1)
    e2 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e2.grid(row=4, column=3)
    e3 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e3.grid(row=5, column=1)
    e4 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e4.grid(row=5, column=3)
    e5 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e5.grid(row=6, column=1)
    e6 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e6.grid(row=6, column=3)
    e7 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e7.grid(row=7, column=1)
    e8 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e8.grid(row=7, column=3)
    e9 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e9.grid(row=8, column=1)
    e10 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e10.grid(row=8, column=3)
    e11 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e11.grid(row=9, column=1)
    e12 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e12.grid(row=9, column=3)
    e13 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e13.grid(row=10, column=1)
    e14 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e14.grid(row=10, column=3)
    e20 = Entry(frame, font=('aria', 17, 'bold'), bd=12, width=20, justify='left')
    e20.grid(row=12, column=1)

    # -----------------------------------Button color-------------------------------------------------

    def btnSubmit_Enter(event):
        btnSubmit["bg"] = "red"

    def btnSubmit_Leave(event):
        btnSubmit["bg"] = "white"

    def btnReset_Enter(event):
        btnReset["bg"] = "yellow"

    def btnReset_Leave(event):
        btnReset["bg"] = "white"

    def btnLogout_Enter(event):
        btnLogout["bg"] = "yellow"

    def btnLogout_Leave(event):
        btnLogout["bg"] = "white"

    def btnSave_Enter(event):
        btnSave["bg"] = "yellow"

    def btnSave_Leave(event):
        btnSave["bg"] = "white"

    def btnAppointment_Enter(event):
        btnAppointment["bg"] = "yellow"

    def btnAppointment_Leave(event):
        btnAppointment["bg"] = "white"

# ----------------------------------------Buttons------------------------------------------------------


    btnSubmit = Button(f2, text='Submit', bd=6, fg="black", font=('aria', 11, 'bold'), width=10, height=1,
                       command=calculate)
    btnSubmit.grid(row=0, column=0)
    btnSubmit.bind("<Enter>", btnSubmit_Enter)
    btnSubmit.bind("<Leave>", btnSubmit_Leave)

    btnAppointment = Button(f2, text="Appointment", bd=6, fg="black", font=('aria', 11, 'bold'), width=10, height=1,
                            command=doctor_appointment_1)
    btnAppointment.grid(row=2, column=0)
    btnAppointment.bind("<Enter>", btnAppointment_Enter)
    btnAppointment.bind("<Leave>", btnAppointment_Leave)

    btnSave = Button(f2, text="Save", bd=6, fg="black", font=('aria', 11, 'bold'), width=10, height=1,
                     command=save)
    btnSave.grid(row=4, column=0)
    btnSave.bind("<Enter>", btnSave_Enter)
    btnSave.bind("<Leave>", btnSave_Leave)

    btnReset = Button(f2, image=photo_4, activebackground='#c1bfbf', overrelief='groove',
                      relief='sunken',
                      command=Reset)
    btnReset.grid(row=6, column=0)
    btnReset.bind("<Enter>", btnReset_Enter)
    btnReset.bind("<Leave>", btnReset_Leave)


    btnLogout = Button(f2, image=photo_2, activebackground='#c1bfbf', overrelief='groove',
                       relief='sunken',
                       command=log_out)
    btnLogout.grid(row=10, column=0)
    btnLogout.bind("<Enter>", btnLogout_Enter)
    btnLogout.bind("<Leave>", btnLogout_Leave)


    # -------------------------------------Menu------------------------------------------------

    menu = Menu(root)

    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Home", menu=subMenu)
    subMenu.add_command(label="Submit", command=calculate)
    subMenu.add_command(label="Appointment", command=doctor_appointment_1)
    subMenu.add_command(label="Save", command=save)
    subMenu.add_command(label="Reset", command=Reset)
    subMenu.add_command(label="Log_Out", command=log_out)
    editMenu = Menu(menu)
    menu.add_cascade(label="Help", menu=editMenu)
    editMenu.add_command(label="About us", command=about_us)  # 156
    editMenu.add_command(label="Contact", command=contact_us)  # 171

    root.mainloop()

if __name__ == "__main__":
    demo("opening breast cancer prediction system")
