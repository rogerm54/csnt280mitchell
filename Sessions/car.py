class Car:
    def __init__(self,make,model,price):
        self.make = make
        self.model = model
        self.price = price
        
    def __str__(self):
        temp = self.make + ", " + self.model
        temp += ", $" + str(self.price)
        return temp
        
    def toXML(self):
        temp = "  <car>\n"
        temp += "    <make>" + self.make + "</make>\n"
        temp += "    <model>" + self.model + "</model>\n"
        temp += "    <price>" + str(self.price) + "</price>\n"
        temp += "  </car>"
        return temp
        
    def toJSON(self):
        temp = "    {\n"
        temp += '      "make" : "' + self.make + '",\n'
        temp += '      "model" : "' + self.model + '",\n'
        temp += '      "price" : ' + str(self.price) + "\n"
        temp += "    }"
        return temp
        
if (__name__ == "__main__"):
    c1 = Car("Toyota","Camry",25999.99)
    print(c1.__str__())
    print(c1.toXML())
    print(c1.toJSON())
