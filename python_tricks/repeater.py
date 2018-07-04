# class Repeater:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return RepeaterIterator(self)
#
# class RepeaterIterator:
#     def __init__(self, source):
#         self.source = source
#
#     def __next__(self):
#         return self.source.value

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

# repeater = Repeater('hello')
# for item in repeater:
#     print(item)

repeater = Repeater('Hello')
iterator = iter(repeater)
print(next(iterator))
print(next(iterator))
print(next(iterator))