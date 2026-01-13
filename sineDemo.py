# Help text
print("If not booting, try this:")
print("pip install pysinewave")

# Info text
print("Sine wave demo for school, licensed under GPL 2.")
print("Programmed entirely by Vámosi Bálint")
print("No generative A.I was used.")

# Imports
import tkinter as tk
import pysinewave as ps
import time

# Definitons
def playSine(): # Defines the function which plays the sine wave
    sine = ps.SineWave(pitch=pitchScale.get()) # Defines the sine function which plays at the pitch of the slider's value.
    sine.play() # Play sine
    time.sleep(1) # Waits one second
    sine.stop() # Turns off sine


# Main loop
mainWindow = tk.Tk() # Defining main window with Tk() function
mainWindow.geometry("300x300") # Defines size of window

pitchScale = tk.Scale(mainWindow, from_=1, to=80) # Defines scale used for pitching up and down sine
pitchScale.place(x=110,y=50) # Places (NOT PACKS!) scale

playButton = tk.Button(mainWindow, text="Play sine", command=playSine) # Defines the play button
playButton.place(x=100, y=200) # Places the play button

topLabel = tk.Label(mainWindow, text="Sine wave demo for school") # Defines label at the top of the screen
topLabel.pack() # "Packs" the label (gets it ready for rendering)

mainWindow.mainloop() # Renders window

