import tkinter as tk
import numpy as np

class SimpleEarTrainer:
    def __init__(self):
        self.root = tk.Tk()
        self.keys = []

        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        nkeys = 12

        column = 0

        for i in range(nkeys):
            if self.is_black_key(i):
                button = tk.Button(self.root, bg='black', text=notes[i%len(notes)], fg="white", font=("Arial", 12), width=4)
                button.grid(row=0, column=column)
            else:
                button = tk.Button(self.root, bg='white', text=notes[i%len(notes)], fg="black", font=("Arial", 12), width=4)
                button.grid(row=1, column=column)
                column = column + 1

            self.keys.append(button)


    def is_black_key(self, idx):
        return idx % 12 in [1, 3, 6, 8, 10]

    def mainloop(self):
        self.root.mainloop()

def main():
    app = SimpleEarTrainer()
    app.mainloop()

if __name__ == "__main__":
    main()