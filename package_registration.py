import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Setup
def initialize_db():
    conn = sqlite3.connect("courier.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS packages (
                        tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sender_name TEXT,
                        receiver_name TEXT,
                        destination_address TEXT,
                        contact_number TEXT,
                        package_weight REAL,
                        status TEXT DEFAULT 'Registered')''')
    conn.commit()
    conn.close()

# Function to register package
def register_package():
    sender = sender_entry.get()
    receiver = receiver_entry.get()
    address = address_entry.get()
    contact = contact_entry.get()
    weight = weight_entry.get()
    
    if not (sender and receiver and address and contact and weight):
        messagebox.showerror("Error", "All fields must be filled!")
        return
    
    try:
        weight = float(weight)
    except ValueError:
        messagebox.showerror("Error", "Package weight must be a number!")
        return
    
    conn = sqlite3.connect("courier.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO packages (sender_name, receiver_name, destination_address, contact_number, package_weight, status) VALUES (?, ?, ?, ?, ?, ?)",
                   (sender, receiver, address, contact, weight, "Registered"))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Package Registered Successfully!")
    display_packages()
    clear_fields()

# Function to display registered packages
def display_packages():
    conn = sqlite3.connect("courier.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM packages")
    rows = cursor.fetchall()
    conn.close()
    
    package_list.delete(0, tk.END)
    for row in rows:
        package_list.insert(tk.END, f"ID: {row[0]}, Sender: {row[1]}, Receiver: {row[2]}, Status: {row[6]}")

# Function to clear input fields
def clear_fields():
    sender_entry.delete(0, tk.END)
    receiver_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Package Registration")
root.geometry("500x500")

initialize_db()

tk.Label(root, text="Sender Name:").pack()
sender_entry = tk.Entry(root)
sender_entry.pack()

tk.Label(root, text="Receiver Name:").pack()
receiver_entry = tk.Entry(root)
receiver_entry.pack()

tk.Label(root, text="Destination Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Label(root, text="Contact Number:").pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

tk.Label(root, text="Package Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="Register Package", command=register_package).pack()

package_list = tk.Listbox(root, width=60)
package_list.pack()

tk.Button(root, text="Refresh List", command=display_packages).pack()

display_packages()
root.mainloop()
