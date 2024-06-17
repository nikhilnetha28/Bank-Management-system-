import tkinter as tk
from tkinter import messagebox
import mysql.connector
from flask import Flask, render_template, redirect, url_for
from subprocess import call
import os

app = Flask(__name__)

# Function to check credentials against the database
def check_credentials(account_number, dob, phone_number):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="nikhil",
            password="nikhil",
            database="b"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query to check credentials
            query = """
            SELECT * FROM bank
            WHERE account_number = %s AND dob = %s AND phone = %s
            """
            data = (account_number, dob, phone_number)

            cursor.execute(query, data)
            result = cursor.fetchone()

            if result:
                return True  # Credentials are valid

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

    return False  # Credentials are invalid

def open_phonepay_interface():
    # Change the current working directory to the directory of acc.py
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)

    # Open the PhonePay interface (acc.py)
    call(["python", "acc.py"])

def open_account_page():
    # Redirect to the /account route
    return redirect(url_for("account"))

def login():
    account_number = entry_account_number.get()
    dob = entry_dob.get()
    phone_number = entry_phone_number.get()

    # Check credentials against the database
    if check_credentials(account_number, dob, phone_number):
        # Show success message
        messagebox.showinfo("Success", "Login successful!")

        # Open the PhonePay interface (acc.py)
        open_phonepay_interface()

    else:
        # Show error message
        messagebox.showerror("Error", "Invalid credentials")

# Create the main window
root = tk.Tk()
root.title("Login")

background_color = "#D2B48C"
text_color = "#000080"
font_size = 16

root.configure(bg=background_color)

label_account_number = tk.Label(root, text="Account Number:", bg=background_color, fg=text_color, font=("Arial", font_size))
label_dob = tk.Label(root, text="Date of Birth:", bg=background_color, fg=text_color, font=("Arial", font_size))
label_phone_number = tk.Label(root, text="Phone Number:", bg=background_color, fg=text_color, font=("Arial", font_size))

entry_account_number = tk.Entry(root, font=("Arial", font_size))
entry_dob = tk.Entry(root, font=("Arial", font_size))
entry_phone_number = tk.Entry(root, font=("Arial", font_size))

login_button = tk.Button(root, text="Login", command=login, bg="#006400", fg="white", font=("Arial", font_size))

label_account_number.grid(row=0, column=0, pady=10, padx=10, sticky="e")
entry_account_number.grid(row=0, column=1, pady=10, padx=10, sticky="w")
label_dob.grid(row=1, column=0, pady=10, padx=10, sticky="e")
entry_dob.grid(row=1, column=1, pady=10, padx=10, sticky="w")
label_phone_number.grid(row=2, column=0, pady=10, padx=10, sticky="e")
entry_phone_number.grid(row=2, column=1, pady=10, padx=10, sticky="w")

login_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
