import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Submit form handler
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    gender = gender_var.get()
    password = entry_password.get()

    if not name or not email or not age or not gender or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    messagebox.showinfo("Success", f"Registration Successful!\n\nName: {name}\nEmail: {email}")

# Toggle fullscreen (optional button)
def toggle_fullscreen():
    current = app.attributes('-fullscreen')
    app.attributes('-fullscreen', not current)

# Create the main window
app = ttk.Window(themename="cosmo")  # Change theme to "darkly" for dark mode
app.title("🌟 User Registration Form")
app.attributes('-fullscreen', True)  # Start in fullscreen mode

# Header
ttk.Label(app, text="User Registration Form", font=("Helvetica", 30, "bold")).pack(pady=40)

# Form Container
form_frame = ttk.Frame(app, padding=20)
form_frame.pack(pady=20)

# Name
ttk.Label(form_frame, text="Full Name:", font=("Helvetica", 12)).pack(anchor="w", pady=(5, 0))
entry_name = ttk.Entry(form_frame, width=50)
entry_name.pack(pady=5)

# Email
ttk.Label(form_frame, text="Email Address:", font=("Helvetica", 12)).pack(anchor="w", pady=(10, 0))
entry_email = ttk.Entry(form_frame, width=50)
entry_email.pack(pady=5)

# Age
ttk.Label(form_frame, text="Age:", font=("Helvetica", 12)).pack(anchor="w", pady=(10, 0))
entry_age = ttk.Entry(form_frame, width=50)
entry_age.pack(pady=5)

# Gender
ttk.Label(form_frame, text="Gender:", font=("Helvetica", 12)).pack(anchor="w", pady=(10, 0))
gender_var = ttk.StringVar()
ttk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").pack(anchor="w")
ttk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").pack(anchor="w")
ttk.Radiobutton(form_frame, text="Other", variable=gender_var, value="Other").pack(anchor="w")

# Password
ttk.Label(form_frame, text="Password:", font=("Helvetica", 12)).pack(anchor="w", pady=(10, 0))
entry_password = ttk.Entry(form_frame, width=50, show="*")
entry_password.pack(pady=5)

# Buttons
ttk.Button(app, text="Submit", bootstyle=SUCCESS, command=submit_form, width=20).pack(pady=20)
ttk.Button(app, text="Toggle Fullscreen", bootstyle=INFO, command=toggle_fullscreen, width=20).pack()

# Start GUI
app.mainloop()
