class Singleton(object):
    instanceAddr = ""

    def __new__(cls, *args, **kwargs):
        if Singleton.instanceAddr == "":
            Singleton.instanceAddr = super().__new__(cls)
        return Singleton.instanceAddr
    
    
r1 = Singleton()
print(r1)
r2 = Singleton()
print(r2)