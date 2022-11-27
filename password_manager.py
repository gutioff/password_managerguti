import random
import pyperclip as pc

def add():
    passr = input("Platfrom name: ")
    passr2 = input("Name: ")
    passr3 = input("Password: ")
    lpass = len(passr3)
    if lpass < 10:
        print("Password non molto sicura ti consiglio di cambiarla..")
        print("")
    with open("password.txt", "a") as f:
        f.write("|Platform: "+ passr + " |Name: " + passr2 + " |Password: " + passr3 + "\n")
def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            print(line)
def remove():
    print("queste sono tutte le tue password ")
    view()
    print("scrivi ora quella che vuoi cancellare copiandola!")
    rem = input()
    with open("password.txt", "r") as f:
        lines = f.readlines()
    with open("password.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != rem:
                f.write(line)
def create():
    password = ""
    caratteri = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMç°°§*é^?=)(é*@#][/&%$£!_.,m"
    print("scegli di quanto deve essere lunga la password!")
    choose = input()
    for i in range(int(choose)):
        password += random.choice(caratteri)
    print(password)
    print("Password copiata automaticamente!")
    pc.copy(password)
    print("")

while True:
    print("")
    print("Welcome to password manager...")
    print("scrivi ADD per aggiungere una password VIEW per vederle REMOVE per toglierne una e CREATE per crearne una nuova")
    passq = input().lower()

    if passq == "add":
        add()
    elif passq == "view":
        view()
    elif passq == "remove":
        remove()
    elif passq == "create":
        create()
    else:
        print("scrivi un opzione corretta! ")
        print("")
        continue