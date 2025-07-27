

import tkinter as tk

def start_timer():
    try:
        total_seconds = int(entry.get())
        countdown(total_seconds)
    except ValueError:
        label.config(text="Please enter seconds as a number!")

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        label.config(text=time_format)
        root.after(1000, countdown, seconds - 1)
    else:
        label.config(text="Time's up!")

# Create GUI window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x150")

# Label to display time
label = tk.Label(root, text="00:00", font=("Helvetica", 48))
label.pack(pady=10)

# Entry to enter time in seconds
entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=5)
entry.insert(0, "60")  # Default 60 seconds

# Button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

root.mainloop()








