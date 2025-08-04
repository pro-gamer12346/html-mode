class rechtangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width
newregtangle = rechtangle (12,10)
print ("area of regtangle",newregtangle.area())