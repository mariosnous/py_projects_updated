import tkinter
from tkinter import ttk
import os
import openpyxl


def enter_data():
    accepted = accept_term_status_var.get()
    if accepted == "Accepted":
        # User_Info
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
    # Course Info

        registration_status = reg_status_var.get()

        numcourses = numcourses_spinbox.get()
        numsemesters = numsemesters_spinbox.get()

        print(f"First Name : {first_name} -- Last Name : {last_name} ")
        print(f"Title : {title} -- Age: {age} -- Nationality: {nationality}")
        print(
            f"Number of Courses : {numcourses} -- Number Of Semesters: {numsemesters} ")
        print(
            f"The User registration status is : {registration_status}")
        print("------------------------------------------------")

        file_path = "data.xlsx"
        if not os.path.exists(file_path):
            work_book = openpyxl.Workbook()
            sheet = work_book.active
            heading = ["First_Name", "Last_Name", "Title", "Age",
                       "Nationality", "# Courses", "# Semesters",
                       "Registration Status"]
            sheet.append(heading)
            work_book.save(file_path)
        work_book = openpyxl.load_workbook(file_path)
        sheet = work_book.active
        sheet.append([first_name, last_name, title, age, nationality,
                     numcourses, numsemesters, registration_status])
        work_book.save(file_path)
    else:
        print("Error")


window = tkinter.Tk()
window.title("Data Entry Form")
frame = tkinter.Frame(window)
frame.pack()

# User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=[
                              "Ramp Agent", "GSE Op", "A/C Loader"])
title.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(
    user_info_frame, values=["Asian", "American", "European", "African"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(
    courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)


numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept Terms

terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)


accept_term_status_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(
    terms_frame, text="I Accept the terms And Conditions.", variable=accept_term_status_var,
    onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)


# Button

button = tkinter.Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()
