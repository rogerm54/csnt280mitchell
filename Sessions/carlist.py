from car import Car
class CarList:
    def __init__(self):
        self.car_list = []

    def add(self,car):
        self.car_list.append(car)
       
    def toXML(self):
        temp = '<?xml version="1.0" ?>\n'
        temp += '<cars>\n'
        for car in self.car_list:
            temp += car.toXML() + "\n"
        temp += '</cars>'
        return temp

if (__name__ == "__main__"):
	carlist = CarList()
	c1 = Car('Toyota','Camry',25999.99)
	c2 = Car('Honda','Accord',25235.99)
	carlist.add(c1)
	carlist.add(c2)
	print(carlist.toXML())
	
	
	
	
	
	
