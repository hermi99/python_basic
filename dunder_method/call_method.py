# __new__ : 클래스 인스턴스를 생성(메모리 할당)
# __init__: 생성된 인스턴스 초기화
# __call__: 인스턴스 실행

class Calc1:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

calc = Calc1(1, 2)
ret = calc.add()
print(ret)

class Add:
    def __init__(self):
        self.count = 0

    def __call__(self, n1, n2):
        self.count += 1
        return n1 + n2

add = Add()
print(add(3, 4))
print(add.count)

print(add(5, 6))
print(add.count)
