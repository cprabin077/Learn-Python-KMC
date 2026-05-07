class A():
    __a = 1
    b = __a + 1

    def __add(self):
        return self.__a + self.b
    
    def public_add(self):
        return self.__add()
    
obj = A()
print(obj.b) # 2
# print(obj.__add()) # error





