from cryptography.fernet import Fernet
import sys
import os
import pickle
import base64
from utils import readFile, writeFile

def decrypt(content, dst):    
    content = pickle.loads(base64.b64decode(content))
    dst = os.path.join(dst, content["filename"])
    content = Fernet(content["key"]).decrypt(content["data"])
    
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
    dst, content = decrypt(content, dst)
    writeFile(content, dst)