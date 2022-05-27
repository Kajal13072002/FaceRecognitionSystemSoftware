from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
 
class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1600,height=40)

        img_top=Image.open(r"college_images\help.JPEG")
        img_top=img_top.resize((1520,740),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=3,y=45,width=1520,height=740)

        dev_label=Label(f_lbl,text="Contact me :kajal130100@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="dark blue")
        dev_label.place(x=1000,y=5)




if __name__ == "__main__":
     root=Tk()
     obj=Help(root)
     root.mainloop()