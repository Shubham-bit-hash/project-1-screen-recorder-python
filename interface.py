#Run main.py!!!

import tkinter
from tkinter import *

def on_closing():
    global running
    running = False

# GUI
root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(False, False)
root.title("Screen Recorder")
root.geometry("800x400+500+100")
canvas = Canvas(root, bg="#4392F1", height=400, width=800, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
background_img = PhotoImage(file=f"imp_images/final1.png")
background = canvas.create_image(400.0, 200.0, image=background_img)
header = canvas.create_text(400.0, 91.0, text="Capture Your screen", fill="#ECE8EF", font=("Roboto-Bold", int(30.0)))
create_label = canvas.create_text(203.5, 174.5, text="create an", fill="#EDFF00", font=("Roboto-Bold", int(16.0)))
video_label = canvas.create_text(590.5, 174.5, text="  (15 recom.)fps video", fill="#030303", font=("Roboto-Medium", int(16.0)))
switch = tkinter.Scale(from_=1, to=100, orient=tkinter.HORIZONTAL, length=200, activebackground="#000000"
                       , bg="#FFC0CB", highlightcolor="#C25993", highlightbackground="#C25993", fg="black",
                       troughcolor="white")

menubar = Menu(root)
video = Menu(menubar, tearoff=0)
about = Menu(menubar, tearoff=0)
video_format = Menu(menubar, tearoff=0)#C25993


mp4_format = tkinter.BooleanVar()
mp4_format.set(True)
avi_format = tkinter.BooleanVar()

video.add_cascade(label='Video Format', menu=video_format)

menubar.add_cascade(label='File', menu=video)
menubar.add_cascade(label="About", menu=about)

start_img = PhotoImage(file=f"imp_images/start.png")
start = Button(image=start_img, borderwidth=0, highlightthickness=0, relief="sunken")
pause_img = PhotoImage(file=f"imp_images/pause.png")
pause = Button(image=pause_img, borderwidth=0, highlightthickness=0, relief="sunken")
end_img = PhotoImage(file=f"imp_images/end.png")
end = Button(image=end_img, borderwidth=0, highlightthickness=0, relief="sunken")
info = canvas.create_text(400.0, 342.5, text="Start Recording", fill="#0f0f0f", font=("Roboto-Medium", int(16.0)))

# When started
#start["state"] = "normal"
end["state"] = "normal"
pause["state"] = "normal"
