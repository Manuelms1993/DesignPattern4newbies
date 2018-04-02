# ------------------------------------------------------------------------
#
#
# Manuel Montero
#
#
# ------------------------------------------------------------------------

# In software engineering, the adapter pattern is a software design pattern
# (also known as Wrapper, an alternative naming shared with the Decorator pattern)
# that allows the interface of an existing class to be used as another interface.
# It is often used to make existing classes work with others without modifying their source code.


class Interface1:
    def method_1(self): pass
    def method_2(self): pass
    def method_3(self): pass

class Interface2:
    def method_1(self): pass
    def method_2(self): pass
    def method_3(self): pass
    def method_4(self): pass

class socket(Interface1):
    def method_1(self): return("Method 1 socket")
    def method_2(self): return("Method 2 socket")
    def method_3(self): return("Method 3 socket")

class adapter(Interface2):

    __socket = None

    def __init__(self, socket): self.__socket=socket
    def method_1(self): return("Method 1 adapter")
    def method_2(self): return(self.__socket.method_2())
    def method_3(self): return(self.__socket.method_3())


if __name__ == "__main__":

    socketObject = socket()
    adapterObject = adapter(socketObject)

    print(adapterObject.method_1())
    print(adapterObject.method_2())
    print(adapterObject.method_3())
    print(adapterObject.method_4())