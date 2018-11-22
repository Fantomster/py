import random
from functools import partial, reduce

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

print(len(integer_list))
print(sum(integer_list))
print(list_of_lists)

x = range(10)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
# x[0] = -1

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

1 in [1, 2, 3]

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x + [7, 8])

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print("Cannot modify a tuple")


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

# print(sp)
# print(s)
# print(p)

all([])  # True, no falsy elements in the list
any([])  # False, no truthy elements in the list

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4,3,-2,1]

# sort the words and counts from highest count to lowest
# wow wow
# wc = sorted(word_counts.items(),
#             key=lambda (word, count): count,
#             reverse=True)

even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

square_dict = { x : x * x for x in range(5) }
square_set = { x * x for x in [1, -1] }

zeroes = [0 for _ in even_numbers] # has the same length as even_numbers

pairs = [(x, y)
         for x in range(10)
         for y in range(10)]    # 100 pairs

increasing_pairs = [(x, y)                     # only pairs with x < y
                    for x in range(10)         # range(lo, hi) equals
                    for y in range(x + 1, 10)] # [lo, lo + 1, ..., hi -1]

# generator
def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1
# create generator 1
for i in lazy_range(10):
    # do_something_with(i)
    i+=1

# create generator 2
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# print(lazy_evens_below_20)

for item in lazy_evens_below_20:
    print(item)

four_uniform_randoms = [random.random() for _ in range(4)]

# Functional tools
def exp(base, power):
    return base ** power

# unwieldy
def two_to_the(power):
    return exp(2, power)

# more likely
two_to_the = partial(exp, 2)
print(two_to_the(3))

square_of = partial(exp, power=2)
print(square_of(3))

def double(x):
    return 2 * x

xs = [1,2,3,4]
twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)

# you can use map with multiple-argument functions if you provide multiple lists
def multiply(x, y): return x * y

products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]

# similarly, filter does the work of a list-comprehension if:
def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]   # [2, 4]
x_evens = filter(is_even, xs)             # same as above
list_evener = partial(filter, is_even)    #  *function* that filters a list
x_evens = list_evener(xs)                 # again [2, 4]

# and reduce combines the first two elements of a list, then that result with
# the third, that result with the fourth, and so on, producing a single result
x_product = reduce(multiply, xs)          # = 1 * 2 * 3 * 4 = 24
print()
print(x_product)
list_product = partial(reduce, multiply)  # *function* that reduces a list
x_product = list_product(xs)              # again = 24
print(x_product)

# Enumerate
# not Pythonic
# for i in range(len(documents)):
#     document = documents[i]
#     do_something(i, document)

# also not Pythonic
# i = 0
# for document in documents:
#     do_something(i, document)
#     i += 1

# The Pythonic solution is enumerate, which produces tuples (index, element)
# for i, document in enumerate(documents):
#     do_something(i, document)

# similarly, if we just want the indexes
# for i in range(len(documents)): do_something(i)   # not Pythonic
# for i, _ in enumerate(documents): do_something(i) # Pythonic

# Zip and Argument unpacking
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(list(zip(list1, list2))) # is [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

# you can use argument unpacking with any function
def add(a,b): return a + b

add(1, 2) # returns 3
add([1, 2]) # TypeError!
add(*[1, 2]) # returns 3

# args and kwargs
def f2(x, y):
    return x + y

g = doubler(f2)
# print(g(1, 2)) # TypeError: g() takes exactly 1 argument (2 given)

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")

# prints
#  unnamed args: (1,2)
#  keyword args: {'key2': 'word2', 'key': 'word'}

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1,2]
z_dict = {"z": 3}
print(other_way_magic(*x_y_list, **z_dict)) # 6

def double_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1, 2)) # 6



