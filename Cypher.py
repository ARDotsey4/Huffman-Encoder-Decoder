class CypherKey:
    def __init__(self, file=None):
        self.freqDict = {}
        self.keyDict = {}
        self.fillDicts(file)

    def fillDicts(self, file):
        if self.freqDict == {}:
            for i in range(0,256):
                self.freqDict[chr(i)] = 0
                self.keyDict[chr(i)] = ''
            print("Frequencies Initialized")

        if file==None:
            return print("No file found")
        
        fileHandler = open(file,'r')
        data = fileHandler.read()
        fileHandler.close()
        for char in data:
            self.freqDict[char] += 1
        return print("Frequencies updated")
    
    def generateKey(self):
        # Initialize priority queue
        pQueue = _PQueue()
        for entry in self.freqDict:
            pQueue.insert((entry,self.freqDict[entry]))

        # Start building cypher
        while len(pQueue.heap)>1:
            right = pQueue.popMin()
            left = pQueue.popMin()
            for chr in right[0]:
                self.keyDict[chr] = '1' + self.keyDict[chr]
            for chr in left[0]:
                self.keyDict[chr] = '0' + self.keyDict[chr]

            # Create new node and insert to pQueue
            pQueue.insert((left[0]+right[0], left[1]+right[1]))

class _PQueue:
    def __init__(self):
        self.heap = []

    """Insert a new element into the Min Heap."""
    def insert(self, node):
        self.heap.append(node)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i - 1) // 2][1] > self.heap[i][1]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    """Pow the root element from the Min Heap."""
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
            if left < len(self.heap) and self.heap[left][1] < self.heap[smallest][1]:
                smallest = left
            if right < len(self.heap) and self.heap[right][1] < self.heap[smallest][1]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break
        return minNode

    def printHeap(self):
        print("Min Heap:", self.heap)