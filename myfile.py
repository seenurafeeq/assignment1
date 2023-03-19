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

# Create a label for the password
password_label = Label(window, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)

# Create an entry box for the password
password_entry = Entry(window, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Define a function to check the login credentials
def check_login():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "Haseena" and password == "123":
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
        transfer_button = Button(welcome_window, text="Transfer from different accounts")
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
    # Bind the create button to the create function
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
    deposit_button.pack(padx=10, pady=10)


#save account
# Define the file name and field names
file_name = "accounts.csv"
field_names = ["username", "password", "account_number", "balance"]

def save_account(username, password, account_number, balance):
    # Open the CSV file in append mode
    with open(file_name, mode="a", newline="") as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the account details to a new row in the file
        writer.writerow([username, password, account_number, balance])

#define a function to view account details
def view_account_details():
    # Get the username entered by the user
    username = username_entry.get()

    # Check if the username exists in the accounts dictionary
    if username in accounts:
        # Get the account details for the given username
        account_details = accounts[username]
        
        # Create a new window to display the account details
        details_window = Toplevel()
        details_window.title("Account Details")
        details_window.geometry("500x350")
        
        # Add widgets to the account details window
        details_label = Label(details_window, text="Account Details for " + username)
        details_label.pack(padx=10, pady=10)
        account_number_label = Label(details_window, text="Account Number: " + str(account_details["account_number"]))
        account_number_label.pack(padx=10, pady=10)
        balance_label = Label(details_window, text="Balance: " + str(account_details["balance"]))
        balance_label.pack(padx=10, pady=10)
    else:
        messagebox.showerror("Account Details Error", "Username does not exist.")
# Create a button to submit the login credentials
login_button = Button(window, text="Login", command=check_login)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the window
window.mainloop()
