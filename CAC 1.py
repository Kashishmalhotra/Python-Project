import os
from tkinter import Tk, Label, Button, filedialog
import pygame

class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Music Player")

        self.current_dir = os.getcwd()
        self.music_file = ""
        self.playing = False

        self.create_widgets()

    def create_widgets(self):
        label = Label(self.window, text="Music Player")
        label.pack(pady=10)

        browse_button = Button(self.window, text="Browse", command=self.browse_file)
        browse_button.pack(pady=5)

        play_button = Button(self.window, text="Play", command=self.play_music)
        play_button.pack(pady=5)

        pause_button = Button(self.window, text="Pause", command=self.pause_music)
        pause_button.pack(pady=5)

        stop_button = Button(self.window, text="Stop", command=self.stop_music)
        stop_button.pack(pady=5)

    def browse_file(self):
        self.music_file = filedialog.askopenfilename(initialdir=self.current_dir, title="Select Music File",
                                                     filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*")))
        if self.music_file:
            self.current_dir = os.path.dirname(self.music_file)

    def play_music(self):
        if self.music_file and not self.playing:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            self.playing = True

    def pause_music(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

if __name__ == "__main__":
    pygame.init()
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
