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

class PaymentFactory:
    def create_payment(self, provider):
        if provider == 'ali':
            return Alipay()
        elif provider == 'huabei':
            # can add more detail params here for init an instance
            return Alipay(use_huabei=True)
        elif provider == 'wechat':
            return WechatPay()
        else:
            raise TypeError('No such provider ', provider)

payment_factory = PaymentFactory()

payment1 = payment_factory.create_payment('ali')
payment1.pay(100)

payment2 = payment_factory.create_payment('huabei')
payment2.pay(200)