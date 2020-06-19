from tkinter import *
from tkinter import messagebox
import datetime
import pymysql.cursors
from tkinter import scrolledtext
import re
from prettytable import from_db_cursor
from PIL import Image,ImageTk
from PIL import *
from tkinter import filedialog

window=Tk()                    
window.geometry("600x600")
window.title("Final project")
imgSet=BooleanVar()

def validation():
   
    global val
    val=0
    ch1=0
    ch2=0
    ch3=0
    ch4=0
    
    v1=entry_1.get()
    v2=entry_2.get()
    v3=entry_3.get()
    v4=entry_4.get()
    v5=entry_5.get()
    v6=x1.get()
    v7=txt.get("1.0","end-1c")
    v8=vari.get()
    
    if(len(v1)!=0 and v1.isalpha()==True):
        if(len(v2)!=0 and v2.isalpha()==True):
            with open('stdid.txt','r')as stdid:
                if v3 in stdid.read():
                    ch1=1
                else:
                    ch1=0
            if(ch1==0 and v3.isdigit()==True):
                with open('contact.txt','r')as contact:
                    if v4 in contact.read():
                        ch2=1
                    else:
                        ch2=0
                if(len(v4)==10 and v4.isdigit()==True and ch2==0):
                    with open('email.txt','r')as email:
                        if v5 in email.read():
                            ch3=1
                        else:
                            ch3=0
                    if(ch3==0):
                        match=re.search("@gmail.com$",v5)
                        if(match):
                            with open('roll.txt','r')as roll:
                                if v6 in roll.read():
                                    ch4=1
                                else:
                                    ch4=0
                            if(v6!=0 and ch4==0):
                                if(v7!=0):
                                    if(v8!="Select"):
                                        f=open('stdid.txt','a')
                                        f.write(f'{v3}\n')
                                        f=open('contact.txt','a')
                                        f.write(f'{v4}\n')
                                        f=open('email.txt','a')
                                        f.write(f'{v5}\n')
                                        f=open('roll.txt','a')
                                        f.write(f'{v6}\n')
                                        val=1
                                    else:
                                        messagebox.showwarning("Error","Select Gender")
                                else:                
                                    messagebox.showwarning("Error","Enter address")            
                            else:
                                if(ch4==1):
                                    messagebox.showwarning("Error","Roll no already present")
                                else:
                                    messagebox.showwarning("Error","Enter valid roll no.")
                        else:
                            messagebox.showwarning("Error","Enter a valid email")
                    else:
                        messagebox.showwarning("Error","Email already present")
                else:
                    if(ch2==1):
                        messagebox.showwarning("Error","Contact number already present")
                    else:
                        messagebox.showwarning("Error","Invalid contact number \n Try Again")
            else:
                messagebox.showwarning("Error","Enter a valid student ID")
                
        else:
            messagebox.showwarning("Error","Enter Last  Name \n Try Again")
            
    else:
        messagebox.showwarning("Error","Enter First Name \n Try Again")
    
        
    if(val==1):
        database()
    else:
        messagebox.showwarning("Error","Please enter proper details")
        
def database():
   
    d1=entry_1.get()
    d2=entry_2.get()
    d3=entry_3.get()
    d4=vari.get()
    d5=w1.get()+'/' + w2.get()+'/' + w3.get()
    d6=entry_4.get()
    d7=entry_5.get()
    d8=x1.get()
    d9=txt.get("1.0","end-1c")
    
    #global curs
    curs=pymysql.connect(host="localhost",user="root",password="",db="management")
    mycursor=curs.cursor()
   
 
    a="INSERT INTO student(FirstName,Lastname,StudentID,Gender,Date,Contact,Email,Roll,Address,Photo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    image=converttoBinaryData()
    r1=(d1,d2,d3,d4,d5,d6,d7,d8,d9,image)
    mycursor.execute(a,r1)
    curs.commit()
    curs.close()

def converttoBinaryData():
    with open("Test.jpg","rb") as file:
        binaryData = file.read()
    return binaryData
    
