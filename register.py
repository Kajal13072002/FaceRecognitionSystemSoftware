from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")
        
        #------>>>>>>Text Variable<<<<<<-------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
         
        #bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\regis.JPEG")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #frame
        frame=Frame(self.root,bg="sky blue")
        frame.place(x=380,y=120,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE!!",font=("times new roman",25,"bold"),fg="black",bg="sky blue")
        register_lbl.place(x=10,y=10)
        
        #Labels and Entries
        #---->ROW 1<<<<-----
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        fname.place(x=50,y=80)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=110,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        l_name.place(x=370,y=80)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=110,width=250)
        #----->>>>ROW2<<<<-----
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        contact.place(x=50,y=150)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=180,width=250)

        email=Label(frame,text="Email ID",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        email.place(x=370,y=150)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=180,width=250)

       #---->>>>ROW3<<<<<------
        sec_q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        sec_q.place(x=50,y=220)
        
        

        self.combo_sec_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_sec_q["values"]=("Select","Your Birthday","Your favourite song","Your pet name")
        self.combo_sec_q.place(x=50,y=250,width=250)
        self.combo_sec_q.current(0)

        security_A=Label(frame,text="Security Answers",font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        security_A.place(x=370,y=220)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=250,width=250)
        
       #------>>>>>>ROW4<<<<---------
        pswrd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        pswrd.place(x=50,y=290)

        self.txt_pswrd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswrd.place(x=50,y=320,width=250)

        cnfrm_pswrd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        cnfrm_pswrd.place(x=370,y=290)

        self.txt_cnfrm_pswrd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_cnfrm_pswrd.place(x=370,y=320,width=250)


    #------>>>>>Check Button<<<<<--------
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to all the Terms & Conditions",font=("times new roman",12,"bold"),bg="sky blue",activebackground="sky blue",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
    #------->>>>>Buttons<<<<<------------
        img=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\regisnow.PNG")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=430,width=210)
        
        img1=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\login.JPEG")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=380,y=430,width=210)

    #----->>>>Function Declaration<<<<--------
    def register_data(self):
       if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
           messagebox.showerror("Error","All fields are required")
       elif self.var_pass.get()!=self.var_confpass.get():
           messagebox.showerror("Error","Password and Confirm Password must be same")
       elif self.var_check.get()==0:
           messagebox.showerror("Error","Kindly agree to the Terms & Conditions")
       else:
           conn=mysql.connector.connect(host="localhost",user="root",password="kajal13072002",database="face_recognizer")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
               messagebox.showerror("Error","User already exist,kindly try another ID")
           else:
               my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                  
                                                                                  ))
           conn.commit()
           conn.close()
           messagebox.showinfo("Success","Registered Successfully")


 
 
 



if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()