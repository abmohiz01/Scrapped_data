class MyClass:

    #CONSTRUCTOR
    def __init__(self,value):
        self._value= value

    #FUNCTION
    def show(self):
        print(f"The Value is {self._value}")

    '''GETTER FOR GETTING VALUES'''
    @property
    def value(self):
        return 10 * self._value

    '''SETTER OF SETTING GET VALUES'''

    @value.setter
    def value(self, newval):
        self._value = newval/10

obj = MyClass(0)
obj.value = 100
print(obj.value)
obj.show()