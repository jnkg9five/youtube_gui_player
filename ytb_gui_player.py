# ytb_gui_player.py

import tkinter as tk
from tkinter import messagebox
import yt_dlp
import pafy
import vlc
import re

class YouTube_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Youtube Video Player")
        self.root.geometry("1280x720")

        self.url_label = tk.Label(root, text="Enter Valid YouTube URL: ")
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        self.play_btn = tk.Button(root, text="Play", command=self.play_ytb_vid)
        self.play_btn.pack(pady=20)

        self.inst = vlc.Instance()
        self.player = self.inst.media_player_new()

        self.canvas = tk.Canvas(root, width=1280, height=570)
        self.canvas.pack()

        self.video_panel = self.canvas.create_rectangle(0, 0, 1280, 570, fill="black")

    def download_vid(self, url):
        ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4',}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            return 'video.mp4'

    def is_valid_ytb_url(self, url):
    #User regex to check if input url is a valid YouTube link
        regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+')
        return regex.match(url)

    def play_ytb_vid(self):
    #Pass URL entry to the GUI interface
        url = self.url_entry.get()
        if self.is_valid_ytb_url(url):
            vid_path = self.download_vid(url)
            if vid_path:
                #play video in gui area
                self.media = self.inst.media_new(vid_path)
                self.player.set_media(self.media)
                self.player.set_xwindow(self.canvas.winfo_id())
                self.player.play()
            else:
                messagebox.showerror("Error", "Failed to download YouTube Video.")
        else:        
            messagebox.showerror("URL is invalid", "Enter a valid YouTube URL.")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTube_GUI(root)
    root.mainloop()