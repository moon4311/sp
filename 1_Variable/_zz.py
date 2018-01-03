print("\n *** 변수 선언 *** ")
a,b=("python","life")
print(a,b)
(a,b)="python","life"
print(a,b)
[a,b]=["python","life"]
print(a,b)

print("\n *** 변수 교환 ***")
a,b=3,5
print(a,b)
a,b=b,a
print(a,b)

print("\n*** 변수 복사 ***")
a=[1,2,3]
b = a
print(" * b = a : ", a,b, " * 원본이 변하면 복사본도 변함" )
a[1] = 4
print(" a[1] = 4 : ",a,b)

a = [1,2,3]
b = a[:]
print(" * b = a[:] : ", a,b, " *  변경한 것만 바뀜")
a[1] = 4
print(" a[1] = 4 : ", a,b)

a=[1,2,3]
from copy import copy
b = copy(a)
print(" * b = copy(a) : ", a,b , " *  변경한 것만 바뀜")