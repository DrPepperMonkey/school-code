class HashMap:
    
    def __init__(self, size):
        self.setSize(size)
        self.setArr(self.size)

    def setSize(self, size):
        self.size = size

    def setArr(self, size):
        self.arr = [None] * size

def hashFunc(key,size:int, prime: int):
    hash = 0
    for i in range(len(key)):
        hash += (ord(key[i]) * prime**i)
    hash = (hash % size)
    return hash

def getLinVal(key, hm: HashMap, prime: int):
    hash = hashFunc(key,hm.size, prime)
    i = hash
    while hm[i][0] != key:
        i += 1
    return hm[i][1]

def linHash(key, value, arr, prime: int):
    hm = HashMap(len(arr))
    hash = hashFunc(key,hm.size, prime)
    while hm[hash] != None:
        hash += 1
        if hash >= len(hm.size):
            hash = 0
    hm[hash] = [key,value]

def getQuadVal(key, hm: HashMap, prime: int):
    hash = hashFunc(key,hm.size, prime)
    i = 1
    while hm[hash][0] != key:
        hash += (i**2)
        i += 1
        if hash >= hm.size:
            hash = 0
            i = 1
    return hm[hash][1]

def quadHash(key, value, arr, prime: int):
    hm = HashMap(len(arr))
    hash = hashFunc(key, hm.size, prime)
    i = 1
    while hm[hash] != None:
        hash += (i**2)
        i += 1
        if hash >= hm.size:
            hash = 0
            i = 1
    hm[hash] = [key,value]

def doubleHash(key, value, arr):
    hm1 = HashMap(len(arr))
    hash1 = hashFunc(key,hm1.size, 31)
    hash2 = hashFunc(key, hm1.size//8, 37)
    if hm1[hash1] != None:
        hm1[hash1][hash2] = [key,value]
    hm1[hash1] = HashMap(hm1.size//8)
    hm1[hash1][hash2] = [key,value]
    return hm1

def doubleHashValue(key, hm: HashMap):
    hash1 = hashFunc(key,hm.size,31)
    hash2 = hashFunc(key,hm.size//8,37)
    return hm[hash1][hash2][1]


    

    


def linkedHash():
    ... 

def hashSelect(hashIn: int, key, value, arr):
    match hashIn:
        case 0:
            return linHash(key, value, arr)
        case 1:
            return quadHash(key, value, arr)
        case 2:
            return doubleHash(key, value, arr)
        case 3:
            return linkedHash(key, value, arr)
        
def main():
    "hashIn = int(input('Input hashing function\n'))"
    arr = [None] * 100
    hm = doubleHash('mia','foo', arr)
    val = doubleHashValue('mia', hm)
    return val

print(main())