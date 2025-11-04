import tkinter as tk

# Create the main application window
root = tk.Tk() # "root" object is the foundation that holds everything e.g. buttons, labels, etc. Tk() creates the main application window
root.title("Flashcard Quiz")
root.geometry("400x300") # Defines the windows initial width and height in pixels
root.config(bg="#F7F9FB")

# Create a heading label widget- text displayed in the window 
title_label = tk.Label(
    root,
    text="🧠 Flashcard Quiz",
    font=("Arial", 20, "bold"), # Sets font type, size, and weight
    fg="#333333", # text colour
    bg="#F7F9FB" # background colour
)
title_label.pack(pady=30) # adds the label to window- adds 30px of space above and below the label for breathing room

#Keeps the window open and responsive
root.mainloop() # starts Tkinter's event loop - keeps the window open and listening for user actions