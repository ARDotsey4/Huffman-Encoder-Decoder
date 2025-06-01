# Huffman Encoding
# 31 May 2025

if __name__ == "__main__":
    pass

class CypherKey:
    def __init__(self, file=None):
        self.freqDict = {}
        self.fillFreqDict(file)
        self.keyHead = None

    def fillFreqDict(self, file):
        if self.freqDict == {}:
            for i in range(0,256):
                self.freqDict[chr(i)] = 0
            print("Frequencies Initialized")

        if file==None:
            return print("No file found")
        
        fileHandler = open(file,'r')
        data = fileHandler.read()
        fileHandler.close()
        for char in data:
            self.freqDict[char] += 1
        return print("Frequencies updated")
    
    def generateKey():
        pass

class PQueue:
    def __init__(self):
        self.heap = []

    """Insert a new element into the Min Heap."""
    def insert(self, node):
        self.heap.append(node)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i - 1) // 2][0] > self.heap[i][0]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    """Delete a specific element from the Min Heap."""
    def popMin(self):
        if self.heap == []:
            return None
        minNode = self.heap[0]
        i = 0
        self.heap[i] = self.heap[-1]
        self.heap.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break
        return minNode

    def printHeap(self):
        print("Min Heap:", self.heap)

def encode():
    pass

def decode():
    pass

