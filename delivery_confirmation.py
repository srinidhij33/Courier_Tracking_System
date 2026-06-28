import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to confirm package delivery
def confirm_delivery():
    tracking_id = tracking_id_entry.get()
    
    if not tracking_id.isdigit():
        messagebox.showerror("Error", "Tracking ID must be a number!")
        return
    
    conn = sqlite3.connect("courier.db")
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM packages WHERE tracking_id = ?", (tracking_id,))
    package = cursor.fetchone()
    
    if not package:
        messagebox.showerror("Error", "Package not found!")
        conn.close()
        return
    
    if package[0] == "Delivered":
        messagebox.showinfo("Info", "This package is already marked as delivered.")
    else:
        cursor.execute("UPDATE packages SET status = 'Delivered' WHERE tracking_id = ?", (tracking_id,))
        conn.commit()
        messagebox.showinfo("Success", "Package marked as delivered!")
    
    conn.close()

# GUI Setup
root = tk.Tk()
root.title("Delivery Confirmation")
root.geometry("350x200")

tk.Label(root, text="Enter Tracking ID:").pack()
tracking_id_entry = tk.Entry(root)
tracking_id_entry.pack()

tk.Button(root, text="Confirm Delivery", command=confirm_delivery).pack()

root.mainloop()