import tkinter as tk
from tkinter import messagebox
import json
from secrets import compare_digest


class LoginInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Login')

        # Set background and text colors
        bg_color = "#1E1E1E"
        text_color = "#FFFFFF"

        # Set window width and height
        window_width = 400
        window_height = 300

        # Calculate center position for window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        # Set window size and position
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.root.configure(bg=bg_color)

        # Create UI elements
        self.username_label = tk.Label(self.root, text='Username:', font=('Arial', 12), bg=bg_color, fg=text_color)
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self.root, font=('Arial', 12))
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text='Password:', font=('Arial', 12), bg=bg_color, fg=text_color)
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.root, show='*', font=('Arial', 12))
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text='Login', command=self.login, font=('Arial', 12), bg='#66b2fb', fg=text_color)
        self.login_button.pack(pady=20)

        self.logged_in = False

    def run(self):
        self.root.mainloop()
        return self.logged_in

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Load user data from the JSON file
        with open('user.json', 'r') as file:
            data = json.load(file)

        # Check if the entered credentials match any user in the data
        for user in data['users']:
            if user['username'] == username and compare_digest (user['password'], password):
                self.logged_in = True
                # Hide the login window
                self.root.withdraw()
                self.root.quit()
                return




                return

        # Login failed, display error message
        messagebox.showerror('Login Failed', 'Invalid username or password')
