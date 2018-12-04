class Flower:
    """flower that has a name, num of petals, and prices"""
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price
    def setName(self, name):
        self._name = name
    def setPetals(self, petals):
        self._petals = petals
    def setPrice(self, price):
        self._price = price
    def getName(self):
        return self._name
    def getPetals(self):
        return self._petals
    def getPrice(self):
        return self._price

if __name__ == "__main__":
    flower = Flower('rose', 6, 100.0)
    print(flower.getPrice())
