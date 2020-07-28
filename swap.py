class Robot(object):
    def __init__(self):
        self.a=123
        self._b=123
        self.__c=123
object=Robot()
print(object.a) #public object
print(object._b) #protected Object
#print(object.__c) #provate


class Robot(object):
    def __init__(self):
        self.version=22
    def getVersion(self):
        print(self._version)
    def setVersion(self,version):
        self.__version=version
obj=Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version)
                            
