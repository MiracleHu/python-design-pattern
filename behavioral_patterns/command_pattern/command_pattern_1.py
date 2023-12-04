from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        self.stock.sell()

class StockTrade:
    def buy(self):
        print("You will buy stocks")
    def sell(self):
        print("You will sell stocks")

class Agent:
    def __init__(self):
        # With the Command pattern, you can store the sequence of commands,
        # and when asked for a redo, rerun the same set of actions.
        self.__orderQueue = []
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

if __name__ == '__main__':
    #Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)
    #Invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
