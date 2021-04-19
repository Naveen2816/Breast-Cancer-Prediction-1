import csv
from tkinter import ttk
import tkinter.messagebox as box
from tkinter import *
from PIL import ImageTk, Image

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#--------------------------------------------Images Path------------------------------------

def doctor_appointment(audio):
    root = Tk()
    root.title("Doctor Appointment")
    root.state("z")
    root.config(bg="lightpink")

    Tops = Frame(root, width=1360, height=50, relief="raise")
    Tops.pack(side=TOP)

    engine.say(audio)
    engine.runAndWait()

    path = "4897dr-ashok-vaid.jpg"
    img = ImageTk.PhotoImage(Image.open(path))

    path_1 = "2521dr-pn-mohapatra.jpeg"
    img_1 = ImageTk.PhotoImage(Image.open(path_1))

    path_2 ="3917dr-vinod-raina.jpeg"
    img_2 = ImageTk.PhotoImage(Image.open(path_2))

    path_3 ="6992dr-subhankar-deb.jpeg"
    img_3 = ImageTk.PhotoImage(Image.open(path_3))

    path_4 ="4356dr-amit-agarwal.jpeg"
    img_4 = ImageTk.PhotoImage(Image.open(path_4))

    path_5="9467dr-s-m-shuaib-zaidi.jpeg"
    img_5=ImageTk.PhotoImage(Image.open(path_5))

    path_6="Dr_Sachin_Subhash_Marda-Surgical_Oncology-Yashoda_Hospitals__Somajiguda.jpg"
    img_6=ImageTk.PhotoImage(Image.open(path_6))

    path_7="1538719700.jpeg"
    img_7=ImageTk.PhotoImage(Image.open(path_7))

    path_8="1545647431.jpeg"
    img_8=ImageTk.PhotoImage(Image.open(path_8))

    path_9="1548153850.jpeg"
    img_9=ImageTk.PhotoImage(Image.open(path_9))
    #-----------------------------------------------Scrollbar----------------------------------------

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), background='steel blue', width=1350, height=700)

    fla = Frame(root, width=600, height=200, bg="Blue", relief="raise")
    fla.pack(side=TOP)

    canvas = Canvas(fla)
    frame = Frame(canvas,bg="steel blue")
    myscrollbar = Scrollbar(fla, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set, background='steel blue')

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((100, 100), window=frame, anchor='nw')
    frame.bind("<Configure>", myfunction)

    #---------------------------------------------Gmail--------------------------------------------

    def email():
        root.destroy()
        import Nav5_Gmail as gml
        gml.GMIL()

    #--------------------------------------Back function----------------------------------------------------

    def breast_cancer_window():
        root.destroy()
        import Nav3_Detection as mino
        mino.demo("please wait, breast cancer prediction system is opening ")

    #-------------------------------------------Labels--------------------------------------
    lbl_1 = Label(Tops,text="List of Best Doctors for Breast Cancer Treatment",bg="lightpink",width="110",height="2",font=('aria', 16, 'bold'), fg="Black",
                            ).grid(row=0, column=0)
    lbl_2 = Label(frame, image = img,height="220",bg="steel blue",width="220").grid(padx=10,row=0,column=0)
    lbl_2_info_0 = Label(frame,text=" Name – Dr Ashok Vaid").grid(pady=1,row=1,column=0)
    lbl_2_info_1 = Label(frame,text=" Hospital – Medanta The Medicity, Delhi NCR").grid(pady=1,row=2,column=0)
    lbl_2_info_2 = Label(frame,text=" Education – MBBS | MD - Internal Medicine | DM - Medical Oncology").grid(padx=20,pady=1,row=3,column=0)
    lbl_2_info_3 = Label(frame,text=" Specialization – (Medical Oncology) Stomach, Breast Cancer").grid(pady=1,row=4,column=0)

    lbl_3 = Label(frame, image = img_1,height="220",bg="steel blue",width="220").grid(padx=150,row=0,column=1)
    lbl_3_info_0 = Label(frame,text="  Name – Dr PN Mohapatra").grid(row=1,column=1)
    lbl_3_info_1 = Label(frame,text="Hospital – AMRI Hospital, Saltlake City, Kolkata").grid(pady=1,row=2,column=1)
    lbl_3_info_2 = Label(frame,text="  Education–MBBS | MD-Internal Medicine | Director-Medical Oncology").grid(padx=20,pady=1,row=3,column=1)
    lbl_3_info_3 = Label(frame,text=" Specialization – (Medical Oncology)Stomach,Breast,Prostate Cancer").grid(pady=1,row=4,column=1)

    lbl_4 = Label(frame, image = img_2,height="220",bg="steel blue",width="220").grid(row=0,column=2)
    lbl_4_info_0 = Label(frame,text="  Name – Dr Vinod Raina").grid(pady=1,row=1,column=2)
    lbl_4_info_1 = Label(frame,text="Hospital–Fortis Memorial Research Institute(FMRI),Delhi NCR").grid(pady=1,row=2,column=2)
    lbl_4_info_2 = Label(frame,text=" Education – MBBS | MD - Internal Medicine | DM - Medical Oncology").grid(padx=3,pady=1,row=3,column=2)
    lbl_4_info_3 = Label(frame,text=" Specialization – (Medical Oncology)Stomach,Breast,Prostate Cancer").grid(pady=1,row=4,column=2)

    lbl_5 = Label(frame, image = img_3,height="220",bg="steel blue",width="220").grid(padx=10,row=7,column=0)
    lbl_5_info_0 = Label(frame,text="  Name – Dr Subhankar Deb ").grid(pady=1,row=8,column=0)
    lbl_5_info_1 = Label(frame,text=" Hospital – AMRI Hospital, Kolkata ").grid(pady=1,row=9,column=0)
    lbl_5_info_2 = Label(frame,text=" Education – MBBS | MS - General Surgery | DNB").grid(padx=20,pady=1,row=10,column=0)
    lbl_5_info_3 = Label(frame,text=" Specialization – (Medical Oncology) Stomach, Breast Cancer").grid(pady=1,row=11,column=0)

    lbl_6 = Label(frame, image = img_4,height="200",bg="steel blue",width="220").grid(padx=10,row=7,column=1)
    lbl_6_info_0 = Label(frame,text="   Name – Dr Amit Agarwal ").grid(pady=1,row=8,column=1)
    lbl_6_info_1 = Label(frame,text=" Hospital – BLK Super Specialty Hospital, Delhi ").grid(pady=1,row=9,column=1)
    lbl_6_info_2 = Label(frame,text=" Education – MBBS | MD – Medicine | DM - Oncology").grid(padx=20,pady=1,row=10,column=1)
    lbl_6_info_3 = Label(frame,text=" Specialization – (Medical Oncology) Stomach, Breast Cancer").grid(pady=1,row=11,column=1)

    lbl_7 = Label(frame, image = img_5,height="200",bg="steel blue",width="220").grid(padx=10,row=7,column=2)
    lbl_7_info_0 = Label(frame,text=" Name – Dr S M Shuaib Zaidi ").grid(pady=1,row=8,column=2)
    lbl_7_info_1 = Label(frame,text=" Hospital – Sharda Health City, Delhi NCR ").grid(pady=1,row=9,column=2)
    lbl_7_info_2 = Label(frame,text=" Education – MBBS | MS | MCh - Surgical Oncology").grid(padx=20,pady=1,row=10,column=2)
    lbl_7_info_3 = Label(frame,text=" Specialization – (Medical Oncology)Breast Cancer").grid(pady=1,row=11,column=2)

    lbl_8 = Label(frame, image = img_6,height="200",bg="steel blue",width="220").grid(padx=10,row=14,column=0)
    lbl_8_info_0 = Label(frame,text=" Name - Dr. Sachin Subhash Marda  ").grid(pady=1,row=15,column=0)
    lbl_8_info_1 = Label(frame,text=" Hospital – Surgical Oncology in Yashoda Hospitals, Somajiguda ").grid(pady=1,row=16,column=0)
    lbl_8_info_2 = Label(frame,text=" Education – MBBS, MS - General Surgery").grid(padx=20,pady=1,row=17,column=0)
    lbl_8_info_3 = Label(frame,text=" Specialization – neck and head surgeon,Breast Surgeon").grid(pady=1,row=18,column=0)

    lbl_9 = Label(frame, image = img_7,height="200",bg="steel blue",width="220").grid(padx=10,row=14,column=1)
    lbl_9_info_0 = Label(frame,text=" Name - Dr Rajeev Agarwal  ").grid(pady=1,row=15,column=1)
    lbl_9_info_1 = Label(frame,text=" Hospital –  Medanta-The Medicity, Delhi NCR ").grid(pady=1,row=16,column=1)
    lbl_9_info_2 = Label(frame,text=" Education – MBBS │ MS (Surgery) │ Senior Resident in Cancer Surgery").grid(padx=20,pady=1,row=17,column=1)
    lbl_9_info_3 = Label(frame,text=" Specialization – Director │ Breast Services (Cancer Institute)").grid(pady=1,row=18,column=1)

    lbl_10 = Label(frame, image = img_8,height="200",bg="steel blue",width="220").grid(padx=10,row=14,column=2)
    lbl_10_info_0 = Label(frame,text=" Name - Dr Ramesh Sarin  ").grid(pady=1,row=15,column=2)
    lbl_10_info_1 = Label(frame,text=" Hospital –   Indraprastha Apollo Hospital, Delhi ").grid(pady=1,row=16,column=2)
    lbl_10_info_2 = Label(frame,text=" Education – MBBS │ MS │ FRCS").grid(padx=20,pady=1,row=17,column=2)
    lbl_10_info_3 = Label(frame,text=" Specialization – Senior Consultant │ Medical Oncology").grid(pady=1,row=18,column=2)

    lbl_11 = Label(frame, image = img_9,height="200",bg="steel blue",width="220").grid(padx=10,row=21,column=0)
    lbl_11_info_0 = Label(frame,text=" Name - Dr Dinesh Chandra Katiyar  ").grid(pady=1,row=22,column=0)
    lbl_11_info_1 = Label(frame,text=" Hospital –   Venkateshwar Hospital, Delhi ").grid(pady=1,row=23,column=0)
    lbl_11_info_2 = Label(frame,text=" Education – MBBS │MS │ M.Ch (Surgical Oncology)").grid(padx=20,pady=1,row=24,column=0)
    lbl_11_info_3 = Label(frame,text=" Specialization – Senior Consultant │ Surgical Oncology").grid(pady=1,row=25,column=0)
    #--------------------------------------------Entry-------------------------------------------------

    entry_2_info_4 = Entry(frame,width="30")
    entry_2_info_4.grid(pady=1,row=5,column=0)
    entry_2_info_4.insert(0,"Email Id - ashokvaid@gmail.com")

    entry_3_info_4 = Entry(frame,width="32")
    entry_3_info_4.grid(pady=1,row=5,column=1)
    entry_3_info_4.insert(0,"Email Id - pnmohapatra@gmail.com")

    entry_4_info_4 = Entry(frame,width="32")
    entry_4_info_4.grid(pady=1,row=5,column=2)
    entry_4_info_4.insert(0,"Email Id - vinodraina@gmail.com")

    entry_5_info_4 = Entry(frame,width="34")
    entry_5_info_4.grid(pady=1,row=12,column=0)
    entry_5_info_4.insert(0,"Email Id - shubenkerdeb@gmail.com")

    entry_6_info_4 = Entry(frame,width="34")
    entry_6_info_4.grid(pady=1,row=12,column=1)
    entry_6_info_4.insert(0,"Email Id - amitagrwal@gmail.com")

    entry_7_info_4 = Entry(frame,width="34")
    entry_7_info_4.grid(pady=1,row=12,column=2)
    entry_7_info_4.insert(0,"Email Id - sahubzaidi@gmail.com")

    entry_8_info_4 = Entry(frame,width="34")
    entry_8_info_4.grid(pady=1,row=19,column=0)
    entry_8_info_4.insert(0,"Email Id - sachinsubhash@gmail.com")

    entry_9_info_4 = Entry(frame,width="34")
    entry_9_info_4.grid(pady=1,row=19,column=1)
    entry_9_info_4.insert(0,"Email Id - rajivagrwal@gmail.com")

    entry_9_info_4 = Entry(frame,width="34")
    entry_9_info_4.grid(pady=1,row=19,column=2)
    entry_9_info_4.insert(0,"Email Id - rameshsarin@gmail.com")

    entry_10_info_4 = Entry(frame,width="34")
    entry_10_info_4.grid(pady=1,row=26,column=0)
    entry_10_info_4.insert(0,"Email Id - dineshktariya@gmail.com")

    #------------------------------------------Button---------------------------------------------------

    btn_1 = Button(frame,text="Gmail",width="10",command=email)
    btn_1.grid(pady=2,row=6,column=0)

    btn_2 = Button(frame,text="Gmail",width="10",command=email)
    btn_2.grid(pady=2,row=6,column=1)

    btn_3 = Button(frame,text="Gmail",width="10",command=email)
    btn_3.grid(pady=2,row=6,column=2)

    btn_4 = Button(frame,text="Gmail",width="10",command=email)
    btn_4.grid(pady=2,row=13,column=0)

    btn_5 = Button(frame,text="Gmail",width="10",command=email)
    btn_5.grid(pady=2,row=13,column=1)

    btn_6 = Button(frame,text="Gmail",width="10",command=email)
    btn_6.grid(pady=2,row=13,column=2)

    btn_7 = Button(frame,text="Gmail",width="10",command=email)
    btn_7.grid(pady=2,row=20,column=0)

    btn_8 = Button(frame,text="Gmail",width="10",command=email)
    btn_8.grid(pady=2,row=20,column=1)

    btn_9 = Button(frame,text="Gmail",width="10",command=email)
    btn_9.grid(pady=2,row=20,column=2)

    btn_10 = Button(frame,text="Gmail",width="10",command=email)
    btn_10.grid(pady=2,row=27,column=0)

    btnback = ttk.Button(Tops, text='Back', width=10,command=breast_cancer_window)
    btnback.place(x=1280, y=30)


    root.mainloop()
if __name__=="__main__":
    doctor_appointment("please wait, Opening list of best doctors for breast cancer treatment ")
