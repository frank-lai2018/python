# 1.__init__()和__new__()
# 1.1 __init__():初始化對象
# class Test(object):
#     def __init__(self):
#         print("這是__init__()")
#         print(self)


# te = Test()
# 1.2 __new__(): object基底類別提供的內建的靜態方法
# 作用: 1.在記憶體中為物件分配空間 2.傳回物件的引用


# class Test(object):
#     def __init__(self):
#         print("這是__init__()")
#         print(self)

#     def __new__(cls, *args, **kwargs):  # cls代表類別本身
#         print("我是__new__()")
#         print(cls)
        
# # 將父類別方法擴充 super().方法名稱()
# res = super().__new__(cls) # 方法重寫，res裡面保存的是實例物件的參考,
# # __new__()是靜態方法，形參裡面有cls，實參就必須傳cls
# return res
# # 注意: 重寫__new__()一定要return super().__new__(cls),
# # 否則python解釋器得不到分配空間的物件引用，就不會呼叫__init__()
# te = Test()
# print("te:",te)

class Test(object):
    def __init__(self):
        print("這是__init__()")
        print(self)

    def __new__(cls, *args, **kwargs):  # cls代表類別本身
        print("我是__new__()")
        print(cls)
        res1 = super().__new__(cls)
        res2 = super().__new__(cls)
        res3 = super().__new__(cls)
        print("res1:", res1)
        print("res2:", res2)
        print("res3:", res3)
        return res2


class Test2(object):
    def __init__(self):
        print("這是__init__()")
        print(self)

    def __new__(cls, *args, **kwargs):  # cls代表類別本身
        print("我是__new__()")
        print(cls)
        print("Test2:", super().__new__(cls))
        return super().__new__(cls)


class Person(object):
    def __new__(cls, *args, **kwargs):
        print("这是new方法")
        print("返回值:", super().__new__(cls))
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name    # 实例属性
        print("名字是:", self.name)


pe = Person('bingbing')
print('返回值:', pe)
# pe2 = Person('susu')
# print(pe2)

# r = Test2()

# print("final:", r)
