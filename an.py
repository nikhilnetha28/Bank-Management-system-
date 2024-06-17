import tkinter as tk
from tkinter import messagebox
import mysql.connector
import random

def submit_registration():
    name_value = entry_name.get()
    father_name_value = entry_father_name.get()
    phone_value = entry_phone.get()
    dob_value = entry_dob.get()
    adhar_value = entry_adhar.get()
    pan_value = entry_pan.get()
    address_value = entry_address.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="nikhil",
            password="nikhil",
            database="b"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Generate a 6-digit account number
            account_number = str(random.randint(100000, 999999))

            # Insert data into the bank table
            insert_data_query = """
            INSERT INTO bank (account_number, name, father_name, phone, dob, adhar, pan, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (account_number, name_value, father_name_value, phone_value, dob_value, adhar_value, pan_value, address_value)

            cursor.execute(insert_data_query, data)
            connection.commit()

            # Show success message
            messagebox.showinfo("Success", f"Account successfully created!\nAccount Number: {account_number}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        # Show error message
        messagebox.showerror("Error", f"Failed to create account: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

root = tk.Tk()
root.title("Bank Registration Form")
root.geometry("500x400")  # Set the frame size

# Styling
background_color = "#3498db"  # Light blue
text_color = "#ffffff"  # White
entry_bg_color = "#ecf0f1"  # Light gray
button_bg_color = "#2ecc71"  # Green
button_fg_color = "#ffffff"  # White
pad_value = 10

root.configure(bg=background_color)

# Labels
label_name = tk.Label(root, text="Name:", bg=background_color, fg=text_color, font=("Helvetica", 14))
label_father_name = tk.Label(root, text="Father's Name:", bg=background_color, fg=text_color, font=("Helvetica", 14))
label_phone = tk.Label(root, text="Phone:", bg=background_color, fg=text_color, font=("Helvetica", 14))
label_dob = tk.Label(root, text="Date of Birth:", bg=background_color, fg=text_color, font=("Helvetica", 14))
label_adhar = tk.Label(root, text="Aadhar No:", bg=background_color, fg=text_color, font=("Helvetica", 14))
label_pan = tk.Label(root, text="PAN No:", bg=background_color, fg=text_color, font=("Helvetica", 14))
label_address = tk.Label(root, text="Address:", bg=background_color, fg=text_color, font=("Helvetica", 14))

# Entry widgets
entry_name = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 14))
entry_father_name = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 14))
entry_phone = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 14))
entry_dob = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 14))
entry_adhar = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 14))
entry_pan = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 14))
entry_address = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 14))

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_registration, bg=button_bg_color, fg=button_fg_color, font=("Helvetica", 14))

# Center the labels and entries in the middle
label_name.grid(row=0, column=0, pady=pad_value, sticky="e")
entry_name.grid(row=0, column=1, pady=pad_value, sticky="w")
label_father_name.grid(row=1, column=0, pady=pad_value, sticky="e")
entry_father_name.grid(row=1, column=1, pady=pad_value, sticky="w")
label_phone.grid(row=2, column=0, pady=pad_value, sticky="e")
entry_phone.grid(row=2, column=1, pady=pad_value, sticky="w")
label_dob.grid(row=3, column=0, pady=pad_value, sticky="e")
entry_dob.grid(row=3, column=1, pady=pad_value, sticky="w")
label_adhar.grid(row=4, column=0, pady=pad_value, sticky="e")
entry_adhar.grid(row=4, column=1, pady=pad_value, sticky="w")
label_pan.grid(row=5, column=0, pady=pad_value, sticky="e")
entry_pan.grid(row=5, column=1, pady=pad_value, sticky="w")
label_address.grid(row=6, column=0, pady=pad_value, sticky="e")
entry_address.grid(row=6, column=1, pady=pad_value, sticky="w")

submit_button.grid(row=7, column=0, columnspan=2, pady=pad_value)

root.mainloop()
