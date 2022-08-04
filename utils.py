def readFile(src):
    with open(src, 'rb') as fh:
        content = fh.read()
    return content

def writeFile(content, dst):
    with open(dst, 'wb') as fh:
        fh.write(content)