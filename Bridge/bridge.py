# 
# Manuel Montero
# 

# Separates an object’s interface from its implementation

import abc, six


class abstractInterface:
  
  def __init__(self, interfaceImplementorObject): 
    self.interfaceImplementorObject = interfaceImplementorObject
    
  def abstractInterfaceGetValue(self): 
    return(self.interfaceImplementorObject.getValue() + 100)
  
  def abstractInterfaceGetValueOriginal(self): 
    return(self.interfaceImplementorObject.getValue())
    
    
@six.add_metaclass(abc.ABCMeta)    
class interfaceImplementor():
  
  @abc.abstractmethod
  def getValue(self): pass

  @abc.abstractmethod
  def setValue(self): pass


class objectType1(interfaceImplementor):
  
  __objectType1Value = 1
  def getValue(self): return(self.__objectType1Value)
  def setValue(self, val): self.__objectType1Value = val


class objectType2(interfaceImplementor):
  
  __objectType2Value = 2
  def getValue(self): return(self.__objectType2Value)
  def setValue(self, val): self.__objectType2Value = val


type1 = objectType1()
abstractInterfaceObject = abstractInterface(type1)
print(abstractInterfaceObject.abstractInterfaceGetValue())
print(abstractInterfaceObject.abstractInterfaceGetValueOriginal())
