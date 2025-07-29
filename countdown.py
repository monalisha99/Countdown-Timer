
# Import the tkinter library and its font module for GUI and font control
import tkinter as tk
from tkinter import font

# Function to start the timer when the START button is clicked
def start_timer():
    time_str = entry_widget.get()  # Get the time input from the entry widget
    try:
        # Split the string (HH:MM:SS) and convert each part to integers
        h, m, s = map(int, time_str.split(":"))

        # Convert the entire time to total seconds
        total_seconds = h * 3600 + m * 60 + s

        # Start the countdown with the total seconds
        count_down(total_seconds)
    except:
        # If input format is incorrect, show error message
        label.config(text="Invalid format! Use HH:MM:SS")

# Recursive countdown function that updates the label every second
def count_down(seconds):
    if seconds >= 0:
        # Convert total seconds back to hours, minutes, and seconds
        h, rem = divmod(seconds, 3600)  # rem = remaining seconds after hours
        m, s = divmod(rem, 60)          # split remainder into minutes and seconds

        # Format the time with leading zeros (e.g., 01:05:09)
        time_format = f"{h:02d}:{m:02d}:{s:02d}"

        # Update the label with the formatted time
        label.config(text=time_format)

        # Schedule the function to run again after 1 second (1000 milliseconds)
        root.after(1000, count_down, seconds - 1)
    else:
        # When time is up, display message
        label.config(text="Time's up!")

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")         # Set window title
root.geometry("420x240")              # Set fixed window size
root.configure(bg="lightgrey")        # Set background color of window

# Create and place the label to display the countdown time
label = tk.Label(
    root,
    text="00:00:00",                  # Initial time
    font=("Arial", 14),              # Font style and size
    bg="lightgrey"                   # Match background color to window
)
label.pack(fill="both", expand=True, padx=10, pady=10)  # Add padding and make label stretch

# Create a frame to hold the Entry and Button widgets, for better centering
middle_frame = tk.Frame(root, bg="lightgrey")
middle_frame.pack(expand=True)  # Use expand to center it vertically

# Create the entry widget for the user to input countdown time
entry_widget = tk.Entry(
    middle_frame,
    font=("Helvetica", 14),         # Font for the entry text
    justify="center",               # Center the text inside the entry box
    width=15                        # Width of the entry box
)
entry_widget.pack(pady=5)          # Add vertical padding
entry_widget.insert(0, "00:00:01") # Set default time (1 second)

# Create the START button to trigger the countdown
start_button = tk.Button(
    middle_frame,
    text="START",                   # Button label
    command=start_timer             # Link the button to the start_timer function
)
start_button.pack(pady=5)          # Add vertical padding

# Start the Tkinter event loop (keeps the window open and responsive)
root.mainloop()





