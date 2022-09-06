class Singleton:
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls) # cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a):
        self.a = a

ms1 = MyClass(1)
ms2 = MyClass(2) # 不会创建新的instance 但是会进行一次__init__
print(ms1.a, ms2.a)
print(id(ms1), id(ms2))
"""
2 2
139843914173312 139843914173312
"""