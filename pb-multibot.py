import tkinter as tk
import webbrowser
import time
from tkinter import*

root= tk.Tk()
root.title('Multitab Browser Replier')
root.resizable(False, False)

#If any browser is not working, edit the path here.
Chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
Firefox = "C://Program Files//Mozilla Firefox//firefox.exe %s"
Brave = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
Edge = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'

Browsers = [
    Firefox,
    Chrome,
    Brave,
    Edge
] 

variable = tk.StringVar(root)
variable.set(Browsers[1])
opt = tk.OptionMenu(root, variable, *Browsers)
opt.config(width=30, font=('Helvetica', 10))
opt.pack()

# --------------------
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

entry2 = tk.Entry (root) 
import tkinter as tk
import webbrowser
import time
from tkinter import*

root= tk.Tk()
root.title('Multitab Browser Replier')
root.resizable(False, False)

#If any browser is not working, edit the path here.
Chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
Firefox = "C://Program Files//Mozilla Firefox//firefox.exe %s"
Brave = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
Edge = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'

Browsers = [
    Firefox,
    Chrome,
    Brave,
    Edge
] 

variable = tk.StringVar(root)
variable.set(Browsers[1])
opt = tk.OptionMenu(root, variable, *Browsers)
opt.config(width=30, font=('Helvetica', 10))
opt.pack()

# --------------------
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 180, window=entry2)

entry3 = tk.Entry (root) 
canvas1.create_window(200, 220, window=entry3)


# titulos
sel_nav = tk.Label(root, text = "Select Browser")
canvas1.create_window(200, 20, window=sel_nav)

url_text = tk.Label(root, text = "Url")
canvas1.create_window(100, 140, window=url_text)

tabs_text = tk.Label(root, text = "Tabs")
canvas1.create_window(100, 180, window=tabs_text)

sleep_text = tk.Label(root, text = "Sleep")
canvas1.create_window(100, 220, window=sleep_text)

#--------------
def callback(url_profile):
    webbrowser.open_new(url_profile)

link1 = Label(root, text="hephitao ✅", fg="green", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://github.com/hephitao"))


def accion ():
    link = entry1.get()
    count = entry2.get()
    seconds = entry3.get()

    for x in range(int(count)):
        
        webbrowser.get(str(variable.get())).open(str(link))
        time.sleep(float(seconds))

start_button = tk.Button(text='Lanzar bot', command=accion)
canvas1.create_window(200, 260, window=start_button)

#stop process button (in process xd)
#button2 = tk.Button(text='detener', command=root.quit())
#canvas1.create_window(200, 280, window=button2)

root.mainloop()
