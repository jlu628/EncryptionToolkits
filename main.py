from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
from encrypt import encrypt
from decrypt import decrypt

root = Tk()
root.title("Encryption Toolkits")
root.minsize(width=500, height=300)
root.resizable(False, False)
directoryHistory = "/Users/jerry/Desktop/"

# Logics
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

    dst, content = encrypt(src, dst)
    if os.path.exists(dst):
        response = messagebox.askyesno(title="File confliction", message=f"File {dst} already exists.\nDo you want to replace it?")
        if not response:
            return
    with open(dst, 'wb') as fh:
        fh.write(content)
    messagebox.showinfo(message=f"Successfully encrypted {src} to {dst}")


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

    dst, content = decrypt(src, dst)
    if os.path.exists(dst):
        response = messagebox.askyesno(title="File confliction", message=f"File {dst} already exists.\nDo you want to replace it?")
        if not response:
            return
    with open(dst, 'wb') as fh:
        fh.write(content)
    messagebox.showinfo(message=f"Successfully decrypted {src} to {dst}")


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


# Placement
titleLabel.place(relx=.5, rely=.1, anchor="center")

srcText.place(relx=.1, rely=.3, anchor="center")
srcEntry.place(relx=.5, rely=.31, anchor="center")
chooseSrcButton.place(relx=.9, rely=.3, anchor="center")

dstText.place(relx=.1, rely=.5, anchor="center")
dstEntry.place(relx=.5, rely=.51, anchor="center")
chooseDstButton.place(relx=.9, rely=.5, anchor="center")

EncrChoiseLabel.place(relx=.35, rely=.75, anchor="center")
DecrChoiseLabel.place(relx=.65, rely=.75, anchor="center")
chooseEncrButton.place(relx=.35, rely=.7,anchor="center")
chooseDecrButton.place(relx=.65, rely=.7,anchor="center")

goButton.place(relx=.5, rely=.85,anchor="center")

root.mainloop()