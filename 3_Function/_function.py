def sum(a,b):
    return a + b


a = 3
b = 4
c = sum(a,b)
print(c)


# 입력값이 몇개가 될지 모를때
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_many(1,2,3,4,5,6,7,8,76,5,4,56))


def sum_mul(choice, *args):
    if choice == "sum" :
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul" :
        result = 1
        for i in args:
            result = result * i
    return result


result = sum_mul("sum" , 1,2,3,4,5)
print(result)
result = sum_mul("mul" , 1,2,3,4,5)
print(result)

print(" 함수 초기값 설정")
# 함수 초기값 설정
# 주의 :   초기화된 값은 마지막에 와야 한다.

def say_myself(name, old, man=True) :
    print(" 나의 이름은 %s 입니다." % name)
    print(" 나이는 %d살입니다." %old)
    if man:
        print("남자")
    else :
        print("여자")

say_myself("김재문",28)
say_myself("김재문",28,0)


a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

# 함수 안에서 함수 밖의 변수 변경 하는 방법
def vartest1(a):
    a = a + 1
    return a

def vartest2():
    global  a  # global 을 붙여야 함수 밖의 변수 제어 가능
    a = a + 1