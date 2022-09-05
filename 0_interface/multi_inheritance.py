class Base1:
    def func1(self):
        print('func1')

class Base2:
    def func2(self):
        print('func2')

class MultiDerived(Base1, Base2):
    pass

test = MultiDerived()

test.func1()
test.func2()