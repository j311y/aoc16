

def getInput(fileName):
    with open(fileName, 'r') as f:
        return ''.join([l.strip() for l in f.readlines()])

def getInputLines(fileName):
    with open(fileName, 'r') as f:
        return [l.strip() for l in f.readlines()]
