from builtins import list


def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

print_vector(0, 1, 0)

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]
print_vector(*tuple_vec)
print_vector(*list_vec)

genexpr = (x * x for x in range(3))
print_vector(*genexpr)

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)
print_vector(*dict_vec)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'__repr__ {self.color} car'

    def __str__(self):
        return f'__str__ {self.color} car'


my_car = Car('red', 37281)
print(my_car)
print('{}'.format(my_car))
print(repr(my_car))
