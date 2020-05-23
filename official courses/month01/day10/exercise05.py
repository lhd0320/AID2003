class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand + "电话来电")
    def pay(self):
        print("已经支付%d"%(self.price))


huawei = Phone("华为", 10000, "黄色")
huawei.call()
iphone = Phone("苹果", 9000, "白色")
iphone.call()
iphone.pay()

