import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to fetch and display package details
def fetch_package():
    tracking_id = tracking_id_entry.get()
    if not tracking_id.isdigit():
        messagebox.showerror("Error", "Tracking ID must be a number!")
        return
    
    conn = sqlite3.connect("courier.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM packages WHERE tracking_id = ?", (tracking_id,))
    package = cursor.fetchone()
    conn.close()
    
    if package:
        status_var.set(package[6])
        package_details.set(f"Sender: {package[1]}, Receiver: {package[2]}, Status: {package[6]}")
    else:
        messagebox.showerror("Error", "Package not found!")

# Function to update package status
def update_status():
    tracking_id = tracking_id_entry.get()
    new_status = status_var.get()
    
    if not tracking_id.isdigit():
        messagebox.showerror("Error", "Tracking ID must be a number!")
        return
    
    conn = sqlite3.connect("courier.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE packages SET status = ? WHERE tracking_id = ?", (new_status, tracking_id))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Package status updated!")
    fetch_package()

# GUI Setup
root = tk.Tk()
root.title("Tracking Updates")
root.geometry("400x300")

tk.Label(root, text="Enter Tracking ID:").pack()
tracking_id_entry = tk.Entry(root)
tracking_id_entry.pack()

tk.Button(root, text="Fetch Package", command=fetch_package,bg="deepskyblue").pack()

package_details = tk.StringVar()
tk.Label(root, textvariable=package_details, wraplength=350).pack()

status_var = tk.StringVar()
tk.Label(root, text="Update Status:").pack()
status_options = ["Registered", "In Transit", "Out for Delivery", "Delivered"]
status_menu = tk.OptionMenu(root, status_var, *status_options)
status_menu.pack()

tk.Button(root, text="Update Status", command=update_status,bg="red").pack()

root.mainloop()