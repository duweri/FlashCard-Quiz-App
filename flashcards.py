import tkinter as tk

flashcards = [
    {"question❔": "What is the capital of France?", "answer": "Paris"},
    {"question❔": "What is 5 + 7?", "answer": "12"},
    {"question❔": "What programming language are we using?", "answer": "Python"},
    {"question❔": "What is the fastset land animal?", "answer": "Cheetah"},
    {"question❔": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question❔": "What does GUI stand for?", "answer": "Graphical User Interface"}
]
# Track the current card
current_index = 0 
#Text output
print(flashcards[0]["question❔"])

# --- Functions ---
def show_answer():
    """Display the answer for the current flashcard."""
    current_card = flashcards[current_index]
    answer_label.config(text=current_card["answer"])  # .config tells Tkinter to update the label on screen

# --- GUI Window ---
# Create the main application window - GUI window
root = tk.Tk() # "root" object is the foundation that holds everything e.g. buttons, labels, etc. Tk() creates the main application window
root.title("Flashcard Quiz")
root.geometry("400x300") # Defines the windows initial width and height in pixels
root.config(bg="#ECFF7E")

# Title 
# Create a heading label widget- text displayed in the window 
title_label = tk.Label(
    root,
    text="🧠 Flashcard Quiz",
    font=("Arial", 20, "bold"), # Sets font type, size, and weight
    fg="#333333", # text colour
    bg="#ECFF7E" # background colour
)
title_label.pack(pady=30) # adds the label to window- adds 30px of space above and below the label for breathing room

# Label for the question
question_label = tk.Label(
    root,
    text= flashcards[current_index]["question❔"],
    font=("Arial", 20, "bold"), # Sets font type, size, and weight
    fg="#333333", # text colour
    bg="#ECFF7E", # background colour
    wraplength= 350 # allows the text to wrap nicely
)
question_label.pack(pady=20)

# Answer label starts blank
answer_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"), # Sets font type, size, and weight
    fg="#555555", # text colour
    bg="#ECFF7E" # background colour
)
answer_label.pack(pady=10)

# Show answer button
show_button = tk.Button(
    root,
    text="Show Answer",
    command=show_answer, #this part of code is the part that listens for the click. Tkinter internally does something like this: Okay, when this button is clicked, I’ll call the function show_answe
    font=("Arial", 12, "bold"),
    bg="#E27AC3",
    fg="#333333",
    padx=10,
    pady=5
)
show_button.pack(pady=20)

# Keeps window running
root.mainloop()


# 💡