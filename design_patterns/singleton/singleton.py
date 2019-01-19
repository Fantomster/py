class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)

# Lazy instantiation in the Singleton pattern
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton() ## class initialized, but object not created
print("Object created", Singleton.getInstance()) # Object gets created here
s1 = Singleton() ## instance already created

class Borg:
    __shared_state = {"1": "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b': ", b) ## b and b1 are distinct objects
print("Borg Object 'b1': ", b1)
print("Object state 'b':", b.__dict__) ## b and b1 share same state
print("Object state 'b':", b.x) ## b and b1 share same state
print("Object state 'b':", b1.x) ## b and b1 share same state
print("Object state 'b1':", b1.__dict__)

class Borg1(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg1, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

