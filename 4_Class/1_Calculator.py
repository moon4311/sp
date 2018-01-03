class Calcalator:
    def __init__(self):
        self.result = 0
    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calcalator()
cal2 = Calcalator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


def sum(self, a, b) :
    result = a + b
    print("%s + %s = %s입니다." %(a, b, result))

