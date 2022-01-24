class MyMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('metaclass__new__')
        return super().__new__(cls, *args, **kwargs)


    def __init__(cls, *args, **kwargs):
        print('metaclass__init__')
        return super().__init__(*args, **kwargs)


    def __call__(cls, *args, **kwargs):
        print('metaclass__call__')
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMetaClass):
    def __init__(self):
        print('child__init__')

    def __call__(self):
        print('child__call__')


print('-------------------')
obj = MyClass()