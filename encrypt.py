from cryptography.fernet import Fernet
import sys
import os
import pickle
import base64
from utils import readFile, writeFile

def encrypt(content, src, dst):
    key = Fernet.generate_key()

    content = {
        "data": Fernet(key).encrypt(content),
        "filename": src.split("/")[-1],
        "key": key
    }
    content = base64.b64encode(pickle.dumps(content))

    filename = src.split("/")[-1].split(".")
    filename = filename[-1] if len(filename) == 1 else  ".".join(filename[:-1])
    dst = os.path.join(dst,filename) + ".encr"

    return dst, content
    

if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print("Wrong format, please provide source and destination folders.")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    if not os.path.exists(src):
        raise ValueError("Source file does not exist")
    if not os.path.exists(dst):
        raise ValueError("Destination folder does not exist")
        
    content = readFile(src)
    dst, content = encrypt(content, src, dst)
    writeFile(content, dst)