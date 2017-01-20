
import collections
import inputhelper

testInput = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

testResult = 'easter'

def calculate(inputLines):
    cnts = []
    if (len(inputLines) == 0):
        raise ValueError("inputLines must have at least one element")

    for index, c in enumerate(inputLines[0]):
        cnts.append(collections.Counter())
        cnts[index][c.lower()] += 1

    numColumns = len(cnts)

    for l in inputLines[1:]:
        for index, c in enumerate(l):
            if (index >= numColumns):
                raise ValueError("line {} doesn't have {} chars".format(l, numColumns))
            cnts[index][c.lower()] += 1

    chars = []
    for i in range(len(cnts)):
        columnChars = cnts[i].items()
        columnChars.sort(key=lambda p: p[1], reverse=True)
        chars.append(columnChars[0][0])

    return ''.join(chars)

def solveTest():
    result = calculate(testInput.split('\n'))
    print "got '{}'".format(result)
    return result == testResult

def solve():
    result = calculate(inputhelper.getInputLines('in6.txt'))
    return result

