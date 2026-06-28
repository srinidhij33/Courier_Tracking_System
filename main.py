import tkinter as tk
import subprocess

# Functions to open individual modules
def open_package_registration():
    subprocess.Popen(["python", "package_registration.py"])

def open_tracking_updates():
    subprocess.Popen(["python", "tracking_updates.py"])

def open_delivery_confirmation():
    subprocess.Popen(["python", "delivery_confirmation.py"])

def open_customer_notifications():
    subprocess.Popen(["python", "customer_notifications.py"])

# Main GUI Setup
root = tk.Tk()
root.title("Courier Tracking System")
root.geometry("400x300")

tk.Label(root, text="Courier Tracking System", font=("Arial", 14, "bold")).pack(pady=10)

# Buttons to launch modules
tk.Button(root, text="Package Registration", command=open_package_registration).pack(pady=5)
tk.Button(root, text="Tracking Updates", command=open_tracking_updates).pack(pady=5)
tk.Button(root, text="Delivery Confirmation", command=open_delivery_confirmation).pack(pady=5)
tk.Button(root, text="Customer Notifications", command=open_customer_notifications).pack(pady=5)

root.mainloop()