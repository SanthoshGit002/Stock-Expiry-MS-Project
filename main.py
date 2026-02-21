from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

window = tkinter.Tk()
window.title("Stock Management System")
window.geometry("1000x600")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)

content = tkinter.Frame(window)
content.grid(row=0, column=0, sticky="nsew")
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=2)
content.rowconfigure(0, weight=1)

tableFrame = tkinter.Frame(content)
tableFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tableFrame.rowconfigure(0, weight=1)
tableFrame.columnconfigure(0, weight=1)

columns = ("item", "qty", "expiry", "price", "supplier")
my_tree = ttk.Treeview(tableFrame, columns=columns, show="headings", height=18)
my_tree.heading("item", text="Item")
my_tree.heading("qty", text="Qty")
my_tree.heading("expiry", text="Expiry")
my_tree.heading("price", text="Price")
my_tree.heading("supplier", text="Supplier")

my_tree.column("item", width=220, anchor="w")
my_tree.column("qty", width=80, anchor="center")
my_tree.column("expiry", width=120, anchor="center")
my_tree.column("price", width=100, anchor="e")
my_tree.column("supplier", width=160, anchor="w")

vsb = ttk.Scrollbar(tableFrame, orient="vertical", command=my_tree.yview)
my_tree.configure(yscrollcommand=vsb.set)
my_tree.grid(row=0, column=0, sticky="nsew")
vsb.grid(row=0, column=1, sticky="ns")

entriesFrame = tkinter.LabelFrame(content, text="Form", borderwidth=5)
entriesFrame.grid(row=0, column=1, sticky="n", padx=(10, 20), pady=10, ipadx=6)

name_var = tkinter.StringVar()
qty_var = tkinter.StringVar()
expiry_var = tkinter.StringVar()
price_var = tkinter.StringVar()
supplier_var = tkinter.StringVar()

Label(entriesFrame, text="Item Name").grid(row=0, column=0, sticky="w", padx=8, pady=6)
Entry(entriesFrame, textvariable=name_var, width=28).grid(row=0, column=1, padx=8, pady=6)

Label(entriesFrame, text="Quantity").grid(row=1, column=0, sticky="w", padx=8, pady=6)
Entry(entriesFrame, textvariable=qty_var, width=28).grid(row=1, column=1, padx=8, pady=6)

Label(entriesFrame, text="Expiry (YYYY-MM-DD)").grid(row=2, column=0, sticky="w", padx=8, pady=6)
Entry(entriesFrame, textvariable=expiry_var, width=28).grid(row=2, column=1, padx=8, pady=6)

Label(entriesFrame, text="Price").grid(row=3, column=0, sticky="w", padx=8, pady=6)
Entry(entriesFrame, textvariable=price_var, width=28).grid(row=3, column=1, padx=8, pady=6)

Label(entriesFrame, text="Supplier").grid(row=4, column=0, sticky="w", padx=8, pady=6)
Entry(entriesFrame, textvariable=supplier_var, width=28).grid(row=4, column=1, padx=8, pady=6)

btnColor = "#196678"
manageFrame = tkinter.LabelFrame(window, text="Manage", borderwidth=5)
manageFrame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
manageFrame.columnconfigure(tuple(range(7)), weight=1)

saveBtn = Button(manageFrame, text="SAVE", width=10, borderwidth=3, bg=btnColor, fg="white")
updateBtn = Button(manageFrame, text="UPDATE", width=10, borderwidth=3, bg=btnColor, fg="white")
deleteBtn = Button(manageFrame, text="DELETE", width=10, borderwidth=3, bg=btnColor, fg="white")
selectBtn = Button(manageFrame, text="SELECT", width=10, borderwidth=3, bg=btnColor, fg="white")
findBtn = Button(manageFrame, text="FIND", width=10, borderwidth=3, bg=btnColor, fg="white")
clearBtn = Button(manageFrame, text="CLEAR", width=10, borderwidth=3, bg=btnColor, fg="white")
exportBtn = Button(manageFrame, text="EXPORT EXCEL", width=15, borderwidth=3, bg=btnColor, fg="white")

saveBtn.grid(row=0, column=0, padx=5, pady=5)
updateBtn.grid(row=0, column=1, padx=5, pady=5)
deleteBtn.grid(row=0, column=2, padx=5, pady=5)
selectBtn.grid(row=0, column=3, padx=5, pady=5)
findBtn.grid(row=0, column=4, padx=5, pady=5)
clearBtn.grid(row=0, column=5, padx=5, pady=5)
exportBtn.grid(row=0, column=6, padx=5, pady=5)

sample_rows = [
    ("Paracetamol 500mg", "50", "2026-01-31", "2.50", "ACME Pharma"),
    ("Vitamin C 1000mg", "30", "2025-12-15", "5.00", "GoodHealth"),
    ("Bandage Pack", "120", "2028-06-01", "1.25", "MediSupplies")
]
for r in sample_rows:
    my_tree.insert("", "end", values=r)

window.resizable(False, False)
window.mainloop()
