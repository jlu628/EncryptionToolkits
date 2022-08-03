from fileinput import filename
from cryptography.fernet import Fernet
import sys
import os
import json
import base64

def decrypt(src, dst):
    with open(src, 'rb') as fh:
        content = fh.read()
        
    content = json.loads(base64.b64decode(content))
    dst = os.path.join(dst, content["filename"])
    content = Fernet(content["key"].encode("utf-8")).decrypt(content["data"].encode("utf-8"))
    
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

    dst, content = decrypt(src, dst)
    with open(dst, 'wb') as fh:
        fh.write(content)