def printed():
    win=Tk()
    win.geometry('1000x1000')
    win.configure(bg="white")
    win.title("DISPLAY")
    pathf="Test.jpg"
    im=Image.open(pathf)
    im=im.resize((150,150))
    tkimage=ImageTk.PhotoImage(im, master=win)
    profilePhoto=Label(win,image=tkimage)
    profilePhoto.image=tkimage
    profilePhoto.place(x=100,y=50)

    Label(win,text="First Name").place(x=100,y=250)
    Label(win,text="Last Name").place(x=100,y=300)
    Label(win,text="Student ID").place(x=100,y=350)
    Label(win,text="Address").place(x=100,y=400)      
    Label(win,text="Mobile No.").place(x=100,y=450)
    Label(win,text="Email").place(x=100,y=500)
    Label(win,text="Roll No.").place(x=100,y=550)
    Label(win,text="Date of Birth").place(x=100,y=600)
    Label(win,text="Gender").place(x=100,y=650)    

    Label(win,text=entry_1.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=250)
    Label(win,text=entry_2.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=300)
    Label(win,text=entry_3.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=350)
    Label(win,text=txt.get("1.0","end-1c"),bg="white",width=50,font="bold",relief="raised").place(x=250,y=400)      
    Label(win,text=entry_4.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=450)
    Label(win,text=entry_5.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=500)
    Label(win,text=x1.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=550)
    Label(win,text=w1.get()+'/' + w2.get()+'/' + w3.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=600)
    Label(win,text=vari.get(),bg="white",width=50,font="bold",relief="raised").place(x=250,y=650)
    
def selImage():
    path=filedialog.askopenfilename(parent=window,title='Choose file',filetypes=[("Image File",'.jpg'),("png Images",".png")])
    im=Image.open(path)
    im=im.resize((150,150))
    tkimage=ImageTk.PhotoImage(im)
    im.save("Test.jpg")
    imgholder.config(image=tkimage)
    imgholder.image=tkimage
    imgSet.set(True)
   



label=Label(window,text="STUDENT MANAGEMENT SYSTEM",relief="raised",fg="white",width=50,font="bold",bg="black")
label.place(x=40,y=10)
label1=Label(window,text=" First Name :",relief="raised",width=10,fg="white",font="bold",bg="Black")
label1.place(x=5,y=50)
entry_1=Entry(window,width=40,relief="solid")
entry_1.place(x=130,y=55)
label2=Label(window,text=" Last Name :",relief="raised",fg="white",width=10,font="bold",bg="Black")
label2.place(x=5,y=90)
entry_2=Entry(window,width=40,relief="solid")
entry_2.place(x=130,y=95)
label3=Label(window,text=" Student ID :",relief="raised",fg="white",width=10,font="bold",bg="black")
label3.place(x=5,y=130)
entry_3=Entry(window,width=40,relief="solid")
entry_3.place(x=130,y=135)
label4=Label(window,text="Gender :",relief="raised",fg="white",width=10,font="bold",bg="black")
label4.place(x=5,y=170)
choices = ["Male","Female"]
vari = StringVar(window)
vari.set("Select")
g=OptionMenu(window,vari,*choices)
g.place(x=130,y=170)
label5=Label(window,text="Date of birth :",relief="raised",fg="white",width=10,font="bold",bg="black")
label5.place(x=5,y=210)
w1=Spinbox(window,from_=1,to=31,width=5)
w1.place(x=130,y=210)
w2=Spinbox(window,from_=1,to=12,width=5)
w2.place(x=190,y=210)
w3=Spinbox(window,from_=1980,to=2019,width=5)
w3.place(x=250,y=210)
label6=Label(window,text=" Contact :",relief="raised",fg="white",width=10,font="bold",bg="black")
label6.place(x=5,y=250)
entry_4=Entry(window,width=40,relief="solid")
entry_4.place(x=130,y=255)
label7=Label(window,text="Email :",relief="raised",fg="white",width=10,font="bold",bg="black")
label7.place(x=5,y=290)
entry_5=Entry(window,width=40,relief="solid")
entry_5.place(x=130,y=295)
label8=Label(window,text=" Roll no. :",relief="raised",fg="white",width=10,font="bold",bg="black")
label8.place(x=5,y=330)
x1=Entry(window,width=40,relief="solid")
x1.place(x=130,y=330)
label9=Label(window,text=" Address :",relief="raised",fg="white",width=10,font="bold",bg="black")
label9.place(x=5,y=370)
txt=Text(window,height=5,width=60,relief="solid")
txt.place(x=130,y=400)
b1=Button(window,text="Submit",width=12,relief="raised",font="bold",bg="black",fg="white",command=validation)
b1.place(x=400,y=530)
b2=Button(window,text="Show",width=12,relief="raised",font="bold",bg="black",fg="white",command=printed)
b2.place(x=250,y=530)
#select Image Button
I1=Button(window,text="Upload Your Picture",width=16,bg="Grey",fg="Black",command=selImage)
I1.place(x=550,y=50)
imgholder=Label(window,bg="black",image="")
imgholder.place(x=570,y=75)
window.config(bg="white")
window.mainloop()
