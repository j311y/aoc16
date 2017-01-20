
import md5
import numpy
import sys

testInput ='abc'

testResult = '18f47a30'

actualInput = 'uqwqemis'

def isMatchingHash(testHash):
    matches = True
    for c in testHash[:5]:
        matches = matches and c == '0'
    return matches

def getHashStr(inStr):
    return md5.new(inStr).hexdigest()

solutionByInput = {}

def calculate(inputStr):
    if (inputStr in solutionByInput):
        return solutionByInput[inputStr]
    password = []
    # ahoy thar. exciting opportunities for optimizations ho!
    for i in xrange(sys.maxint):
        testHash = getHashStr(inputStr + str(i))
        if (isMatchingHash(testHash)):
            password.append(testHash[5])
            if (len(password) == 8):
                break
    passwordStr = ''.join(password)
    solutionByInput[inputStr] = passwordStr
    return passwordStr

def solveTest():
    result = calculate(testInput)
    return result == testResult

def solve():
    result = calculate(actualInput)
    return result

