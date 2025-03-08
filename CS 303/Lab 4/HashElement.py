class HashElement:

    # default constructor
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def getKey(self):
        return self.key
    
    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value