from cryptography.fernet import Fernet
import sys
import os
import json
import base64

def encrypt(src, dst):
    key = Fernet.generate_key()
    with open(src, 'rb') as file:
        file = file.read()

    content = {
        "data": Fernet(key).encrypt(file).decode("utf-8"),
        "filename": src.split("/")[-1],
        "key": key.decode("utf-8")
    }
    content = base64.b64encode(json.dumps(content).encode('ascii'))

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
        raise ValueError("Source folder does not exist")
    if not os.path.exists(dst):
        raise ValueError("Destination folder does not exist")
        
    dst, content = encrypt(src)
    with open(dst, 'wb') as fh:
        fh.write(content)