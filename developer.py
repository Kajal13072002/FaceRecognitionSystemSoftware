from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
 
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1600,height=40)

        img_top=Image.open(r"college_images\dev2.JPEG")
        img_top=img_top.resize((1600,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1600,height=750)

        #frame 
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=930,y=200,width=600,height=570)
        
        #Developer info
        dev_label=Label(main_frame,text="Hello!! , My name is Kajal Kumari,a self motivated student with",font=("times new roman",15),bg="Black",fg="white")
        dev_label.place(x=0,y=340)
        dev_label=Label(main_frame,text=" knowledge of programming languages and computer basics.I'm persuing",font=("times new roman",15),bg="black",fg="white")
        dev_label.place(x=0,y=370)
        dev_label=Label(main_frame,text="my B.Tech degree from NIT Srinagar in IT.My interests are in Software",font=("times new roman",15),bg="black",fg="white")
        dev_label.place(x=0,y=400)
        dev_label=Label(main_frame,text="Development,DBMS and ML.My hobbies are coding,reading,writing and ",font=("times new roman",15),bg="black",fg="white")
        dev_label.place(x=0,y=430)
        dev_label=Label(main_frame,text="driving.Interested in seeking a job as software engineer to utilize",font=("times new roman",15),bg="black",fg="white")
        dev_label.place(x=0,y=460)
        dev_label=Label(main_frame,text=" my technical skills and software design.",font=("times new roman",15),bg="black",fg="white")
        dev_label.place(x=0,y=490)

        img2=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\dev3.JPEG")
        img2=img2.resize((600,330),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
      
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=5,width=600,height=330)



if __name__ == "__main__":
     root=Tk()
     obj=Developer(root)
     root.mainloop()