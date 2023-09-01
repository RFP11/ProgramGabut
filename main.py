import tkinter as tk
from tkinter import messagebox, PhotoImage
import random

error_popups = []

def show_custom_error():
    error_popup = tk.Toplevel(root)
    error_popup.title("Error")
    error_popup.geometry("200x100")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = random.randint(0, screen_width - 200)  # 200 is the width of the error pop-up
    y = random.randint(0, screen_height - 100)  # 100 is the height of the error pop-up
    error_popup.geometry(f"200x100+{x}+{y}")

    label = tk.Label(error_popup, text="Invalid Password!")
    label.pack(padx=20, pady=20)
    
    ok_button = tk.Button(error_popup, text="OK", command=error_popup.destroy)
    ok_button.pack()

    error_popups.append(error_popup)


def close_error_popups():
    for popup in error_popups:
        try:
            popup.destroy()  # Destroy the pop-up if it still exists
        except tk.TclError:
            pass  # Handle the case where the pop-up is already destroyed


def show_message(name):
    profile_popup = tk.Toplevel(root)
    profile_popup.title("My Biography Profile")
    profile_popup.geometry("500x500")

    # Create a Canvas widget for image display
    canvas = tk.Canvas(profile_popup, width=200, height=200)
    canvas.pack(padx=20, pady=10)

    # Load and display an image on the Canvas (replace 'your_image.gif' with your image file)
    image = PhotoImage(file="profile.png")  # Replace with your image file
    resized_image = image.subsample(3)  # Resize the image (adjust the factor as needed)
    canvas.create_image(0, 0, anchor=tk.NW, image=resized_image)
    canvas.image = resized_image  # Keep a reference to the image

    # Add your biography information here
    bio_text = f"""
    Name: {name}
    Age: 17
    Hobbies: Code
    Bio: Junior Programmer
    """

    label = tk.Label(profile_popup, text="Biography Profile", font=("Helvetica", 16, "bold"))
    label.pack(padx=20, pady=20)

    bio_label = tk.Label(profile_popup, text=bio_text, justify=tk.LEFT)
    bio_label.pack(padx=20, pady=10)

    # Add a button to exit the application
    exit_button = tk.Button(profile_popup, text="Exit", command=exit_application)
    exit_button.pack(padx=20, pady=10)


def exit_application():
    root.quit()

# Function to check login credentials
def crack():
    username = username_entry.get()
    password = password_entry.get()

    if username != "M Rafly Pratama":
        messagebox.showerror("Error", "Invalid Username")
    elif len(password) == 0:
        messagebox.showerror("Error", "Password can't be empty")
    else:
        # root.withdraw()
        for popup in range(1, 50):
            print(popup)
            root.after(100, show_custom_error)  # Delay in milliseconds
            delay = popup * 15

        # After all error pop-ups are displayed, show the message
        def show_message_after_errors():
            close_error_popups()
            messagebox.showinfo("Success", f"You are loged in as {username}")
            show_message(username)

        root.after(delay, show_message_after_errors) 
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username != "M Rafly Pratama":
        messagebox.showerror("Error", "Invalid Username")
    elif len(password) == 0:
        messagebox.showerror("Error", "Password can't be empty")
    elif password != "MyUsualPassword":
        messagebox.showerror("Error", "Invalid Password")
    else:
        show_message(username)


# Create the main window
root = tk.Tk()
root.title("Login Interface")
root.geometry("400x300")

# Create labels and entry widgets for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show='*')  # The password is hidden with asterisks
password_entry.pack(pady=5)

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

login_button = tk.Button(root, text="Crack Login", command=crack)
login_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
