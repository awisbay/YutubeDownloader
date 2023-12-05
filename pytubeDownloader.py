import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        c
    except:
        print("YouTube Link is invalid")


# system Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# adding UI element
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack(padx=15, pady=15)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
link.pack()

# Finish Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack

# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
