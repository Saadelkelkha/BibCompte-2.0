from tkinter import *
from BibCompte import compte, compteCourant, compteEpargne
import json
from tkinter import ttk
import tkinter as tk

window = Tk()
window.title("BANK")
# window.geometry('500x400')

def Creation_COMPTE():
    # Function to create a new account based on user input
    account_type = type_var.get()
    if account_type == "Epargne":
        ACCOUNT = compteEpargne.CompteEpargne(propentry.get(), soldeentry.get(), interetentry.get())

        with open("data.json", "r") as file:
            date = json.load(file)
            date["compte"].append({
            "Numero": compte.Compte.Getnumero() ,
            "Proprietaire": propentry.get(),
            "SoldeIntial": soldeentry.get(),
            "Taux interet": interetentry.get(),
            "Montant Decouvert": ""
        })
            file.close()
    else:
        ACCOUNT = compteCourant.CompteCourant(propentry.get(), soldeentry.get(), mdecouvertentry.get())

        with open("data.json", "r") as file:
            date = json.load(file)
            date["compte"].append({
            "Numero": compte.Compte.Getnumero() ,
            "Proprietaire": propentry.get(),
            "SoldeIntial": soldeentry.get(),
            "Taux interet": "",
            "Montant Decouvert": mdecouvertentry.get()
        })
    with open("data.json", "w") as file:
        json.dump(date, file, indent=2)

    nm.config(text = compte.Compte.Getnumero() + 1)
    def insert_data(data_list):
        for account in data_list:
            tree.insert("", "end", values=(
                account["Numero"],
                account["Proprietaire"],
                account["SoldeIntial"],
                account["Taux interet"],
                account["Montant Decouvert"]
            ))

    # Create a Treeview widget
    tree = ttk.Treeview(window, columns=("Numero", "Proprietaire", "SoldeIntial", "Taux interet", "Montant Decouvert"), show="headings")

    # Define column headings 
    tree.heading("Numero", text="Numero")
    tree.heading("Proprietaire", text="Proprietaire")
    tree.heading("SoldeIntial", text="Solde Intial")
    tree.heading("Taux interet", text="Taux interet")
    tree.heading("Montant Decouvert", text="Montant Decouvert")

    # Specify column widths
    for column in ("Numero", "Proprietaire", "SoldeIntial", "Taux interet", "Montant Decouvert"):
        tree.column(column, width=100)

    # Insert data from the json fichier
    with open("data.json", "r") as file :
        data = json.load(file)
    

    insert_data(data["compte"])

    # Add a vertical scrollbar
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Pack everything
    tree.grid(column=3, row=7, sticky=(tk.W, tk.E, tk.N, tk.S))
    vsb.grid(column=4, row=7, sticky=(tk.N, tk.S))
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    
        
    

def type_selected():
    # Function to handle radio button selection for account type
    account_type = type_var.get()
    if account_type == "Epargne":
        interetentry.config(state=NORMAL)
        mdecouvertentry.config(state=DISABLED)
    else:
        interetentry.config(state=DISABLED)
        mdecouvertentry.config(state=NORMAL)

numero = Label(window, text="Numero: ")
numero.grid(row=0, column=0)

nm = Label(window,text= compte.Compte.Getnumero() + 1)
nm.grid(row=0, column=1)

prop = Label(window, text="Proprietaire: ")
prop.grid(row=1, column=0)

propentry = Entry(window)
propentry.grid(row=1, column=1)

solde = Label(window, text="Solde initial: ")
solde.grid(row=2, column=0)

soldeentry = Entry(window)
soldeentry.grid(row=2, column=1)

solde = Label(window, text="Euro")
solde.grid(row=2, column=2)

type = Label(window, text="Type: ")
type.grid(row=3, column=0)

type_var = StringVar()

type_courant = Radiobutton(window, text="Courant", variable=type_var, value="Courant", command=type_selected)
type_courant.grid(row=3, column=1)

type_epargne = Radiobutton(window, text="Epargne", variable=type_var, value="Epargne", command=type_selected)
type_epargne.grid(row=3, column=2)

interet = Label(window, text="Taux interet: ")
interet.grid(row=4, column=0)

interetentry = Entry(window)
interetentry.grid(row=4, column=1)

mdecouvert = Label(window, text="M.Decouvert: ")
mdecouvert.grid(row=5, column=0)

mdecouvertentry = Entry(window)
mdecouvertentry.grid(row=5, column=1)

button = Button(window,text=" Creation Compte",command=Creation_COMPTE)
button.grid(row=6,column=1)



def insert_data(data_list):
    for account in data_list:
        tree.insert("", "end", values=(
            account["Numero"],
            account["Proprietaire"],
            account["SoldeIntial"],
            account["Taux interet"],
            account["Montant Decouvert"]
        ))

# Create a Treeview widget
tree = ttk.Treeview(window, columns=("Numero", "Proprietaire", "SoldeIntial", "Taux interet", "Montant Decouvert"), show="headings")

# Define column headings
tree.heading("Numero", text="Numero")
tree.heading("Proprietaire", text="Proprietaire")
tree.heading("SoldeIntial", text="Solde Intial")
tree.heading("Taux interet", text="Taux interet")
tree.heading("Montant Decouvert", text="Montant Decouvert")

# Specify column widths
for column in ("Numero", "Proprietaire", "SoldeIntial", "Taux interet", "Montant Decouvert"):
    tree.column(column, width=100)

# Insert data from the json fichier
with open("data.json", "r") as file :
    data = json.load(file)
    

insert_data(data["compte"])

# Add a vertical scrollbar
vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Pack everything
tree.grid(column=3, row=7, sticky=(tk.W, tk.E, tk.N, tk.S))
vsb.grid(column=4, row=7, sticky=(tk.N, tk.S))
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

window.mainloop()
