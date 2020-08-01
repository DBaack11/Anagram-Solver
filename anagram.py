import tkinter as tk
from tkinter import messagebox

# Function that clears the entry box, anagrams text box, and results label.
def clear_click():
    anagrams.delete('1.0', tk.END)
    word.delete(0, tk.END)
    results.config(text="Results In:")

# Code for the design of the GUI below
root.title("Anagram Solver")
root.geometry('600x250')

# GUI Frames
left_frame = tk.Frame(master=root, bg="gray")
left_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
divider = tk.Frame(master=root, width=5)
divider.pack(fill=tk.Y, side=tk.LEFT)
right_frame = tk.Frame(master=root, bg="gray")
right_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# GUI Labels
left_frame_label = tk.Label(left_frame, text="Enter a Word", fg="white", bg="gray", font=("Ubuntu", 40, "bold"))
left_frame_label.pack(side=tk.TOP)
right_frame_label = tk.Label(right_frame, text="Anagrams", fg="white", bg="gray", font=("Ubuntu", 20, "bold"))
right_frame_label.pack(side=tk.TOP)
results = tk.Label(right_frame, text="Results In: ", fg="white", bg="gray", font=("Ubuntu", 15, "bold"))
results.pack(side=tk.BOTTOM)

# Entry and Text boxes
word = tk.Entry(left_frame, textvariable=entry, fg="white", bg="gray", font=("Ubuntu", 15, "bold"), justify="center")
word.pack(pady=10)
anagrams = tk.Text(right_frame, fg="white", bg="gray", font=("Ubuntu", 30, "bold"))
anagrams.tag_configure("center", justify="center")
anagrams.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

# Buttons
clear = tk.Button(left_frame, text="CLEAR", font=("Ubuntu", 30, "bold"), fg="white",
                  highlightbackground="dark gray", highlightthickness=4, command=clear_click)
clear.pack(side=tk.BOTTOM, expand=True)
solve = tk.Button(left_frame, text="SOLVE", font=("Ubuntu", 30, "bold"), fg="white",
                  highlightbackground="dark gray", highlightthickness=4, command=solve_click)
solve.pack(side=tk.BOTTOM, expand=True)

tk.mainloop()
