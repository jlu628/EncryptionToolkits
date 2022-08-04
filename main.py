from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
from encrypt import encrypt
from decrypt import decrypt
from utils import readFile, writeFile

root = Tk()
root.title("Encryption Toolkits")
root.minsize(width=500, height=300)
root.resizable(False, False)
directoryHistory = "/Users/jerry/Desktop/"

# Logics
def updateProcess(msg):
    processLabel.config(text=msg)
    root.update()

def getFile(chooseFor):
    global directoryHistory
    if (chooseFor == "src"):
        if (actionChoice.get() == "decr"):
            response=filedialog.askopenfilename(initialdir=directoryHistory, filetypes=[("ENCR", "*.encr")])
        else:
            response=filedialog.askopenfilename(initialdir=directoryHistory)
        srcEntry.delete(0,"end")
        srcEntry.insert(0, response)
        directoryHistory = "/".join(response.split("/")[:-1]) if len(response) > 0 else directoryHistory
    elif (chooseFor == "dst"):
        response=filedialog.askdirectory(initialdir=directoryHistory)
        dstEntry.delete(0,"end")
        dstEntry.insert(0, response)
        directoryHistory = response if len(response) > 0 else directoryHistory


def encryptFile():
    src = srcEntry.get()
    dst = dstEntry.get()
    if not os.path.exists(src):
        messagebox.showerror(title="source error", message="Source folder does not exist")
        return
    if not os.path.exists(dst):
        messagebox.showerror(title="destination error", message="Destination folder does not exist")
        return

    # Read file
    updateProcess("Reading source file...")
    content = readFile(src)

    # Encryption
    updateProcess("Encrypting data...")
    dst, content = encrypt(content, src, dst)

    # Save result
    updateProcess("Saving encrypted file...")
    if os.path.exists(dst):
        response = messagebox.askyesno(title="File confliction", message=f"File {dst} already exists.\nDo you want to replace it?")
        if not response:
            updateProcess("")
            return
    writeFile(content, dst)

    updateProcess("Done!")
    messagebox.showinfo(message=f"Successfully encrypted {src} to {dst}")
    updateProcess("")


def decryptFile():
    src = srcEntry.get()
    dst = dstEntry.get()
    if not os.path.exists(src):
        messagebox.showerror(title="source error", message="Source folder does not exist")
        return
    if not os.path.exists(dst):
        messagebox.showerror(title="destination error", message="Destination folder does not exist")
        return
    if not src.split(".")[-1] == "encr":
        messagebox.showerror(title="file error", message="Decrypted file must have .encr extension")
        return

    # Read file
    updateProcess("Reading source file...")
    content = readFile(src)

    # Decryption
    updateProcess("Decrypting data...")
    dst, content = decrypt(content, dst)

    # Save result
    if os.path.exists(dst):
        response = messagebox.askyesno(title="File confliction", message=f"File {dst} already exists.\nDo you want to replace it?")
        if not response:
            updateProcess("")
            return
    writeFile(content, dst)

    updateProcess("Done!")
    messagebox.showinfo(message=f"Successfully decrypted {src} to {dst}")
    updateProcess("")


def action():
    if actionChoice.get() == "encr":
        try:
            encryptFile()
        except:
            messagebox.showerror(title="unknown error", message="An unknown error occured")
    else:
        try:
            decryptFile()
        except:
            messagebox.showerror(title="unknown error", message="An unknown error occured")


# Create elements
titleLabel = Label(root, text="Encryption Toolkits", font="Helvetica 30 bold")
srcText = Label(root, text="Src:", font="Helvetica 15 bold")
dstText = Label(root, text="Dst:", font="Helvetica 15 bold", padx=10, pady=10)
srcEntry = Entry(root, width=30, borderwidth="2", relief="groove")
dstEntry = Entry(root, width=30, borderwidth="2", relief="groove")
chooseSrcButton = Button(root, text="browse", width=7, height=1, command=lambda:getFile("src"))
chooseDstButton = Button(root, text="browse", width=7, height=1, command=lambda:getFile("dst"))
EncrChoiseLabel = Label(root, text="encrypt")
DecrChoiseLabel = Label(root, text="decrypt")
actionChoice = StringVar()
actionChoice.set("encr")
chooseEncrButton = Radiobutton(root, value="encr", variable=actionChoice)
chooseDecrButton = Radiobutton(root, value="decr", variable=actionChoice)
goButton = Button(root, text="go!", width=4, height=1,command=action)
processLabel = Label(root, width=30)

# Placement
titleLabel.place(relx=.5, rely=.1, anchor="center")

srcText.place(relx=.1, rely=.3, anchor="center")
srcEntry.place(relx=.5, rely=.31, anchor="center")
chooseSrcButton.place(relx=.9, rely=.3, anchor="center")

dstText.place(relx=.1, rely=.5, anchor="center")
dstEntry.place(relx=.5, rely=.51, anchor="center")
chooseDstButton.place(relx=.9, rely=.5, anchor="center")

EncrChoiseLabel.place(relx=.35, rely=.7, anchor="center")
DecrChoiseLabel.place(relx=.65, rely=.7, anchor="center")
chooseEncrButton.place(relx=.35, rely=.65,anchor="center")
chooseDecrButton.place(relx=.65, rely=.65,anchor="center")

goButton.place(relx=.5, rely=.8,anchor="center")
processLabel.place(relx=.5, rely=.9,anchor="center")

root.mainloop()