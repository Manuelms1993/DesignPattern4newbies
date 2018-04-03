# 
# Manuel Montero
# 

# In software engineering, the composite pattern is a partitioning design pattern. 
# The composite pattern describes a group of objects that is treated the same way as a single
# instance of the same type of object. The intent of a composite is to "compose" objects into 
# tree structures to represent part-whole hierarchies. Implementing the composite pattern lets
# clients treat individual objects and compositions uniformly.

import abc, six


@six.add_metaclass(abc.ABCMeta)  
class ComponentObject:
    
    @abc.abstractmethod
    def getName(self): pass
  
  
class Composite(ComponentObject):

    __name = None

    def __init__(self, name):
        self._children = set()
        self.__name = name
    
    def getName(self):
        print(self.__name)
        for child in self._children: child.getName()

    def add(self, component):
        self._children.add(component)


class primitiveObject(ComponentObject):

    __name = None

    def __init__(self, name):
        self._children = set()
        self.__name = name
        
    def getName(self): print(self.__name)


primitiveObject1 = primitiveObject("Leaf1")
primitiveObject2 = primitiveObject("Leaf2")
compositeBIG = Composite("Composite")
compositeSMALL = Composite("compositeSMALL")
compositeBIG.add(primitiveObject1)
compositeSMALL.add(primitiveObject2)
compositeBIG.add(compositeSMALL)
compositeBIG.getName()
