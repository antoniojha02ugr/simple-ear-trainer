import tkinter as tk
import numpy as np
import pygame
import random

class SimpleEarTrainer:
    def __init__(self):
        # Initialize pygame and its mixer module
        pygame.init()
        pygame.mixer.init()

        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("SimpleEarTrainer")

        # Create an empty label to create a gap in the layout
        empty_row1 = tk.Label(self.root, height=1)
        empty_row1.grid(row=1)

        # Create a StringVar to manage the text entry content
        self.text_var = tk.StringVar()
        self.text_var.set("")

        # Create the text entry widget for showing notes and answers
        self.text_entry = tk.Entry(self.root, textvariable=self.text_var, state='readonly', font=("Arial", 20), width=4, justify="center")
        self.text_entry.grid(row=0, column=3)

        # Initialize an empty list for storing the piano keys/buttons
        self.keys = []

        # List of musical notes
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        # Variable for the played note, set to -1 when no note has been played
        self.p_note = -1

        column = 0

        # Create the piano keys/buttons and bind events to them
        for i in range(len(self.notes)):
            # Buttons have different positioning depending on its color
            if self.is_black_key(i):
                button = tk.Button(self.root, bg='black', text=self.notes[i%len(self.notes)], fg="white", font=("Arial", 12), width=4)
                button.grid(row=4, column=column)
            else:
                button = tk.Button(self.root, bg='white', text=self.notes[i%len(self.notes)], fg="black", font=("Arial", 12), width=4)
                button.grid(row=5, column=column)

                # When a white key is displayed, the next one is placed in the next column
                column = column + 1

            # Midi encoding of the notes in the fourth scale 
            note_number = i + 60

            button.bind("<Button-1>", lambda event, note=note_number: self.answer_note(note))

            self.keys.append(button)

        # Create another empty label for layout spacing
        empty_row2 = tk.Label(self.root, height=1)
        empty_row2.grid(row=3)

        # Create the 'Play' button and bind its event
        self.play_button = tk.Button(self.root, bg='white', text="Play", fg="black", font=("Arial", 20), width=12)
        self.play_button.grid(row=2, column=2, columnspan=3)
        self.play_button.bind("<Button-1>", lambda event: self.ask_note())

    def ask_note(self):
        # Generate a random note to ask the user about
        self.p_note = random.randint(60, 71)

        # Set the color of the question mark to black
        self.text_entry.configure(fg="black")

        # Play the randomly selected note's sound
        self.play_note(self.p_note)

        # Set the color of the text to black and display question mark
        self.text_entry.configure(fg="black")
        self.text_var.set("?")

    def answer_note(self, note):
        # Play the player's selected note's sound
        self.play_note(note)

        # Check if there's a previously asked note
        if self.p_note != -1:
            # Set the text in the text entry to display the correct note name
            self.text_var.set(str(self.notes[self.p_note%12]))

            # If the answer is correct, set the correct note name to green, otherwise to red
            if self.p_note == note:
                self.text_entry.configure(fg="green")
            else:
                self.text_entry.configure(fg="red")

        # Reset the played note variable to indicate no active question
        self.p_note = -1

    def play_note(self, note):
        # Construct the path to the sound file based on the midi note number
        path = "./sounds/" + str(note) + ".mp3"

        # Load and play the note's sound using pygame.mixer
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        # Add a one second delay to give time for the sound to play
        pygame.time.delay(1000)  

        # Stop the playback to avoid overlapping sounds
        pygame.mixer.music.stop()

    def is_black_key(self, idx):
        # Determine if a key is black based on its index in the note list
        return idx % 12 in [1, 3, 6, 8, 10]

    def mainloop(self):
        # Start the main Tkinter event loop
        self.root.mainloop()

    def __del__(self):
        # Clean up pygame resources when the object is deleted
        pygame.quit()

def main():
    # Create and run the SimpleEarTrainer application
    app = SimpleEarTrainer()
    app.mainloop()

if __name__ == "__main__":
    # Entry point of the script
    main()
