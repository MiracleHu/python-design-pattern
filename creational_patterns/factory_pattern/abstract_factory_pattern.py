from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass

'''
vegetarian pizzas are prepared with an appropriate crust, vegetables, and seasoning, 
and nonvegetarian pizzas are served with nonvegetarian toppings on top of vegetarian pizzas.
'''
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxeVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxeVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class PizzaStore:
    def __init__(self):
        pass
    '''
    When an end user approaches PizzaStore and asks for an American nonvegetarian pizza, 
    USPizzaFactory is responsible for preparing the vegetarian pizza as the base 
    and serving the nonvegetarian pizza with ham on top!
    '''
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()
