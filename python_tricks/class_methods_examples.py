class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
# print(obj.method())
# print(MyClass.method(obj))
# print(obj.classmethod())

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozarella', 'tomatoes', 'ham'])

print(Pizza(['cheese', 'tomatoes']))
print(Pizza.margherita())
print(Pizza.prosciutto())