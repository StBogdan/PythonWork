#Read a file
def readFile(fileName):
    file = open(fileName)
    content = file.read()
    return content
