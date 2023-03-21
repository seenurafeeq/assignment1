from tkinter import *
from tkinter import messagebox

# Create a window
window = Tk()
window.title("Login ")
window.geometry("500x350")
# Set the background color of the window
window.config(bg="purple")
# Create a label for the username
username_label = Label(window, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)
# Create an entry box for the username
username_entry = Entry(window)
username_entry.grid(row=1, column=1, padx=10, pady=10)
# Create a label for the account number
accountnumber_label = Label(window, text="Account Number:")
accountnumber_label.grid(row=2, column=0, padx=10, pady=10)
# Create an entry box for the account number
accountnumber_entry = Entry(window, show="*")
accountnumber_entry.grid(row=2, column=1, padx=10, pady=10)
# Create a label for the account type
accounttype_label = Label(window, text="Account Type:")
accounttype_label.grid(row=3, column=0, padx=10, pady=10)
# Create an entry box for the account type
accounttype_entry = Entry(window, text="Account Type")
accounttype_entry.grid(row=3, column=1, padx=10, pady=10)

# Define a function to check the login credentials
def check_login():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = accountnumber_entry.get()
    # Check if the username and password are correct
    if username == "Haseena" and password == "123456789":
        # Destroy the login window and create a new window with a welcome message
        window.destroy()
        welcome_window = Tk()
        welcome_window.title("Welcome Page")
        welcome_window.geometry("500x350")
        welcome_window.config(bg="orange")
        welcome_label = Label(welcome_window, text="Welcome, " + username + "!", fg="red", font=("Helvetica", 16, "bold"))
        welcome_label.pack(padx=10, pady=10)
        account_button = Button(welcome_window, text="Create an account", command=create_account)
        account_button.pack(padx=10, pady=10)
        withdraw_button = Button(welcome_window, text="Withdraw Cash", command=open_withdraw_page)
        withdraw_button.pack(padx=10, pady=10)
        deposit_button = Button(welcome_window, text="Deposit Cash", command=open_deposit_page)
        deposit_button.pack(padx=10, pady=10)
        transfer_button = Button(welcome_window, text="Transfer from different accounts", command=transfer_money)
        transfer_button.pack(padx=10, pady=10)
        viewaccount_button = Button(welcome_window, text="View account details", command=view_account_details)
        viewaccount_button.pack(padx=10, pady=10)
    else:
        messagebox.showerror("Login Error", "Incorrect username or password.")


#define a function to create account
def create_account():
    # Create a new window for the account creation page
    account_window = Toplevel()
    account_window.title("Create Account")
    account_window.geometry("500x350")
    # Add widgets to the account creation page
    account_label = Label(account_window, text="Create Account")
    account_label.pack(padx=10, pady=10)
    name_label = Label(account_window, text="Enter name:")
    name_label.pack(padx=10, pady=10)
    name_entry = Entry(account_window)
    name_entry.pack(padx=10, pady=10)
    balance_label = Label(account_window, text="Enter initial balance:")
    balance_label.pack(padx=10, pady=10)
    balance_entry = Entry(account_window)
    balance_entry.pack(padx=10, pady=10)
    create_button = Button(account_window, text="Create Account")
    create_button.pack(padx=10, pady=10)
    # Define a function to create the account when the create button is clicked
    def create():
        name = name_entry.get()
        balance = float(balance_entry.get())
        # Close the account creation window
        account_window.destroy()
        # Show a message box to confirm that the account was created
        messagebox.showinfo("Account Created", f"Account for {name} created with initial balance {balance}.")
        #Bind the create button to the create function
    create_button.config(command=create)
    

# define a function to withdraw money
def open_withdraw_page():
    # Create a new window for the withdraw page
    withdraw_window = Toplevel()
    withdraw_window.title("Withdraw Page")
    withdraw_window.geometry("500x350")

    # Add widgets to the withdraw page
    withdraw_label = Label(withdraw_window, text="Withdraw Money")
    withdraw_label.pack(padx=10, pady=10)
    amount_label = Label(withdraw_window, text="Enter amount:")
    amount_label.pack(padx=10, pady=10)
    amount_entry = Entry(withdraw_window)
    amount_entry.pack(padx=10, pady=10)
    withdraw_button = Button(withdraw_window, text="Withdraw")
    # Define a function to withdraw the amount from the user's account
    def withdrawal():
            withdraw_window.destroy()
            messagebox.showinfo("Withdrawal", f"Withdrawal successful.")
    withdraw_button.config(command=withdrawal)
    withdraw_button.pack(padx=10, pady=10)


# define a function to deposit money
def open_deposit_page():
    # Create a new window for the deposit page
    deposit_window = Toplevel()
    deposit_window.title("Deposit Page")
    deposit_window.geometry("500x350")
    
    # Add widgets to the deposit page
    deposit_label = Label(deposit_window, text="Deposit Money")
    deposit_label.pack(padx=10, pady=10)
    amount_label = Label(deposit_window, text="Enter amount:")
    amount_label.pack(padx=10, pady=10)
    amount_entry = Entry(deposit_window)
    amount_entry.pack(padx=10, pady=10)
    deposit_button = Button(deposit_window, text="Deposit")
    
    # Define a function to deposit the amount to the user's account
    def deposit():
        deposit_window.destroy()
        messagebox.showinfo("Deposit", f"Deposit successful.")
    
    deposit_button.config(command=deposit)
    deposit_button.pack(padx=10, pady=10)


# define a function to transfer money
def transfer_money():
    # Create a new window for the transfer page
    transfer_window = Toplevel()
    transfer_window.title("Transfer Page")
    transfer_window.geometry("500x350")

    # Add widgets to the transfer page
    transfer_label = Label(transfer_window, text="Transfer Money")
    transfer_label.pack(padx=10, pady=10)
    account_number_label = Label(transfer_window, text="Enter account number to transfer to:")
    account_number_label.pack(padx=10, pady=10)
    account_number_entry = Entry(transfer_window)
    account_number_entry.pack(padx=10, pady=10)
    amount_label = Label(transfer_window, text="Enter amount:")
    amount_label.pack(padx=10, pady=10)
    amount_entry = Entry(transfer_window)
    amount_entry.pack(padx=10, pady=10)
    transfer_button = Button(transfer_window, text="Transfer") 
    def transfer():
        transfer_window.destroy()
        messagebox.showinfo("Transfer", f"Transfer successful.")
    
    transfer_button.config(command=transfer)
    transfer_button.pack(padx=10, pady=10)

    # Define a function to transfer the amount from the user's account to another account
    # Create a dictionary to store account details


#define a function to view account details
def view_account_details():
    account_info = {
        "Account Number": "123456789",
        "Account Type": "Savings",
        "Name": "Haseena",
        "Balance": "$1000",
    }
    
    # Create a new window to display the account information
    account_window = Toplevel()
    account_window.title("Account Details")
    account_window.geometry("300x200")

    # Create labels to display the account information
    for i, (key, value) in enumerate(account_info.items()):
        label = Label(account_window, text=f"{key}: {value}")
        label.grid(row=i, column=0, padx=10, pady=5)

# Create a button to submit the login credentials
login_button = Button(window, text="Login", command=check_login)
login_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the window
window.mainloop()
