import tkinter as Tk
import customtkinter
from pytube import YouTube
from tkinter import messagebox

flash_delay = 500
flash_colours = ('black','white')

def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    app.after(flash_delay, flashColour, object, 1 - colour_index)




def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure
        video.download()
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Download Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

# progress bar update
    progressBar.set(float(percentage_of_completion)/100)

# system Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


my_label = customtkinter.CTkLabel(app, text="Downloading >>")

# adding UI element
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack(padx=15, pady=15)

# link input
url_var = Tk.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
link.pack()

# Finish Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
