import tkinter as tk
from datetime import datetime

# Create main window
root = tk.Tk()
root.title("Simple Keylogger - Educational Project")
root.geometry("600x400")

logging = False
log_file = "keylog.txt"


# Function to start logging
def start_logging():
    global logging
    logging = True
    status_label.config(text="Status: Logging Started")


# Function to stop logging
def stop_logging():
    global logging
    logging = False
    status_label.config(text="Status: Logging Stopped")


# Function to record key presses
def key_pressed(event):
    if not logging:
        return

    key = event.keysym

    # Convert special keys into readable names
    if key == "space":
        key = "[SPACE]"
    elif key == "Return":
        key = "[ENTER]"
    elif key == "BackSpace":
        key = "[BACKSPACE]"
    elif key == "Tab":
        key = "[TAB]"

    # Get current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Display key in the application
    output.insert(tk.END, key + " ")
    output.see(tk.END)

    # Save key to file
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"{current_time} : {key}\n")


# Heading
title_label = tk.Label(
    root,
    text="Simple Keylogger",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)


# Information
info_label = tk.Label(
    root,
    text="Educational demonstration - logs keys only in this window"
)
info_label.pack()


# Start button
start_button = tk.Button(
    root,
    text="Start Logging",
    command=start_logging,
    width=15
)
start_button.pack(pady=10)


# Stop button
stop_button = tk.Button(
    root,
    text="Stop Logging",
    command=stop_logging,
    width=15
)
stop_button.pack(pady=5)


# Status
status_label = tk.Label(
    root,
    text="Status: Logging Stopped",
    font=("Arial", 12)
)
status_label.pack(pady=10)


# Text box
output = tk.Text(
    root,
    height=10,
    width=60
)
output.pack(pady=10)


# Detect key presses inside this application
root.bind("<KeyPress>", key_pressed)

# Start GUI
root.mainloop()