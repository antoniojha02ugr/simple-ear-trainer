import tkinter as tk
import numpy as np
import pygame
import random

class SimpleEarTrainer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.root = tk.Tk()

        self.root.title("SimpleEarTrainer")

        self.keys = []

        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        column = 0

        for i in range(len(notes)):
            if self.is_black_key(i):
                button = tk.Button(self.root, bg='black', text=notes[i%len(notes)], fg="white", font=("Arial", 12), width=4)
                button.grid(row=2, column=column)
            else:
                button = tk.Button(self.root, bg='white', text=notes[i%len(notes)], fg="black", font=("Arial", 12), width=4)
                button.grid(row=3, column=column)
                column = column + 1

            note_number = i + 60
            button.bind("<Button-1>", lambda event, note=note_number: self.play_note(note))

            self.keys.append(button)

    def play_note(self, note):
        path = "./sounds/" + str(note) + ".mp3"

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        pygame.time.delay(1000)  
        pygame.mixer.music.stop()

    def is_black_key(self, idx):
        return idx % 12 in [1, 3, 6, 8, 10]

    def mainloop(self):
        self.root.mainloop()

    def __del__(self):
        pygame.quit()

def main():
    app = SimpleEarTrainer()
    app.mainloop()

if __name__ == "__main__":
    main()
