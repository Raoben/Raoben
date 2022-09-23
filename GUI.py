
from doctest import master
from fileinput import filename
import tkinter as tk
from tkinter import filedialog
import os
from tkinter.ttk import Labelframe
from tkinter import *
from tkinter.filedialog import askopenfilenames

root = tk.Tk()
from os import walk
#This is Frame with AudiRed
canvas = tk.Canvas(root, height=600, width=600, bg="#b51c14")
canvas.pack()

#this is white templet
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
 

#Button UPDATE LIST
PrintPPG = tk.Button(root, text="UPDATE LIST", padx=10, pady=5,
                          fg="white", bg="#8C00E6",)
PrintPPG.pack() 

#Youtube Filedialog code
master = ()
root.filename = filedialog.askopenfilenames(initialdir="/Plocklistor", title="Select A File", filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
my_label = Label(frame, text=root.filename).pack()

root.mainloop() 
