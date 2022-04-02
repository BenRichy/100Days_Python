# using *args
# create function that adds all numbers passed to it

def add_all(*args):
    total = 0
    for number in args:
        total += number
    print(total)

add_all(4,2,1)

## using **kwargs

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)

# create class with kwargs
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Ford", model = "Fiesta")
print(my_car.model)