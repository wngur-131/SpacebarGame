from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
  
print("width x height = {0} x {1} (pixels)".format(monitor_width, monitor_height))
mainloop()