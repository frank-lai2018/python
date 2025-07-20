# 閉包
#   條件:
#       1.函數嵌套定義(函數裡面再定義函數)
#       2.內層函數使用外層函數的局部變數
#       3.外層函數返回值是內層函數的函數名
#

def outer():  # 外層函數
    n = 10  # 外層函數局部變數

    def inner():  # 內層函數
        print(n)  # 內層函數使用外層函數的局部變數
    return inner


print(outer())

# 第一種調用寫法
outer()()

# 第二種調用寫法

ot = outer()
ot()  # 調用內函數


def outer1(m):  # 外層函數
    n = 10  # 外層函數局部變數

    def inner1(o):  # 內層函數
        print("計算結果:", m+n+o)  # 內層函數使用外層函數的局部變數
    return inner1


outer1(10)(5)
