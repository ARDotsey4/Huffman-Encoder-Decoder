# Huffman Encoding
# 31 May 2025

import Cypher

def encode(cypher, inFile=None, outFile=None):
    if inFile == None:
        return print("Input file required")

    inHandler = open(inFile,'r')
    data = inHandler.read()
    inHandler.close()

    outHandler = open("encryption.txt" if outFile == None else outFile, 'w')
    for char in data:
        outHandler.write(cypher.keyDict[char])
    outHandler.close()
    return print("Encryption Complete")


def decode(cypher, inFile=None, outFile=None):
    if inFile==None:
        return print("Input file required")
    
    inHandler = open(inFile,'r')
    data = inHandler.read()
    inHandler.close()

    if data.count('0') + data.count('1') != len(data):
        return print("Invalid input data")

    # Reverse encryption cypher
    maxRank = 0
    for char in cypher.keyDict:
        if len(cypher.keyDict[char]) > maxRank:
            maxRank = len(cypher.keyDict[char])

    DECYPHERLEN = 2**(maxRank+1) - 1
    deCypher = [None] * DECYPHERLEN
    for char in cypher.keyDict:
        index = 0
        for bit in cypher.keyDict[char]:
            index = 2 * index + 1 + int(bit)
        deCypher[index] = char

    # Decode input file
    outHandler = open("decryption.txt" if outFile == None else outFile, 'w')
    keyIndex = 0
    for bit in data:
        keyIndex = 2 * keyIndex + 1 + int(bit)
        if deCypher[keyIndex] != None:
            outHandler.write(deCypher[keyIndex])
            keyIndex = 0
    outHandler.close()
    return print("Decryption Complete")


if __name__ == "__main__":
    import random

    key = Cypher.CypherKey("plainMessage.txt")
    key.generateKey()
    encode(key, "plainMessage.txt")
    decode(key, "encryption.txt")