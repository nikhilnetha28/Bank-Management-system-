import tkinter as tk
from tkinter import simpledialog, messagebox

class BankAccountGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account GUI")

        self.account_holder_label = tk.Label(root, text="Account Holder:")
        self.account_holder_label.grid(row=0, column=0, padx=10, pady=10)

        self.account_holder_entry = tk.Entry(root)
        self.account_holder_entry.grid(row=0, column=1, padx=10, pady=10)

        self.account_number_label = tk.Label(root, text="Account Number:")
        self.account_number_label.grid(row=1, column=0, padx=10, pady=10)

        self.account_number_entry = tk.Entry(root)
        self.account_number_entry.grid(row=1, column=1, padx=10, pady=10)

        self.create_account_button = tk.Button(root, text="use above Account", command=self.create_account)
        self.create_account_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.credit_button = tk.Button(root, text="Credit", command=self.credit)
        self.credit_button.grid(row=3, column=0, padx=10, pady=10)

        self.debit_button = tk.Button(root, text="Debit", command=self.debit)
        self.debit_button.grid(row=3, column=1, padx=10, pady=10)

        self.check_balance_button = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.transaction_history_button = tk.Button(root, text="Transaction History", command=self.view_transaction_history)
        self.transaction_history_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.bank_account = None

    def create_account(self):
        account_holder = self.account_holder_entry.get()
        account_number = self.account_number_entry.get()
        self.bank_account = BankAccount(account_holder, account_number)

    def credit(self):
        if self.bank_account:
            amount = simpledialog.askfloat("Credit", "Enter the amount to credit:")
            if amount is not None:
                self.show_credit_widgets(amount)
        else:
            messagebox.showwarning("Warning", "Enter the account holder name and account number first.")

    def show_credit_widgets(self, amount):
        self.to_label = tk.Label(self.root, text="Money receving from ac no:")
        self.to_label.grid(row=6, column=0, padx=10, pady=10)

        self.to_entry = tk.Entry(self.root)
        self.to_entry.grid(row=6, column=1, padx=10, pady=10)

        self.credit_button.config(state=tk.DISABLED)
        self.debit_button.config(state=tk.DISABLED)

        confirm_button = tk.Button(self.root, text="Confirm", command=lambda: self.confirm_credit(amount))
        confirm_button.grid(row=7, column=0, columnspan=2, pady=10)

    def confirm_credit(self, amount):
        to_account = self.to_entry.get()
        self.bank_account.credit(amount, to_account)
        messagebox.showinfo("Credit", f"Amount credited successfully to {to_account}.")
        self.clear_credit_widgets()

    def clear_credit_widgets(self):
        self.to_label.destroy()
        self.to_entry.destroy()
        self.credit_button.config(state=tk.NORMAL)
        self.debit_button.config(state=tk.NORMAL)

    def debit(self):
        if self.bank_account:
            amount = simpledialog.askfloat("Debit", "Enter the amount to debit:")
            if amount is not None:
                self.show_debit_widgets(amount)
        else:
            messagebox.showwarning("Warning", "Enter the account holder name and account number first.")

    def show_debit_widgets(self, amount):
        self.from_label = tk.Label(self.root, text="Money sending ac no:")
        self.from_label.grid(row=6, column=0, padx=10, pady=10)

        self.from_entry = tk.Entry(self.root)
        self.from_entry.grid(row=6, column=1, padx=10, pady=10)

        self.credit_button.config(state=tk.DISABLED)
        self.debit_button.config(state=tk.DISABLED)

        confirm_button = tk.Button(self.root, text="Confirm", command=lambda: self.confirm_debit(amount))
        confirm_button.grid(row=7, column=0, columnspan=2, pady=10)

    def confirm_debit(self, amount):
        from_account = self.from_entry.get()
        self.bank_account.debit(amount, from_account)
        self.clear_debit_widgets()

    def clear_debit_widgets(self):
        self.from_label.destroy()
        self.from_entry.destroy()
        self.credit_button.config(state=tk.NORMAL)
        self.debit_button.config(state=tk.NORMAL)

    def check_balance(self):
        if self.bank_account:
            balance = self.bank_account.check_balance()
            messagebox.showinfo("Balance", balance)
        else:
            messagebox.showwarning("Warning", "Enter the account holder name and account number first.")

    def view_transaction_history(self):
        if self.bank_account:
            history = self.bank_account.view_transaction_history()
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showwarning("Warning", "Enter the account holder name and account number first.")

class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []

    def credit(self, amount, to_account):
        self.balance += amount
        self.transaction_history.append(f"Credit: +${amount} to {to_account}")

    def debit(self, amount, from_account):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Debit: -${amount} from {from_account}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return f"Current Balance: ${self.balance}"

    def view_transaction_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        else:
            return "\n".join(self.transaction_history)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankAccountGUI(root)
    root.mainloop()
