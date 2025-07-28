class Washer:
    height = 800   # 类属性

    def wash(self):  # self参数是类中的实例方法必须具备的
        print("我会洗衣服")
        print("方法中的self:", self)  # self表示当前调用该方法的对象


wa = Washer()
wa.wash()
