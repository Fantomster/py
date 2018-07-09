def repeater(value):
    while True:
        yield value

# for x in repeater('Hi'):
#     print(x)

# One line generator
# iterator = ('Hello' for i in range(3))

def repeat_three_times(value):
    yield value
    yield value
    yield value

for x in repeat_three_times('Hey there'):
    print(x)
repeater1 = repeat_three_times('Hey there')
next(repeater1)
next(repeater1)
next(repeater1)
next(repeater1)
next(repeater1)