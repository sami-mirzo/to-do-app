import tkinter as tk
from tkinter import *
from tktooltip import ToolTip

root = tk.Tk()
root.geometry("500x450")
root.config(bg='grey')

def aufgabe_add():
    aufgabe = entry1.get()
    if aufgabe == "":
        print("Aufgabe eintragen")
    else:
        listbox.insert(0, aufgabe)
        entry1.delete(0, tk.END)

def aufgabe_delete():
    listbox.delete(tk.ANCHOR)

def eingabe_entfernen(event, eingabe):
    eingabe.delete(0, tk.END)

        
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=20)

listbox = tk.Listbox(listbox_frame)
listbox.pack(side=tk.LEFT)

scroll_bar = tk.Scrollbar(listbox_frame, orient="vertical")
scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview())

entry1 = tk.Entry(root)
entry1.pack()
entry1.insert(0, "Aufgabe")
entry1.bind('<Button-1>', lambda event: eingabe_entfernen(event, entry1))

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

aufgabe_add_btn = tk.Button(button_frame, text="Aufgabe hinzufügen", bg='green', fg='white', command=aufgabe_add)
aufgabe_add_btn.pack(side=tk.LEFT)

aufgabe_delete_btn = tk.Button(button_frame, text="Aufgabe löschen", bg='red', fg='white', command=aufgabe_delete)
aufgabe_delete_btn.pack(side=tk.LEFT)

ToolTip(aufgabe_add_btn, msg='Aufgabe')

tk.mainloop()




