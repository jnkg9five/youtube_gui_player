# YouTube Video Player GUI Program

## Description 
This is a Python program written to create a GUI interface using Tkinter Lib to enter a valid YouTube video URL, download the video to .mp4 format and play the video in the GUI. 

## Features
- YouTube URL Support
- GUI Interface with Playback Buttons (Play, Pause, Resume, Stop)
- Added volume slider functionality into GUI Interface (Default volume 50%)
- Video plays in the embedded video frame area under URL input.

## Prerequisites
- Python 3.x
- yt-dlp (youtube downloader)
- python-vlc (video player interface program)
- tkinter (from python standard library)

## Installation
1. Clone the repository or download ytb_gui_player.py program
2. Install the necessary dependencies
   1. yt-dlp
   ````bash
   pip install ytb-dl
   ````
   2. python-vlc
   ````bash
   pip install python-vlc
   ````
3. Run the program
   ````bash
   python ytb_gui_player.py
   ````