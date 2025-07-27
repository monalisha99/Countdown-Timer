

import tkinter as tk


def start_timer():
    time_str = entry_widget.get()
    try:
        # Split the time: "00:01:30".split(":") → ["00", "01", "30"]
        # map(int, ...) converts each of those to integers → [0, 1, 30]
        # These values are assigned to h, m, and s.
                                                                    #1 hour = 3600 seconds
        h, m, s = map(int, time_str.split(":"))                     #1 minute = 60 seconds
        total_seconds = h * 3600 + m * 60 + s                       #For example: 0*3600 + 1*60 + 30 = 90 seconds
                                                                    #Convert hours, minutes, seconds to total seconds

        #Start the actual countdown by calling the countdown() function and passing the total seconds.
        count_down(total_seconds)                                  
    except:                                                      
        label.config(text="Invalid format! Use HH:MM:SS")          
                                                                   
def count_down(seconds):
    if seconds >= 0:                         #This checks if the timer has not yet reached zero
                                              #As long as seconds is not negative, continue countdown.
        h, rem = divmod(seconds, 3600)        # see below (1) and (2)
        m, s = divmod(rem, 60)
        time_format = f"{h:02d}:{m:02d}:{s:02d}"    #Format the values to always show 2 digits.
        label.config(text=time_format)              #Updates the label widget to display the current countdown time.
        root.after(1000, count_down, seconds - 1)    #"Wait 1000 milliseconds (1 second), then call countdown() again with one less second."
    else:
        label.config(text="Time's up!")          #When the countdown hits below 0, stop the timer and show this message.

#(1) h, rem = divmod(seconds, 3600) ? 
# explanation:-
#divmod() returns two values:
#Quotient → h = how many full hours
#Remainder → rem = what's left after removing full hours
#Example: divmod(3670, 3600) → h=1, rem=70


#(2) m, s = divmod(rem, 60)?
# explanation:-
#Now split the remaining seconds into minutes and seconds.
#Example: divmod(70, 60) → m=1, s=10




root = tk.Tk()
root.title("Countdown Timer")
root.geometry("420x240")


label = tk.Label(root, text="00:00:00", font=("Helvetica", 14))
label.pack(pady=10)


entry_widget = tk.Entry(root, font=("Helvetica",14), justify="center")
entry_widget.pack(pady=5)
entry_widget.insert(0,"00:00:01")  # default 59 seconds

start_button = tk.Button(root, text="START", command=start_timer)
start_button.pack(pady=5)

root.mainloop()








