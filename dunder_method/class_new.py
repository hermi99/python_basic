#__new__ 는 메모리에 객체를 할당

# __init__보다 먼저 실행되며
# 클래스 자기 자신(cls)을 숨겨진 파라미터로 받으며
# 반드시 object를 return함


class MyClass:
    def __init__(self, n1, n2):
        print('init called')

    def __new__(cls, *args, **kwargs):
        print('new called')
        obj = super().__new__(cls)
        return obj

    def __call__(self, *args, **kwargs):
        print('call called')


cls = MyClass(1, 2)

