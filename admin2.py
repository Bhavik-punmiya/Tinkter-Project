from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import login

# Establishing MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhavik0310",
    database="djsanghvi"
)
my_cursor = mydb.cursor()


class AdminControls:
    def __init__(self, root):
        self.root = root

        # Local variables
        self.teacherName = StringVar()
        self.teacherGender = StringVar()
        self.teacherBranch = StringVar()
        self.teacherContact = StringVar()
        self.teacherSubject = StringVar()
        self.teacherUsername = StringVar()
        self.teacherPassword = StringVar()
        self.teacherSession = StringVar()

        # Call the tkinter frames to the window
        self.adminControlsFrame()
        self.adminFrameButtons()
        self.tableOutputFrame()

    """Teacher Info Entries Frame"""

    def adminControlsFrame(self):
        # Admin Control Frame Configurations
        self.entriesFrame = Frame(self.root, bg="#5856a0")
        self.entriesFrame.pack(side=TOP, fill=X)
        self.admin_frame_title = Label(self.entriesFrame, text="Admin View", font=("Goudy old style", 35),
                                       bg="#5856a0",
                                       fg="white")
        self.admin_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        # Teacher Name
        self.labelName = Label(self.entriesFrame, text="Name", font=("Times New Roman", 16, "bold"), bg="#5856a0",
                               fg="white")
        self.labelName.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtName = Entry(self.entriesFrame, textvariable=self.teacherName, font=("Times New Roman", 15), width=30)
        self.txtName.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Teacher Gender
        self.labelGender = Label(self.entriesFrame, text="Gender", font=("Times New Roman", 16, "bold"), bg="#5856a0",
                                 fg="white")
        self.labelGender.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.comboGender = ttk.Combobox(self.entriesFrame, textvariable=self.teacherGender, font=("Times New Roman", 15),
                                        width=28, state="readonly")
        self.comboGender['values'] = ("Male", "Female", "Trans", "Prefer Not to Say")
        self.comboGender.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        # Teacher Branch
        self.labelBranch = Label(self.entriesFrame, text="Branch", font=("Times New Roman", 16, "bold"),
                                 bg="#5856a0", fg="white")
        self.labelBranch.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.comboBranch = ttk.Combobox(self.entriesFrame, textvariable=self.teacherBranch, font=("Times New Roman", 15),
                                        width=28, state="readonly")
        self.comboBranch['values'] = (
            "Electronics and Telecommunication Engg", "Information Technology", "Computer Engineering",
            "Mechanical Engineering", "Computer Science and Engineering (Data Science)",
            "Artificial Intelligence and Machine Learning", "Artificial Intelligence (AI) and Data Science",
            "Computer Science and Engineering", "(IOT and Cyber Security with Block Chain Technology)",
            "Chemical Engineering", "Electronics Engineering", "Production Engineering", "Biomedical Engineering")
        self.comboBranch.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Teacher Contact Number
        self.labelContact = Label(self.entriesFrame, text="Contact Number", font=("Times New Roman", 16, "bold"),
                                  bg="#5856a0", fg="white")
        self.labelContact.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.txtContact = Entry(self.entriesFrame, textvariable=self.teacherContact, font=("Times New Roman", 15),
                                width=30)
        self.txtContact.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        # Teacher Subject
        self.labelSubject = Label(self.entriesFrame, text="Subject", font=("Times New Roman", 16, "bold"),
                                  bg="#5856a0", fg="white")
        self.labelSubject.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txtSubject = Entry(self.entriesFrame, textvariable=self.teacherSubject, font=("Times New Roman", 15),
                                width=30)
        self.txtSubject.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Teacher Username
        self.labelUsername = Label(self.entriesFrame, text="Username", font=("Times New Roman", 16, "bold"),
                                   bg="#5856a0", fg="white")
        self.labelUsername.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        self.txtUsername = Entry(self.entriesFrame, textvariable=self.teacherUsername, font=("Times New Roman", 15),
                                 width=30)
        self.txtUsername.grid(row=3, column=3, padx=10, pady=5, sticky="w")

        # Teacher Password
        self.labelPassword = Label(self.entriesFrame, text="Password", font=("Times New Roman", 16, "bold"),
                                   bg="#5856a0", fg="white")
        self.labelPassword.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.txtPassword = Entry(self.entriesFrame, textvariable=self.teacherPassword, font=("Times New Roman", 15),
                                 width=30)
        self.txtPassword.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Teacher Session
        self.labelSession = Label(self.entriesFrame, text="Session", font=("Times New Roman", 16, "bold"),
                                  bg="#5856a0", fg="white")
        self.labelSession.grid(row=4, column=2, padx=10, pady=5, sticky="w")
        self.comboSession = ttk.Combobox(self.entriesFrame, textvariable=self.teacherSession,
                                         font=("Times New Roman", 15), width=28, state="readonly")
        self.comboSession['values'] = ("Practical Lab", "Lecture")
        self.comboSession.grid(row=4, column=3, padx=10, pady=5, sticky="w")

    """CTA Methods"""

    def addTeacher(self):
        if self.txtName.get() == "" or self.txtContact.get() == "" or self.comboBranch.get() == "":
            messagebox.showerror("Error!", "Please fill all the required fields!")
            return
        else:
            teacher_name = self.txtName.get()
            teacher_contact = self.txtContact.get()
            teacher_branch = self.comboBranch.get()
            teacher_gender = self.comboGender.get()  # Get teacher's gender
            teacher_subject = self.txtSubject.get()  # Get teacher's subject
            teacher_username = self.txtUsername.get()  # Get teacher's username
            teacher_password = self.txtPassword.get()  # Get teacher's password
            teacher_session = self.comboSession.get()  # Get teacher's session
            
            # Your code to handle adding a new teacher using the provided data
            try:
                sql = "INSERT INTO teachers (name, gender, branch, contact_number, subject, username, password, session) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (teacher_name, teacher_gender, teacher_branch, teacher_contact, teacher_subject, teacher_username, teacher_password, teacher_session)
                my_cursor.execute(sql, values)
                mydb.commit()
                messagebox.showinfo("Success!", "Teacher added successfully!")
            except Exception as e:
                messagebox.showerror("Error!", f"Failed to add teacher: {e}")
            
            # Clear input fields after adding the teacher
            self.clearInputs()

    # Method to clear input fields after performing operations
    def clearInputs(self):
        self.txtName.delete(0, END)
        self.txtContact.delete(0, END)
        self.comboBranch.set("")
        self.comboGender.set("")
        self.txtSubject.delete(0, END)
        self.txtUsername.delete(0, END)
        self.txtPassword.delete(0, END)
        self.comboSession.set("")
        # Clear other input fields if needed
    
    def updateTeacher(self):
        teacher_username = self.teacherUsername.get()  # Get the username of the teacher to update
        if teacher_username:
            # Retrieve updated values from UI fields
            updated_name = self.teacherName.get()
            updated_contact = self.teacherContact.get()
            updated_branch = self.teacherBranch.get()
            updated_gender = self.teacherGender.get()
            updated_subject = self.teacherSubject.get()
            updated_password = self.teacherPassword.get()
            updated_session = self.teacherSession.get()

            try:
                # Update teacher details in the database
                sql = "UPDATE teachers SET name = %s, gender = %s, branch = %s, contact_number = %s, subject = %s, password = %s, session = %s WHERE username = %s"
                values = (updated_name, updated_gender, updated_branch, updated_contact, updated_subject, updated_password, updated_session, teacher_username)
                my_cursor.execute(sql, values)
                mydb.commit()
                messagebox.showinfo("Success!", "Teacher details updated successfully!")

                # Clear inputs and update the table output frame
                self.clearInputs()  # Clear input fields
                self.updateTableOutputFrame()  # Update the Treeview output frame after updating

            except Exception as e:
                messagebox.showerror("Error!", f"Failed to update teacher details: {e}")
        else:
            messagebox.showerror("Error!", "Please enter the username of the teacher to update.")



            
    def logOut(self):
        self.entriesFrame.destroy()
        self.buttonsFrame.destroy()
        self.tableFrame.destroy()
        login.Login(self.root)
        
    def viewTeachers(self):
        # Your code to retrieve and display all teachers from the database
        try:
            my_cursor.execute("SELECT * FROM teachers")
            teachers = my_cursor.fetchall()

            # Display retrieved teachers in the UI or handle as needed
            for teacher in teachers:
                print(teacher)  # Replace this with your display logic for UI
        except Exception as e:
            messagebox.showerror("Error!", f"Failed to retrieve teachers: {e}")

    # Other methods for managing teachers (e.g., edit, retrieve, etc.)

    
    def adminFrameButtons(self):
        # Button Frame Configurations
        self.buttonsFrame = Frame(self.entriesFrame, bg="#5856a0")
        self.buttonsFrame.grid(row=10, column=0, padx=10, pady=10, sticky="w", columnspan=8)

        # Add a new Record
        self.btnAdd = Button(self.buttonsFrame, command=self.addTeacher, text="Add Instructor", bd=0, cursor="hand2",
                            bg="#EADDF7", fg="#5856a0", width=20, font=("Impact", 15))
        self.btnAdd.grid(row=0, column=0, padx=10)

        # Update Selected Record
        self.btnUpdate = Button(self.buttonsFrame, command=self.updateTeacher, text="Update Instructor", bd=0,
                                cursor="hand2", bg="#EADDF7", fg="#5856a0", width=20, font=("Impact", 15))
        self.btnUpdate.grid(row=0, column=1, padx=10)

        # Delete Selected Record
        self.btnDlt = Button(self.buttonsFrame, command=self.deleteTeacher, text="Remove Instructor", bd=0,
                            cursor="hand2", bg="#EADDF7", fg="#5856a0", width=20, font=("Impact", 15))
        self.btnDlt.grid(row=0, column=2, padx=10)

        # Reset Widget Inputs
        self.btnReset = Button(self.buttonsFrame, command=self.clearInputs, text="Reset Form", bd=0, cursor="hand2",
                            bg="#EADDF7", fg="#5856a0", width=20, font=("Impact", 15))
        self.btnReset.grid(row=0, column=3, padx=10)

        # Display List
        self.btnView = Button(self.buttonsFrame, command=self.viewTeachers, text="View Instructor List", bd=0,
                            cursor="hand2", bg="#EADDF7", fg="#5856a0", width=20, font=("Impact", 15))
        self.btnView.grid(row=0, column=4, padx=10)

        
        # LogOut
        self.btnLogOut = Button(self.entriesFrame, command=self.logOut, text="Log Out", bd=0, cursor="hand2",
                                bg="#EADDF7", fg="#5856a0", width=15, font=("Impact", 15))
        self.btnLogOut.grid(row=0, column=6, padx=15, sticky="e")
        
    def tableOutputFrame(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=400, width=1400, height=560)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        # ttk style object to add configurations
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 14, "bold"), sticky="w")

        # Fetch data from MySQL database
        my_cursor.execute("SELECT * FROM teachers")
        teachers = my_cursor.fetchall()  # Using the global 'my_cursor'

        # Formatting the output table view
        self.out = ttk.Treeview(self.tableFrame, yscrollcommand=self.yScroll.set,
                                columns=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"),
                                style="mystyle.Treeview")
        self.out.heading("1", text="ID")
        self.out.column("1", width=10)
        self.out.heading("2", text="Name")
        self.out.column("2", width=150)
        self.out.heading("3", text="Gender")
        self.out.column("3", width=80)
        self.out.heading("4", text="Branch")
        self.out.column("4", width=250)
        self.out.heading("5", text="Contact Number")
        self.out.column("5", width=100)
        self.out.heading("6", text="Subject")
        self.out.column("6", width=150)
        self.out.heading("7", text="Username")
        self.out.column("7", width=150)
        self.out.heading("8", text="Password")
        self.out.column("8", width=150)
        self.out.heading("9", text="Session")
        self.out.column("9", width=100)
        self.out.heading("10", text="Class ID")
        self.out.column("10", width=80)
        
        self.out['show'] = 'headings'

        # Insert data into the Treeview
        for i, teacher in enumerate(teachers, start=1):
            self.out.insert('', 'end', values=teacher)

        # Virtual Events to trigger methods
        self.out.bind("<ButtonRelease-1>", self.getData)

        # TreeView output layout configurations
        self.out.pack(fill=X)
        self.yScroll.config(command=self.out.yview)
        
    def deleteTeacher(self):
        teacher_username = self.txtUsername.get()  # Get the username from the Entry widget
        if teacher_username:
            try:
                # Delete the teacher from the database
                sql = "DELETE FROM teachers WHERE username = %s"
                value = (teacher_username,)
                my_cursor.execute(sql, value)
                mydb.commit()
                messagebox.showinfo("Success!", "Teacher deleted successfully!")

                # Clear inputs and update the table output frame
                self.clearInputs()  # Clear input fields
                self.updateTableOutputFrame()  # Update the Treeview output frame after deletion

            except Exception as e:
                messagebox.showerror("Error!", f"Failed to delete teacher: {e}")
        else:
            messagebox.showerror("Error!", "Please enter the username of the teacher to delete.")

    def updateTableOutputFrame(self):
        try:
            # Clear the current table output frame (TreeView)
            for item in self.out.get_children():
                self.out.delete(item)

            # Fetch the updated data from the database
            my_cursor.execute("SELECT * FROM teachers")
            teachers = my_cursor.fetchall()

            # Insert updated data into the Treeview output frame
            for i, teacher in enumerate(teachers, start=1):
                self.out.insert('', 'end', values=teacher)

        except Exception as e:
            messagebox.showerror("Error!", f"Failed to update table output frame: {e}")
        
    def getData(self, event):
        try:
            selected_item = self.out.focus()  # Get the selected item from the Treeview
            if selected_item:  # Check if any item is selected
                selected_data = self.out.item(selected_item)
                chosen_row = selected_data["values"]

                # Setting data to respective Entry/Combobox fields
                self.teacherName.set(chosen_row[1])  # Professor Name
                self.teacherGender.set(chosen_row[2])  # Gender
                # For branch, contact number, subject, username, and session, update the respective variables accordingly
                self.teacherBranch.set(chosen_row[3])  # Branch
                self.teacherContact.set(chosen_row[4])  # Tel Number
                # Assuming self.hrRate and self.avail are related to Hourly Rate and Availability
                self.hrRate.set(chosen_row[5])  # Hourly Rate
                self.avail.set(chosen_row[6])  # Availability
                # Update other fields similarly based on your Treeview columns

                # Fetch the username and password from the Treeview and set them accordingly
                self.teacherUsername.set(chosen_row[8])  # Username
                self.teacherPassword.set(chosen_row[9])  # Password

                # Implement the logic for the 'selectDays' method if needed
                # self.selectDays(event)

        except IndexError:
            pass  # Handling IndexError if the selected row is out of range
