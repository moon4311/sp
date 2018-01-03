try:
    pass
except :
    pass

try:
    pass
except IOError :
    pass

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

try:
    f=open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else :  # except 가 아닐 경우 실행 됨
    data = f.read()
    print(data)
    f.close()


f = open('foo.txt','w')
try:
    f.write("TESTTT")
finally:
    f.close()


class Bird:
    def fly(self):
        print("very fast")
        pass #raise NotImplementedError


class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

