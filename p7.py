
import re
import inputhelper

testInput = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
ioxxoj[asdfgh]zxcvbn[ababaab]floott
aflar[qwerty]poiuyy[njkouf]flool"""

testResult = 3

def isAbba(seq):
    diff = seq[0] != seq[1]
    eq = seq[0] == seq[3] and seq[1] == seq[2]
    return diff and eq

def containsAbba(seq):
    for i in xrange(len(seq) - 3):
        if (isAbba(seq[i:i+4])):
            return True
    return False

def isSupported(ip):
    entries = re.split('\[|\]', ip)
    supported = None
    for index, entry in enumerate(entries):
        if ((index % 2) == 0):
            supported = supported or containsAbba(entry)
        elif (containsAbba(entry)):
            supported = False
            break
    return supported == True

def calculate(inputLines):
    numSupport = 0
    if (len(inputLines) == 0):
        raise ValueError("inputLines must have at least one element")

    for l in inputLines:
        if (isSupported(l.strip())):
            numSupport+=1

    return numSupport

def solveTest():
    result = calculate(testInput.split('\n'))
    print "got '{}'".format(result)
    return result == testResult

def solve():
    result = calculate(inputhelper.getInputLines('in7.txt'))
    return result

