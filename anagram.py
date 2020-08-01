"""
Author: Devin Baack
Program: anagram.py
Date Modified: 08/01/2020

This program utilizes multiple components of the Python programming language and topics covered
in CIS 179 to create a GUI that accepts a single word string input and, after a button click,
lists all of the same-length anagrams of the word, provided by parsing through an
official dictionary file.
"""

# ############## Try These Examples ############## #
# *     coder         edit          sonic        * #
# *     post          name          boredom      * #
# *     resort        last          letters      * #
# *     leap          protein       printer      * #
# *     earth         dancer        pear         * #
# *     spider        medical       oracle       * #
# ################################################ #

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
entry = tk.StringVar()


# Custom exception utilized for verifying valid input
class InvalidInputException(Exception):
    pass


# Function that, when called through button click, retrieves string from entry box, checks if
# it is a valid input, and displays all anagrams on the text box.
# Utilizing datetime calculations, this function times the anagram algorithm and displays the result.
def solve_click():
    start = datetime.now()
    entry_word = entry.get().lower()
    dictionary = open("english3.txt").read().splitlines()

    try:
        if not entry_word.isalpha():
            raise InvalidInputException
    except InvalidInputException:
        messagebox.showinfo("Invalid Input", "Please enter a single alphabetic word. \n"
                                             "                      (No Spaces)")
        word.delete(0, tk.END)

    for line in dictionary:
        if sorted(line) == sorted(entry_word):
            anagrams.insert(tk.END, line + '\n')
            anagrams.tag_add("center", "1.0", "end")

    end = datetime.now()
    calculation = round(float((str(end - start)).replace("0:00:0", '')), 3)

    if len(entry_word) != 0:
        results.config(text=f"Results In: {calculation} seconds")


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
