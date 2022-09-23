from doctest import master
from fileinput import filename
import tkinter as tk
from tkinter import filedialog
import os
from tkinter.ttk import Labelframe
from tkinter import *
from tkinter.filedialog import askopenfilenames

root = tk.Tk()

#This is Frame with AudiRed
canvas = tk.Canvas(root, height=500, width=500, bg="#b51c14")
canvas.pack()

#this is white templet
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# folder path
dir_path = r'C:\Users\robin\Documents\Plocklistor'
# list to store files name
def lof():
    ext = ('pdf')
    for files in os.listdir(dir_path):
        if files.endswith(ext):
            for file in files:
                my_button = tk.Button(frame, text=files, padx=50, pady=5, fg="black", bg="#FFFFFF",)
            my_button.pack()


#Button UPDATE LIST
PrintPPG = tk.Button(root, text="UPDATE LIST", padx=10, pady=5,
                          fg="white", bg="#8C00E6",command=lof)
PrintPPG.pack() 

root.mainloop()