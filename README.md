# Courier Tracking System

A lightweight desktop application for registering packages, tracking their delivery status, and notifying customers — built with Python, Tkinter, and SQLite.

## Features

- **Package Registration** — Register a new package with sender, receiver, destination address, contact number, and weight; details are saved to a local SQLite database.
- **Tracking Updates** — Look up any package by its Tracking ID and update its current status.
- **Delivery Confirmation** — Mark a package as `Delivered`, with a check to prevent duplicate confirmations.
- **Customer Notifications** — Simulate notifying a customer with their package's current status.

## Tech Stack

- **Python 3**
- **Tkinter** — GUI
- **SQLite3** — local database storage

## Project Structure

```
Courier Tracking System/
├── main.py                     # Dashboard that launches all modules
├── package_registration.py     # Register new packages
├── tracking_updates.py         # Search and update package status
├── delivery_confirmation.py    # Confirm package delivery
├── customer_notifications.py   # Simulate customer status notifications
└── courier.db                  # SQLite database (auto-created on first run)
```

## Getting Started

### Prerequisites

- Python 3.7+
- Tkinter (bundled with most Python installs; on Linux: `sudo apt-get install python3-tk`)

No third-party packages are required — everything runs on Python's standard library.

### Installation

```bash
git clone https://github.com/<your-username>/courier-tracking-system.git
cd "Courier Tracking System"
python main.py
```

## Usage

1. Run `main.py` to open the main dashboard.
2. **Package Registration** — fill in sender, receiver, address, contact, and weight, then submit to register a package.
3. **Tracking Updates** — enter a Tracking ID to fetch package details and update its status (`Registered` → `In Transit` → `Out for Delivery` → `Delivered`).
4. **Delivery Confirmation** — enter a Tracking ID to mark it as delivered.
5. **Customer Notifications** — enter a Tracking ID to view a simulated notification with the package's current status.

Each module can also be launched independently:

```bash
python package_registration.py
python tracking_updates.py
python delivery_confirmation.py
python customer_notifications.py
```

## Database Schema

**Table:** `packages`

| Column               | Type    | Description                              |
|----------------------|---------|-------------------------------------------|
| tracking_id          | INTEGER | Primary key, auto-incremented             |
| sender_name          | TEXT    | Name of the sender                        |
| receiver_name        | TEXT    | Name of the receiver                      |
| destination_address  | TEXT    | Delivery address                          |
| contact_number       | TEXT    | Receiver's contact number                 |
| package_weight       | REAL    | Package weight (kg)                       |
| status               | TEXT    | `Registered`, `In Transit`, `Out for Delivery`, or `Delivered` |

## Roadmap

- [ ] Real SMS/email notifications (e.g. Twilio, SMTP) instead of popup simulation
- [ ] Web-based interface (Flask/Django) as an alternative to the Tkinter GUI
- [ ] Authentication for couriers vs. admin users
- [ ] Live shipment tracking / map view

## License

This project is open source and available under the [MIT License](LICENSE).
