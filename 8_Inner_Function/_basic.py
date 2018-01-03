# abs - 절대값
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all(x) 반복 가능한 자료형x를 입력 인수로 받아 모두 참일 때 True
all([1,2,3])  # True
all([1,2,3,0])  # False

#any(x) x중 하나라도 참이 있을 경우 True
any([1,2,3]) # true
any([0,""])  # False

#chr(i) 아스키 코드값을 해당 문자로 출력
chr(97) # 'a'
chr(48) # '0'

#dir(x) x가 자체적으로 가지고 있는 변수나 함수를 보여준다
dir([1, 2, 3]) #['append', 'count', 'extend', 'index', 'insert', 'pop',...]
dir({'1':'a'}) #['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]

#divmod(a,b)  a/b 몫과 나머지 리턴
divmod(7,3) # (2,1)

#enumerate  (열거하다) # for문과 함꼐 쓰임 /  자료형의 index 파악 가능
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

#eval
eval('1+2') # 3
eval("'hi'+'a'") # hia
eval("divmod(4,3)") #(1,1)

#hex(x)  16진수로 변환
hex(234) # 0xea'
hex(3) #'0x3

#id(object) 주소값 리턴
a= 3
print( id(3) )
print( id(a) )
b = a
print( id(b) )

#input
# a = input()
# print(a)
# b=input("Enter : ")
# print(b)

#int 10진수 정수 반환
int('3') # 3
int(3.4) # 3
int('11',2)  # 2진수 11 =>  3
int('1A',16) # 16진수 1ㅁ => 26


#isinstance(object,class) 해당 클래스의 인스턴스인지 확인

#lambda
sum = lambda a,b : a+b
print(sum(3,4))

myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList)
print(myList[0](3,4),myList[1](3,4))

# map  -> two_times.py / map_test.py

# max  최대값 리턴
max([1,2,3]) # 3
max("python")  # y
 # 가 > z > ^ > Z > @ > 9~0 > * ) > ( > & > % > $ > #  > !

# min  최소값 리턴
min([1,2,3]) # 1
min("python") # h

#oct(x)  정수 -> 8진수
oct(34) #'0o42'
oct(12345) # 0o30071

#open(fileName, [mode])  mode : w,r,a,b  b-> 바이너리 모드로 파일 열기
# [mode] 생략 시 기본값은 r
f= open("D:/program/python/newss.txt",'rb')
data=f.read()
print(data)
f.close()
f= open("D:/program/python/newss.txt",'r')
data=f.read()
print(data)
f.close()

# ord(c) 문자의 값을 리턴 <-> chr(c)
print( ord('!')) #33
print( ord('9')) #57
print( ord('Z')) #90
print( ord('z')) #122
print( ord('가')) #44032

#pow(x,y) x의 y제곱
pow(2,4) # 16
pow(3,3) # 27

#range([start,],stop [,step])

print( list(range(5)) )  # 0~ 5 앞까지
print( list(range(5, 10)) )  # 5~ 10 앞까지
print( list(range(5,-20,-3)) )  # 5 ~ 20 앞까지 3칸씩 건너뛰어서

print( sorted([3,1,2]) )
print( sorted(['a','c','b']) )
print( sorted("zero"))

#str  문자열 형태로 객체 변환
print( str(3) )
print( str('hi') )
print( str('hi'.upper()) )
print( str(["s","h","a","a","p"]) )

#tuple 튜플 형태로 리턴

#type 입력값의 자료형 리턴

