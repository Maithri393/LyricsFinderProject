import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests
from tkinter import messagebox

# Function to fetch lyrics
def get_lyrics():
    artist = entry_artist.get().strip()
    song = entry_song.get().strip()

    if not artist or not song:
        messagebox.showwarning("Input Error", "Please enter both artist and song title.")
        return

    status_var.set("Searching for lyrics...")
    app.update_idletasks()

    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lyrics = data.get("lyrics", "Lyrics not found.")
        status_var.set("Lyrics found ✅")
    else:
        lyrics = "Lyrics not found or an error occurred."
        status_var.set("Lyrics not found ❌")

    text_area.config(state="normal")
    text_area.delete("1.0", "end")
    text_area.insert("end", lyrics)
    text_area.config(state="disabled")

# Clear input/output fields
def clear_fields():
    entry_artist.delete(0, "end")
    entry_song.delete(0, "end")
    text_area.config(state="normal")
    text_area.delete("1.0", "end")
    text_area.config(state="disabled")
    status_var.set("Cleared 🔄")

# Toggle fullscreen mode
def toggle_fullscreen():
    current = app.attributes("-fullscreen")
    app.attributes("-fullscreen", not current)

# Setup app window
app = ttk.Window(themename="cosmo")
app.title("🎵 Lyrics Finder - Fullscreen Edition")
app.attributes("-fullscreen", True)  # or use app.state('zoomed') if you don't want true fullscreen

# App header
ttk.Label(app, text="Lyrics Finder 🎶", font=("Helvetica", 26, "bold")).pack(pady=15)

# Artist input
ttk.Label(app, text="Artist Name:", font=("Helvetica", 13)).pack(anchor="w", padx=50)
entry_artist = ttk.Entry(app, width=50, font=("Helvetica", 12))
entry_artist.pack(padx=50, pady=5)

# Song input
ttk.Label(app, text="Song Title:", font=("Helvetica", 13)).pack(anchor="w", padx=50, pady=(10, 0))
entry_song = ttk.Entry(app, width=50, font=("Helvetica", 12))
entry_song.pack(padx=50, pady=5)

# Buttons
button_frame = ttk.Frame(app)
button_frame.pack(pady=20)

ttk.Button(button_frame, text="Get Lyrics", bootstyle=SUCCESS, command=get_lyrics).grid(row=0, column=0, padx=15)
ttk.Button(button_frame, text="Clear", bootstyle=DANGER, command=clear_fields).grid(row=0, column=1, padx=15)
ttk.Button(button_frame, text="Toggle Fullscreen", bootstyle=INFO, command=toggle_fullscreen).grid(row=0, column=2, padx=15)

# Scrollable text area
text_area = ttk.ScrolledText(app, wrap="word", width=100, height=25, font=("Consolas", 12))
text_area.pack(padx=50, pady=10)
text_area.config(state="disabled")

# Status bar
status_var = ttk.StringVar(value="Enter artist and song to find lyrics.")
status_bar = ttk.Label(app, textvariable=status_var, anchor="w", bootstyle="secondary", font=("Helvetica", 10))
status_bar.pack(fill="x", padx=0, pady=(0, 5))

# Start app
app.mainloop()
