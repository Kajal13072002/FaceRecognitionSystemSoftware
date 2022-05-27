from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from cv2 import resize
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
import random
import time
import datetime
from tkinter import filedialog, Text

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\log1.JPEG")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=600,y=170,width=350,height=450)

        img1=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\icon.PNG")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg.place(x=725,y=180,width=100,height=100)

        get_str=Label(frame,text="Let's get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=85,y=110)

        #label
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        username=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=225)

        self.txtpswrd=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpswrd.place(x=40,y=250,width=270)


        #------>>>>ICON IMAGES SETTING<<<<-------
        img2=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\logicon1.JPEG")
        img2=img2.resize((29,26),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg.place(x=640,y=325,width=29,height=26)


        img3=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\passicon1.JPEG")
        img3=img3.resize((29,26),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=395,width=29,height=26)
        #Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        #register button
        regisbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        regisbtn.place(x=15,y=350,width=160)
        #forgetpassword button
        forbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forbtn.place(x=10,y=370,width=160)
    
    #Regsiter Window
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpswrd.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="Komal" and self.txtpswrd.get()=="Kunal":
            messagebox.showinfo("Success","Welcome,this app is developed by Kajal")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="kajal13072002",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpswrd.get()
                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")    
            else:
                open_main=messagebox.askyesno("YesNo","Access to Admin only")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return 
            conn.commit()
            self.clear()
            conn.close()
    
    def clear(self):
        self.txtuser.set("")
        self.txtpswrd.set("")

   
    #-------------------------->>>>>>>>>>Reset Password<<<<<<<<<<<<<------------------------------
    
    def reset_pass(self):
        if self.combo_sec_q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="kajal13072002",database="face_recognizer")
                cur=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_sec_q.get(),self.txt_security.get())
                cur.execute(query,value)
                row=cur.fetchone()

                #------>>>>Print Row<<<<<<------------
                if row==None:
                    messagebox.showerror("Error","Please select the correct security question",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    cur.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.root2)









    #--------------------------->>>>>>Forgot Password Window<<<<<<<<-------------------------------
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="kajal13072002",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            #Print row
            if row==None:
                messagebox.showerror("Error","Please enter the valid UserName")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                sec_q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
                sec_q.place(x=50,y=80)
        
        

                self.combo_sec_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_sec_q["values"]=("Select","Your Birthday","Your favourite song","Your pet name")
                self.combo_sec_q.place(x=50,y=110,width=250)
                self.combo_sec_q.current(0)

                security_A=Label(self.root2,text="Security Answers",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="dark green",fg="white")
                btn.place(x=130,y=290)








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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
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
  
    def return_login(self):
        self.root.destroy()




if __name__ == "__main__":
   main()