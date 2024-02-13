class Car:
    def __init__(self, w):
        self.wheel = w
    
    def getWheel(self):
        return self.wheels
    
#main
c = Car(4)
n = c.getWheels()
print(n)