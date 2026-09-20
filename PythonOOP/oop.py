class Kettle(object):
    
    power_source = "electricity"    # similar to static field

    def __init__(self, make, price) -> None:
        self.make = make
        self.price = price
        self.on = False
    
    def switch_on_off(self):
        self.on = not self.on


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.price, kenwood.make)
kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", "14.55")

# print("Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}".format(kenwood=kenwood, hamilton=hamilton))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on_off()
print(hamilton.on)

Kettle.switch_on_off(kenwood)
print(kenwood.on)

print("*" * 50)


kenwood.power = 1.5
print(kenwood.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print("Switch to atomic power")

Kettle.power_source = 'Atomic'
print(Kettle.power_source)
print("Switch kenwood to gas power")
kenwood.power_source = 'Gas'
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
