import tkinter as tk
from tkinter import messagebox

# פונקציה שתהיה מוקשרת לכפתור
def on_add_customer():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    
    # פשוט מציג הודעה עם המידע שהוזן
    messagebox.showinfo("Customer Added", f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}")

# יצירת חלון ראשי
root = tk.Tk()
root.title("Customer Management System")

# יצירת תוויות
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=10)

# יצירת תיבות טקסט
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=10)

# יצירת כפתור
add_button = tk.Button(root, text="Add Customer", command=on_add_customer)
add_button.grid(row=4, column=0, columnspan=2, pady=20)

# הפעלת חלון Tkinter
root.mainloop()

