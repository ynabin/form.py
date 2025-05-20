import tkinter as tk
from tkinter import ttk

def submit_form():
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    form_number = form_number_entry.get()
    contact_number = contact_number_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END)

    print("Name:", name)
    print("Course:", course)
    print("Semester:", semester)
    print("Form Number:", form_number)
    print("Contact Number:", contact_number)
    print("Email:", email)
    print("Address:", address)

    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    form_number_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)

window = tk.Tk()
window.title("Registration Form")

name_label = ttk.Label(window, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(window)
name_entry.grid(row=0, column=1)

course_label = ttk.Label(window, text="Course:")
course_label.grid(row=1, column=0, sticky=tk.W)
course_entry = ttk.Entry(window)
course_entry.grid(row=1, column=1)

semester_label = ttk.Label(window, text="Semester:")
semester_label.grid(row=2, column=0, sticky=tk.W)
semester_entry = ttk.Entry(window)
semester_entry.grid(row=2, column=1)

form_number_label = ttk.Label(window, text="Form Number:")
form_number_label.grid(row=3, column=0, sticky=tk.W)
form_number_entry = ttk.Entry(window)
form_number_entry.grid(row=3, column=1);

contact_number_label = ttk.Label(window, text="Contact Number:")
contact_number_label.grid(row=4, column=0, sticky=tk.W)
contact_number_entry = ttk.Entry(window)
contact_number_entry.grid(row=4, column=1)

email_label = ttk.Label(window, text="Email:")
email_label.grid(row=5, column=0, sticky=tk.W)
email_entry = ttk.Entry(window)
email_entry.grid(row=5, column=1)


address_label = ttk.Label(window, text="Address:")
address_label.grid(row=6, column=0, sticky=tk.W)
address_entry = tk.Text(window, height=3, width=20)
address_entry.grid(row=6, column=1)

submit_button = ttk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=7, column=1, sticky=tk.E)

window.mainloop()