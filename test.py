import numpy as np


class MyClass:
    def __init__(self, name):
        self.name = name
    def method(self):
        print(self.name + "san, Hello World")
        
model = MyClass('Taro')
print(model.name)
# Taro
model.method()
# Tarosan, Hello World

class NewClass(MyClass):
    def __init__(self, name1, name2):
        super().__init__(name1)
# super(MyClass, self).__init__(name1) も可
        self.name2 = name2
    def new_method(self):
        self.method()
        print(self.name2 + 'san, Hello World')
model = NewClass('Taro', 'Jiro')
model.new_method()

class Demo:
    def __init__(self, a : list):
        self.a = a
        self.n = len(a)
        import pdb ;pdb.set_trace()
    def __len__(self):
        return len(self.a)
    def __getitem__(self, index):
        try:
            assert index<self.n
            return self.a[index]
        except:
            raise AssertionError('index out of range')
            # return 0 
            # pass 

A = Demo([1,2,3])
print(len(A)) # 3
print(A[0]) # 1
print(A[3]) # AssertionError
