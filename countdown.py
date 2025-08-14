
# Import the tkinter library and its font module for GUI and font control
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import subprocess

# Function to start the timer when the START button is clicked
def startTimer():
    timeStr = entryWidget.get()  # Get the time input from the entry widget
    if timeStr == "00:00:00":
        messagebox.showinfo("Enter Your Time!")
    try:
        if timeStr!="00:00:00":
            # Split the string (HH:MM:SS) and convert each part to integers
            h, m, s = map(int, timeStr.split(":"))

            # Convert the entire time to total seconds
            totalSeconds = h * 3600 + m * 60 + s

            # Start the countdown with the total seconds
            countDown(totalSeconds)
    except:
        # If input format is incorrect, show error message
        label.config(text="Invalid Format! Use HH:MM:SS")


# Recursive countdown function that updates the label every second
def countDown(seconds):
    if seconds >= 0:
        # Convert total seconds back to hours, minutes, and seconds
        h, rem = divmod(seconds, 3600)  # rem = remaining seconds after hours
        m, s = divmod(rem, 60)          # split remainder into minutes and seconds

        # Format the time with leading zeros (e.g., 01:05:09)
        timeFormat = "{:02d}:{:02d}:{:02d}".format(h, m, s)

        # Update the label with the formatted time
        label.config(text=timeFormat)

        # Schedule the function to run again after 1 second (1000 milliseconds)
        root.after(1000, countDown, seconds - 1)
    else:
        # When time is up, display message
        label.config(text="Time's up!", fg="red")
        subprocess.run(["mpg123", "alarm_clock.mp3"])

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")         # Set window title
root.geometry("520x340")              # Set fixed window size
root.configure(bg="white")        # Set background color of window

# Create and place the label to display the countdown time
label = tk.Label(
    root,
    text="00:00:00",                  # Initial time
    font=("Arial", 20),              # Font style and size
    bg="white"                   # Match background color to window
)
label.pack(fill="both", expand=True, padx=5, pady=5)  # Add padding and make label stretch

# Create a frame to hold the Entry and Button widgets, for better centering
middleFrame = tk.Frame(root, bg="white")
middleFrame.pack(expand=True)  # Use expand to center it vertically

# Create the entry widget for the user to input countdown time
entryWidget = tk.Entry(
    middleFrame,
    font=("Helvetica", 20),         # Font for the entry text
    justify="center",               # Center the text inside the entry box
    width=35                     # Width of the entry box
)
entryWidget.pack(pady=5, ipady=20)          # Add vertical padding
entryWidget.insert(0, "00:00:00") # Set default time (1 second)

# Create the START button to trigger the countdown
startButton = tk.Button(
    middleFrame,
    text="START",
    bg="lightblue",
    fg="black",
    activebackground="darkblue",
    activeforeground="red",                   # Button label
    command=startTimer             # Link the button to the startTimer function
)
startButton.pack(pady=5, ipady=15)          # Add vertical padding

# Start the Tkinter event loop (keeps the window open and responsive)
root.mainloop()





