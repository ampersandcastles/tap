import tkinter as tk
import time

# Create a small widget that calculates BPM based on mouse clicks or space bar taps
# The widget should have a label that displays the current BPM
# The widget should have a button that starts and stops the BPM calculation

click_times = [] # to store click times
bpm = 0 # to store bpm
running = False # to store if the widget is running

# Function to calculate the BPM
def calculate_bpm():
    global click_times, bpm, running
    if len(click_times) >= 2:
        #calculate difference between first and last click
        time_diff = click_times[-1] - click_times[-2]
        #calculate bpm based on time difference
        bpm = int(60 / time_diff)
        bpm_label.config(text=f"BPM: + {bpm}")
    else:
        bpm_label.config(text="BPM: N/A")

# Function to handle mouse clicks or space bar taps
def handle_click(event):
    global click_times, running
    if running:
        click_times.append(time.time())
        calculate_bpm()

def start_stops():
    global running, click_times, bpm
    if running:
        running = False
        click_times = []
        bpm = 0
        bpm_label.config(text="BPM: N/A")
        start_stop_button.config(text="Start")
    else:
        running = True
        start_stop_button.config(text="Stop")
    
root = tk.Tk()
root.title("BPM Calculator")
root.geometry("300x200")

# Create and place bpm label

bpm_label = tk.Label(root, text="BPM: N/A", font=("Helvetica", 24))
bpm_label.pack(pady=20)

# Create and place start/stop button
start_stop_button = tk.Button(root, text="Start", font=("Helvetica", 18), command=start_stops)
start_stop_button.pack(pady=20)

root.bind("<Button-1>", handle_click)
root.bind("<space>", handle_click)

root.mainloop()