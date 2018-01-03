# tuple =  ()
# faster than lists
# tuple can't modified

print("\n *** tuple 생성 *** ")
a_tuple = ("a",  "b",  "mpilgrim",  "z",  "example")
print("a_tuple : ", a_tuple )
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print("t1 :", t1," * 빈 튜플")
print("t2 : ", t2, " * 요소 하나만 가질 때 ,를 넣어야 한다")
print("t3 : ", t3, " * 일반적")
print("t4 : ", t4, " * 괄호 생략 가능")


print("a_tuple.count('z') : ", a_tuple.count("z"), " * 갯수 카운트" )
print("a_tuple.index('z') : ", a_tuple.index("z"), " * 위치 확인")

print("a_tuple[3] : ", a_tuple[3], "* 위치의 항목 확인")
print("a_tuple[1:] : ", a_tuple[1:], "* list 처럼 슬라이싱")

b_tu= (3 , 4)
print("a_tuple + b_tu :", a_tuple + b_tu , "* 튜블 간 더하기")
print("a_tuple * 3 : ", a_tuple * 3 , "* 곱한 수 만큼 반복" )


# list(a_tuple)    / tuple(a_list)   형변환 방법
newlist = list(a_tuple)
newlist.append("a")
print("newlist : ",  newlist)
newlist = tuple(newlist)
print("newlist : ",  newlist)



(monday,  tuesday,  wednesday,  thursday,  friday,  saturday,  sunday) = range(7)
#  0         1          2           3         4         5         6
# range(a)  0부터 a-1까지   / range(a, b)  a부터 b-1까지
print(monday)