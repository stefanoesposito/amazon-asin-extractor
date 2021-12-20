import re
import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from typing import Sized
import pyperclip as pc
from PIL import Image, ImageTk

def asin_finder(e):
  link = entry_link.get()
  asin_s = re.search(r'\/dp\/(.*?)\/', link, flags=re.IGNORECASE) 
  asin_q = re.search(r'\/dp\/(.*?)\?', link, flags=re.IGNORECASE) 
  asin_p = re.search(r'\/gp\/product\/(.*?)\/', link, flags=re.IGNORECASE) 
  asin_p_q = re.search(r'\/gp\/product\/(.*?)\?', link, flags=re.IGNORECASE) 

  if asin_s:
    dp_slash = asin_s.group(1)
    print(dp_slash)
    asin1 = Label(root, text=f"ASIN: {dp_slash}", font="Helvetica 39 bold", foreground="#222")
    asin1.pack(side=TOP, pady=28)
    pc.copy(dp_slash)
    conferma = Label(text="ASIN copied to clipboard", font="Helvetica 25 bold italic", foreground="#222")
    conferma.pack(side=TOP, pady=15)
    
  elif asin_q:
    dp_question = asin_q.group(1)
    print(dp_question)
    asin2 = Label(root, text=f"ASIN: {dp_question}", font="Helvetica 39 bold", foreground="#222") 
    asin2.pack(side=TOP, pady=28)
    pc.copy(dp_question)
    conferma = Label(text="ASIN copied to clipboard", font="Helvetica 25 bold italic", foreground="#222")
    conferma.pack(side=TOP, pady=15)
    
  elif asin_p:
    gp_product = asin_p.group(1)
    print(gp_product)
    asin3 = Label(root, text=f"ASIN: {gp_product}", font="Helvetica 39 bold", foreground="#222")
    asin3.pack(side=TOP, pady=28)
    pc.copy(gp_product)
    conferma = Label(text="ASIN copied to clipboard", font="Helvetica 25 bold italic", foreground="#222")
    conferma.pack(side=TOP, pady=15)
    
  elif asin_p_q:
    gp_product_q = asin_p_q.group(1)
    print(gp_product_q)
    asin4 = Label(root, text=f"ASIN: {gp_product_q}", font="Helvetica 39 bold", foreground="#222")
    asin4.pack(side=TOP, pady=28)
    pc.copy(gp_product_q)
    conferma = Label(text="ASIN copied to clipboard", font="Helvetica 25 bold italic", foreground="#222")
    conferma.pack(side=TOP, pady=15)
    
  else:
    niente = Label(text="No ASIN found", font="Helvetica 33 bold", foreground="#222")  
    niente.pack(side=TOP, pady=60)
    

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


root = tk.Tk()

root.title("Amazon Asin Extractor")
root.geometry("430x480+500+150")
# root.configure(background="#fefefe")
root.bind('<Return>', asin_finder)


get_btn = PhotoImage(file="img/get_asin_img.gif")
# Label(image=get_btn).pack()

restart_btn = PhotoImage(file="img/restart_img.gif")
# Label(image=restart_btn).pack()

titolo = Label(root, text="Amazon ASIN Extractor", background="#fe9400", font="Helvetica 32 bold")
titolo.pack(side=TOP)
titolo.configure(foreground="#222")
titolo.bind('<Button>', restart_program)

istruzioni = Label(root, text="Paste your link here and click on Get ASIN", foreground="#222", font="Helvetica 16 italic bold")
istruzioni.pack(side=TOP, pady=12)
istruzioni.configure()

entry_link = Entry(root, width = 44)
entry_link.focus()
entry_link.pack()

estrai = tk.Button(root, image=get_btn, cursor="hand2", command=asin_finder, bd=0)
estrai.pack(pady=15)
estrai.bind('<ButtonPress>', asin_finder)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')


restart = tk.Button(root, image=restart_btn, cursor="hand2", command=restart_program, bd=0)
# restart.pack(fill=tk.X, side=tk.BOTTOM)
restart.pack(side=tk.BOTTOM, pady=30)

root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)
root.mainloop()