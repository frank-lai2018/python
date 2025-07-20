#   裝飾器
#       含意:裝飾氣本質上就是一個閉包函數，他的好處就是在不修改於有代碼的基礎上，增加額外的功能
#       作用:在不改變原有代碼下添加新的功能
#       條件:
#           1.不修改原程式或函數代碼
#           2.不改變函數或程式的調用方法
#

def outer(fn):

    def inner():
        print("裝飾器....start")
        fn()
        print("裝飾器....end")
    return inner


@outer   # 語法糖，解析器讀到這行，就會呼叫outer裝飾器，把test函數當成參數傳進去執行
def test():
    print("test")


test()


@outer   # 語法糖，解析器讀到這行，就會呼叫outer裝飾器，把test1函數當成參數傳進去執行
def test1():
    print("test111")

  
test1()
