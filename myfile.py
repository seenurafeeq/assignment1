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
        account_button = Button(welcome_window, text="Create an account")
        account_button.pack(padx=10, pady=10)
        withdraw_button = Button(welcome_window, text="Withdraw Cash", command=open_withdraw_page)
        withdraw_button.pack(padx=10, pady=10)
        deposite_button = Button(welcome_window, text="Deposit Cash")
        deposite_button.pack(padx=10, pady=10)
        transfer_button = Button(welcome_window, text="Transfer from different accounts")
        transfer_button.pack(padx=10, pady=10)
        viewaccount_button = Button(welcome_window, text="View account details")
        viewaccount_button.pack(padx=10, pady=10)
    else:
        messagebox.showerror("Login Error", "Incorrect username or password.")

# define a function for withdraw money
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
    withdraw_button.pack(padx=10, pady=10)

# Create a button to submit the login credentials
login_button = Button(window, text="Login", command=check_login)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the window
window.mainloop()
