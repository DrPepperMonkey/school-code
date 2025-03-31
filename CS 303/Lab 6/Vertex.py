class Vertex:

    '''
    This is the default constructor. You may add attributes or helper functions as you see fit. Make sure to update the constructor as needed.
    '''
    def __init__(self, nameIn):
        self.setName(nameIn)
        self.setColor(None)
        self.setD(None)
        self.setPi(None)

    def setName(self, nameIn):
        self.name = nameIn

    def getName(self):
        return self.name

    def setColor(self, colorIn):
        self.color = colorIn

    def getColor(self):
        return self.color
    
    def setD(self, dIn):
        self.d = dIn

    def getD(self):
        return self.d
    
    def setPi(self, piIn):
        self.pi = piIn

    def getPi(self):
        return self.pi
    
