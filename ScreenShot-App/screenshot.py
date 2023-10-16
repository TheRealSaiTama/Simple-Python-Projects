import time
import pyautogui
import tkinter as tk
from tkinter import ttk

def screenshot():
    name = int(round(time.time() * 1000))
    name = '/home/keshav/python-projects/ScreenShot-App/screenshots_data/{}.png'.format(name)
    # time.sleep(3) # this is not needed, as the user can click the button when ready
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
root.title("Screenshot App") # give a title to the window
root.geometry("300x100") # set the size of the window
root.resizable(False, False) # prevent the window from being resized

frame = tk.Frame(root)
frame.pack(padx=10, pady=10) # add some padding around the frame

button = ttk.Button( # use ttk.Button for a nicer look
    frame,
    text="Take Screenshot",
    command=screenshot
)

button.pack(side=tk.LEFT, padx=10, pady=10) # add some padding around the button

close = ttk.Button( # use ttk.Button for a nicer look
    frame,
    text="QUIT",
    command=root.destroy # use root.destroy instead of quit to close the window properly
)

close.pack(side=tk.LEFT, padx=10, pady=10) # add some padding around the button

root.mainloop()
