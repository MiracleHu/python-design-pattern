from abc import ABCMeta, abstractmethod

class Payment:
    def pay(self, money):
        raise NotImplemented

class PaymentABS(metaclass=ABCMeta):
    @abstractmethod # strong restriction for sub class
    def pay(self, money):
        pass

class Alipay(PaymentABS):
    def pay(self, money):
        print('done Ali payment: ', money)

class WechatPay(Payment):
    pass
    # def pay(self, money):
    #     pass

class Paypal(PaymentABS):
    pass

p1 = Alipay()
p1.pay(100)

p2 = WechatPay()
# p2.pay(100)

p3 = Paypal() # Can not even instantiate