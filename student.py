from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
 



class Student:
    def __init__(self,root):
     self.root=root
     self.root.geometry("1920x1080+0+0")
     self.root.title("Face Recognition System")
     
     #------>>>>>>Variables<<<<<------
     self.var_dep=StringVar()
     self.var_course=StringVar()
     self.var_year=StringVar()
     self.var_semester=StringVar()
     self.var_std_id=StringVar()
     self.var_std_name=StringVar()
     self.var_div=StringVar()
     self.var_roll=StringVar()
     self.var_gender=StringVar()
     self.var_dob=StringVar()
     self.var_phone=StringVar()
     self.var_faculty=StringVar()
     

#first image
     img=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\s1.JPEG")
     img=img.resize((500,130),Image.ANTIALIAS)
     self.photoimg=ImageTk.PhotoImage(img)

  
     f_lbl=Label(self.root,image=self.photoimg)
     f_lbl.place(x=0,y=0,width=520,height=130)
    
     #second image 
     img1=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\s2.JPEG")
     img1=img1.resize((500,130),Image.ANTIALIAS)
     self.photoimg1=ImageTk.PhotoImage(img1)


     f_lbl=Label(self.root,image=self.photoimg1)
     f_lbl.place(x=500,y=0,width=525,height=130)

     #third image
     img2=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\s3.JPEG")
     img2=img2.resize((500,130),Image.ANTIALIAS)
     self.photoimg2=ImageTk.PhotoImage(img2)
      
     f_lbl=Label(self.root,image=self.photoimg2)
     f_lbl.place(x=1000,y=0,width=530,height=130)

    #backgroung image
     img3=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\BG2.JPEG")
     img3=img3.resize((1920,1080),Image.ANTIALIAS)
     self.photoimg3=ImageTk.PhotoImage(img3)


     bg_img=Label(self.root,image=self.photoimg3)
     bg_img.place(x=0,y=130,width=1920,height=1080)

     title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark blue")
     title_lbl.place(x=0,y=0,width=1500,height=45)
    
     main_frame=Frame(bg_img,bd=2,bg="white")
     main_frame.place(x=10,y=55,width=1950,height=1050)

     #Left label frame
     Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
     Left_frame.place(x=10,y=10,width=750,height=580)

     img_left=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\attendance2.JPEG")
     img_left=img_left.resize((740,130),Image.ANTIALIAS)
     self.photoimg_left=ImageTk.PhotoImage(img_left)

     f_lbl=Label(Left_frame,image=self.photoimg_left)
     f_lbl.place(x=5,y=0,width=730,height=130)
     
     #current course frame
     current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",15,"bold"))
     current_course_frame.place(x=5,y=150,width=735,height=130)

     #Department
     dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
     dep_label.grid(row=0,column=0,padx=10,sticky=W)

     dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
     dep_combo["values"]=("Select Department","CSE","IT","ECE","Mechanical","Civil","EE","Chemical","MME")
     dep_combo.current(0)
     dep_combo.grid(row=0,column=1,padx=2,pady=10)
     
     #Course
     course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
     course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

     course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
     course_combo["values"]=("Select Course","B.Tech","M.Tech","M.Sc","PhD","MBA")
     course_combo.current(0)
     course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
    
    #year
     year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
     year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

     course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
     course_combo["values"]=("Select Year","2018-2022","2019-2023","2020-2024","2021-2025")
     course_combo.current(0)
     course_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
    
     #semester
     semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
     semester_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

     course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
     course_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
     course_combo.current(0)
     course_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
    
     #Class student information
     class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",15,"bold"))
     class_student_frame.place(x=5,y=280,width=735,height=255)
     
     #Student ID
     studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
     studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

     studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times of roman",12,"bold"))
     studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
     
     #Student Name
     studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
     studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

     studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times of roman",12,"bold"))
     studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
     
     #Class Division
     class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
     class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

     #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times of roman",12,"bold"))
     #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

     div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=20,state="readonly")
     div_combo["values"]=("A","B","C")
     div_combo.current(0)
     div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
     
     #Roll Number
     roll_no_label=Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
     roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

     roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times of roman",12,"bold"))
     roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

     #Gender
     gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
     gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

     #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times of roman",12,"bold"))
     #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
     

     gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="readonly")
     gender_combo["values"]=("Male","Female","Other")
     gender_combo.current(0)
     gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

     #DOB
     dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
     dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

     dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times of roman",12,"bold"))
     dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

     #Phone Number
     phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
     phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

     phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times of roman",12,"bold"))
     phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
    
     #Faculty name
     fac_label=Label(class_student_frame,text="Faculty Name:",font=("times new roman",12,"bold"),bg="white")
     fac_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

     fac_entry=ttk.Entry(class_student_frame,textvariable=self.var_faculty,width=20,font=("times of roman",12,"bold"))
     fac_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
     
     #Radio Button
     self.var_radio1=StringVar()
     radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
     radiobtn1.grid(row=4,column=0)
 
      
     radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
     radiobtn2.grid(row=4,column=1)

     #Buttons Frame
     btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
     btn_frame.place(x=5,y=165,width=735,height=30)

     save_btn=Button(btn_frame,text="Save",command=self.add_data,width="19",font=("times new roman",12,"bold"),bg="blue",fg="white")
     save_btn.grid(row=0,column=0)
     
     update_btn=Button(btn_frame,text="Update",command=self.update_data,width="19",font=("times new roman",12,"bold"),bg="blue",fg="white")
     update_btn.grid(row=0,column=1)

     dlte_btn=Button(btn_frame,text="Delete",command=self.delete_data,width="19",font=("times new roman",12,"bold"),bg="blue",fg="white")
     dlte_btn.grid(row=0,column=2)

     reset_btn=Button(btn_frame,text="Reset",width="19",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
     reset_btn.grid(row=0,column=3)
      
     btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
     btn_frame1.place(x=5,y=200,width=735,height=30)

     take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a photo sample",width="40",font=("times new roman",12,"bold"),bg="blue",fg="white")
     take_photo_btn.grid(row=0,column=1)

     updatephoto_btn=Button(btn_frame1,text="Update photo sample",width="40",font=("times new roman",12,"bold"),bg="blue",fg="white")
     updatephoto_btn.grid(row=0,column=2)

     


     #Right label frame
     Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
     Right_frame.place(x=760,y=10,width=750,height=580)
      
     img_right=Image.open(r"C:\Users\Kajal Kumari\OneDrive\Desktop\FaceRecognitionProject\college_images\right_image.JPEG")
     img_right=img_right.resize((740,130),Image.ANTIALIAS)
     self.photoimg_right=ImageTk.PhotoImage(img_right)

     f_lbl=Label(Right_frame,image=self.photoimg_right)
     f_lbl.place(x=5,y=0,width=730,height=130)

     #SEARCH SYSTEM
     search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
     search_frame.place(x=5,y=135,width=738,height=70)
     
     search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
     search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

     search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
     search_combo["values"]=("Select","Roll_No","Phone No")
     search_combo.current(0)
     search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
     
     search_entry=ttk.Entry(search_frame,width=15,font=("times of roman",12,"bold"))
     search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

     
     search_btn=Button(search_frame,text="Search",width="15",font=("times new roman",12,"bold"),bg="blue",fg="white")
     search_btn.grid(row=0,column=3,padx=4)

     showAll_btn=Button(search_frame,text="Show All",width="15",font=("times new roman",12,"bold"),bg="blue",fg="white")
     showAll_btn.grid(row=0,column=4,padx=4) 

     #----->>>Table Frame<<<-----
     table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
     table_frame.place(x=5,y=205,width=738,height=340)

     scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
     scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

     self.student_data_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Semester","Student_id","Name","Division","Roll_No","Gender","DOB","Phone_No","Faculty","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
     
     scroll_x.pack(side=BOTTOM,fill=X)
     scroll_y.pack(side=RIGHT,fill=Y)
     scroll_x.config(command=self.student_data_table.xview)
     scroll_y.config(command=self.student_data_table.yview)

     self.student_data_table.heading("Dep",text="Department")
     self.student_data_table.heading("Course",text="Course")
     self.student_data_table.heading("Year",text="Year")
     self.student_data_table.heading("Semester",text="Semester")
     self.student_data_table.heading("Student_id",text="StudentId")
     self.student_data_table.heading("Name",text="Name")
     self.student_data_table.heading("Division",text="Division")
     self.student_data_table.heading("Roll_No",text="Roll No")
     self.student_data_table.heading("Gender",text="Gender")
     self.student_data_table.heading("DOB",text="DOB")
     self.student_data_table.heading("Phone_No",text="Phone No")
     self.student_data_table.heading("Faculty",text="Faculty Name")
     self.student_data_table.heading("PhotoSample",text="PhotoSampleStatus")
     self.student_data_table["show"]="headings"
     
     self.student_data_table.column("Dep",width=100)
     self.student_data_table.column("Course",width=100)
     self.student_data_table.column("Year",width=100) 
     self.student_data_table.column("Semester",width=100)
     self.student_data_table.column("Student_id",width=100)
     self.student_data_table.column("Name",width=100)
     self.student_data_table.column("Division",width=100)
     self.student_data_table.column("Roll_No",width=100)
     self.student_data_table.column("Gender",width=100)
     self.student_data_table.column("DOB",width=100)
     self.student_data_table.column("Phone_No",width=100)
     self.student_data_table.column("Faculty",width=100)
     self.student_data_table.column("PhotoSample",width=150)

     self.student_data_table.pack(fill=BOTH,expand=1)
     self.student_data_table.bind("<ButtonRelease>",self.get_cursor)
     self.fetch_data()
     
#----->>>>>Function Declaration<<<<<-----

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
             try:
                  conn=mysql.connector.connect(host='localhost',username='root',password='kajal13072002',database='face_recognizer')
                  my_cursor=conn.cursor()
                  my_cursor.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                 
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_faculty.get(),
                                                                                                    self.var_radio1.get()
                                                                                             
                    
                                                                                                 ))
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
             except Exception as es:
                  messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

     #------>>>>>>Fetching Data from Database<<<<<<-------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kajal13072002",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_data")
        data=my_cursor.fetchall()      

        if len(data)!=0:
            self.student_data_table.delete(*self.student_data_table.get_children())
            for i in data:
               self.student_data_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #------>>>>>>>Get Cursor<<<<<<<-------
    def get_cursor(self,event=""):
         cursor_focus=self.student_data_table.focus()
         content=self.student_data_table.item(cursor_focus)
         data=content["values"]

         self.var_dep.set(data[0]),
         self.var_course.set(data[1]),
         self.var_year.set(data[2]),
         self.var_semester.set(data[3]),
         self.var_std_id.set(data[4]),
         self.var_std_name.set(data[5]),
         self.var_div.set(data[6]),
         self.var_roll.set(data[7]),
         self.var_gender.set(data[8]),
         self.var_dob.set(data[9]),
         self.var_phone.set(data[10]),
         self.var_faculty.set(data[11]),
         self.var_radio1.set(data[12])
     

    #------>>>>>>Update Function<<<<<<-----
    def update_data(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)     
         else:
               try:
                   Update=messagebox.askyesno("Update","Do you want to update the student's details?",parent=self.root)
                   if Update>0:
                       conn=mysql.connector.connect(host='localhost',username='root',password='kajal13072002',database='face_recognizer')
                       my_cursor=conn.cursor()
                       my_cursor.execute("update student_data set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,DOB=%s,Phone_No=%s,Faculty=%s,PhotoSample=%s where Student_id=%s", (
                                                                                                                                                                
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_faculty.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get()                                                                                                     
                                                                                                                                                      ))
                   else:
                         if not Update:
                              return 
                   messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                   conn.commit()
                   self.fetch_data
                   conn.close()
               except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 

     #delete function    
    def delete_data(self):
         if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student id is must",parent=self.root)
         else:
               try: 
                   delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student info?",parent=self.root)
                   if delete>0:
                       conn=mysql.connector.connect(host='localhost',username='root',password='kajal13072002',database='face_recognizer')
                       my_cursor=conn.cursor() 
                       sql="delete from student_data where Student_id=%s"
                       val=(self.var_std_id.get(),)
                       my_cursor.execute(sql,val)
                   else:
                         if not delete:
                              return


                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
               except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)          

     #reset
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("Select Division")
         self.var_roll.set("")
         self.var_gender.set("Male")
         self.var_dob.set("")
         self.var_phone.set("")
         self.var_faculty.set("")
         self.var_radio1.set("")
     

 
   # = = = = = = =  =  = Generate Data set or take photo sample = = = = = = = 
    def generate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
         else:
              try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='kajal13072002',database='face_recognizer')
                    my_cursor=conn.cursor() 
                    my_cursor.execute("select * from student_data")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                       id+=1
                   
                    my_cursor.execute("update student_data set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,DOB=%s,Phone_No=%s,Faculty=%s,PhotoSample=%s where Student_id=%s", (
                                                                                                                                                                
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_faculty.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get()==id+1                                                                                                     
                                                                                                                                                      ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()  


               # = = = = = = = = =LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV= = = = = = = = = =
                    face_classifier=cv2.CascadeClassifier("Haar Cascade Frontalface Default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #minimum neighbour=5

                        for(x,y,w,h) in faces:
                               face_cropped=img[y:y+h,x:x+w]
                               return face_cropped
                    
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                             img_id+=1
                             face=cv2.resize(face_cropped(my_frame),(450,450))
                             face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                             file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                             cv2.imwrite(file_name_path,face)
                             cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                             cv2.imshow("Cropped Face",face)

                         
                        if cv2.waitKey(1)==13 or int(img_id)==20:
                              break
                    cap.release()
                    cv2.destroyAllWindows()  
                    messagebox.showinfo("Result","Generating data sets completed!!!")
              except Exception as es:  
                   messagebox.showerror("Error",f"Due To:{str(es)}",paremt=self.root)                                                                                                                                                                                                     

  

 

if __name__ == "__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()