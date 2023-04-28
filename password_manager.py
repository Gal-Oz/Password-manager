from cryptography.fernet import Fernet


'''''
def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file:
        key_file.write(key)'''''
#יצירת מפתח הצפנה של התוכנה


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


master_pwd = input ("What is the master password? ").lower()
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("password.txt" , "r") as f:
        for line in f.readlines():
            data = line.rstrip()   #מחיקת רווחים בין השורות
            user, passw = data.split("|")   #פיצול בין תו מסויים
            print("User Name:", user, "| Password:" , fer.decrypt(passw.encode()).decode())


def add():
    name = input ("Account Name: ")
    pwd = input ("Password: ")

    with open("password.txt" , "a") as f:
        f.write (name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input ("Would you like to add a new password or view existing ones (view , add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue