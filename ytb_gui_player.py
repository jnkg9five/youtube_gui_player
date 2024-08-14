# ytb_gui_player.py

import tkinter as tk
from tkinter import messagebox
import yt_dlp
import pafy
import vlc
import re
import os

class YouTube_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Youtube Video Player")
        self.root.geometry("800x600")

        # URL Input
        self.url_label = tk.Label(root, text="Enter Valid YouTube URL: ")
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        # VLC Player Instance
        self.inst = vlc.Instance()
        self.player = self.inst.media_player_new()

        # Video Frame 
        self.video_frame = tk.Frame(root, bg="black")
        self.video_frame.pack(fill=tk.BOTH, expand=1)

        # Video Controls (Play, Pause, Resume, Stop)
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        # Play Button
        self.play_btn = tk.Button(root, text="Play", command=self.play_ytb_vid)
        self.play_btn.pack(pady=20)

        # Pause Button
        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        # Resume Button
        self.resume_button = tk.Button(self.control_frame, text="Resume", command=self.resume_video)
        self.resume_button.pack(side=tk.LEFT, padx=5)

        # Stop Button
        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_video)
        self.stop_button.pack(side=tk.LEFT, padx=5)


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
                self.player.set_xwindow(self.video_frame.winfo_id())
                self.player.play()
            else:
                messagebox.showerror("Error", "Failed to download YouTube Video.")
        else:        
            messagebox.showerror("URL is invalid", "Enter a valid YouTube URL.")

    def pause_video(self):
        if self.player.is_playing():
            self.player.pause()

    def resume_video(self):
        if not self.player.is_playing():
            self.player.play()

    def stop_video(self):
        self.player.stop()  

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTube_GUI(root)
    root.mainloop()
    os.remove('video.mp4')