class MyClass1:
    bar = True

my_class1 = MyClass1()

MyClass2 = type('MyClass2', (), {'bar': True})
my_class2 = MyClass2()

print(type(my_class1), my_class1.bar)
print(type(my_class2), my_class2.bar)

def echo(self):
    print('hello ', self.bar)

MyChildClass = type('MyChildClass', (MyClass2,), {'echo': echo})
my_childclass = MyChildClass()
print(type(my_childclass), my_childclass.bar)
my_childclass.echo()


class MakeCalc(type):
    def __new__(metacls, name, bases, namespace):
        namespace['desc'] = 'calc description'
        namespace['add'] = lambda self, a, b: a + b
        return type.__new__(metacls, name, bases, namespace)

    def __call__(self, *args, **kwargs):
        print('MakeCalc __call__')
        return type.__call__(self, *args, **kwargs)

Calc = MakeCalc('Calc', (), {})
calc = Calc()
print(calc.desc)
print(calc.add(5, 7))
