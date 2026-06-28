import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to fetch package status and notify customer
def notify_customer():
    tracking_id = tracking_id_entry.get()
    
    if not tracking_id.isdigit():
        messagebox.showerror("Error", "Tracking ID must be a number!")
        return
    
    conn = sqlite3.connect("courier.db")
    cursor = conn.cursor()
    cursor.execute("SELECT receiver_name, contact_number, status FROM packages WHERE tracking_id = ?", (tracking_id,))
    package = cursor.fetchone()
    conn.close()
    
    if package:
        receiver, contact, status = package
        message = f"Dear {receiver}, your package (ID: {tracking_id}) is currently '{status}'. For more info, contact support."
        messagebox.showinfo("Notification", message)
    else:
        messagebox.showerror("Error", "Package not found!")

# GUI Setup
root = tk.Tk()
root.title("Customer Notifications")
root.geometry("400x200")

tk.Label(root, text="Enter Tracking ID:").pack()
tracking_id_entry = tk.Entry(root)
tracking_id_entry.pack()

tk.Button(root, text="Notify Customer", command=notify_customer).pack()

root.mainloop()