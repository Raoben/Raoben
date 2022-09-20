
from fileinput import filename
import tkinter as tk
from tkinter import filedialog, Text
import os
from turtle import bgcolor
from tkinter import *
import webbrowser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import argparse
import fnmatch


root = tk.Tk() 

def Uploadaction(event=None): 
    filename = filedialog.askopenfilename(initialdir="/", title="Select File")

def open_book():
    books = []
    for file in os.listdir("Plocklistor"):
        if fnmatch.fnmatch(file, '*.PDF'):
            books.append(file)
    return books


#This is Frame with AudiRed
canvas = tk.Canvas(root, height=600, width=600, bg="#b51c14")
canvas.pack()

#this is white templet
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Buttom Openfile
Openfile = tk.Button(root, text="open file", padx=10, pady=5,
                     fg="white", bg="#8C00E6", command=open_book)
Openfile.pack() 

#Button Print PPG
PrintPPG = tk.Button(root, text="Pint PPG", padx=10, pady=5,
                          fg="white", bg="#8C00E6",command=Uploadaction)
PrintPPG.pack() 

def Openweb():
    webbrowser.open(Url)

Url = "https://random-ize.com/bad-jokes/"

#Button Jokes
JokeButton = tk.Button(root, text="Jokes Button", padx=10, pady=3, fg="white", bg="#8C00E6", command=Openweb)
JokeButton.pack()

root.mainloop() 
