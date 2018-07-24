class AlwaysEquals:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)

class SameHash:
    def __hash__(self):
        return 1

print(AlwaysEquals() == AlwaysEquals())
print(AlwaysEquals() == 42)
print(AlwaysEquals() == 'waaat?')

objects = [AlwaysEquals(),
           AlwaysEquals(),
           AlwaysEquals()]
print([hash(obj) for obj in objects])

print({AlwaysEquals(): 'yes', AlwaysEquals(): 'no'})

a = SameHash()
b = SameHash()
print(a == b)
print(hash(a), hash(b))

print({a : 'a', b: 'b'})