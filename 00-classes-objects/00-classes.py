class Car:
    def __init__(self, modelname, yearm, price):
        self.modelname = modelname
        self.yearm = yearm
        self.price = price

    def price_inc(self):
        self.price = (self.price*1.5)


honda = Car('honda', 2008, 70000)
honda.cc = 1500
tat = Car('tata', 2009, 80000)
print(honda.price)
print(tat.price)

print(honda.__dict__)
print(tat.__dict__)
honda.price_inc()
print(honda.price)

