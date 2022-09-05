from abc import ABCMeta, abstractmethod

class PaymentABS(metaclass=ABCMeta):
    @abstractmethod # strong restriction for sub class
    def pay(self, money):
        pass

class Alipay(PaymentABS):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print('done Huabei payment: ', money)
        else:
            print('done Ali payment: ', money)

class WechatPay(PaymentABS):
    def pay(self, money):
        print('done Wechat payment: ', money)

class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# 单一职责原则，有利于扩展，只添加新代码，不用更改已有代码
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechatpayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

alipayment_factory = AlipayFactory()
payment1 = alipayment_factory.create_payment()
payment1.pay(100)

huabei_factory = HuabeiFactory()
payment2 = huabei_factory.create_payment()
payment2.pay(200)