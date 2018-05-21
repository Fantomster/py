class ManagerFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# with ManagerFile('hello.txt') as f:
#     f.write('asda')
#     f.write('asda')
#     f.write('asda')
#     f.write('asda')

from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

# plus_3 = Adder(3)
# plus_3(4)