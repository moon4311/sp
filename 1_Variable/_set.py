# sets 집합 자료형
# java의 Set
# 순서가 없다
# 중복된 값이 없다.
# 중복값 제거를 위해 다른 자료형을 Set 변경 후 다시 원래 자료형으로 재변경

a_set = {1}
print('a_set : ',  a_set,  type(a_set))

a_list = ['a',  'b',  'mpilgrim',  True,  False,  42]
a_set = set(a_list)
print(a_set)


a_set = set()  #  -> class 'set'
not_sure = {}  #  -> class 'dict'


# #### list = []   / tuple = ()   / set = {}
print("\n *** 항목 추가 (중복 X ) *** ")
a_set = {1, 2}
a_set.add(4)
print("\n 1개 추가\n a_set.add(4) : ", a_set)
a_set.add(1)
print("a_set.add(1) : ", a_set,  "* sets are bags of unique values")

a_set.update({2, 4, 6})
print("\n 여러개 추가\na_set.update({a, b}) : ",  a_set,  "* duplicate values are ignored")
a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
print("a_set.update({a, b}, {c, d}) : ",  a_set,  "* set possible update() method with any number of arguments")
a_set.update([10, 20, 30])
print("a_set.update([a, b, c]) : ",  a_set, "* list 객체를 더할수도 있다.")

print("\n *** 항목 삭제 *** ")

a_set.discard(10)
print("a_set.discard(10) : ",  a_set , " * 항목 없는 경우 넘어감 ")
a_set.remove(13)
print("a_set.remove(13) : ",  a_set, " * 항목이 없는 경우 에러 ")
print("a_set.pop() : ",  a_set.pop(),  " * the pop() method removes a single value from a set and returns the value.")
print("a_set.pop() : ",  a_set.pop(),  " * there is no “last” value in a set")
print("a_set.pop() : ",  a_set.pop(),  " * 앞에서부터 하나씩 추출")
a_set.clear()
print("a_set.clear() : ", a_set)



print("\n *** 항목 읽기 / 비교 *** ")
print("9 in a_set : ",  9 in a_set , " * 포함 여부")

b_set = {1,  2,  3,  5,  6,  8,  9,  12,  15,  17,  18,  21}
print("\n a∪b\n a_set | b-set : ", a_set | b_set )
print(" a_set.union(b_set) : ",  a_set.union(b_set),  " * a_set.union(b_set) == b_set.union(a_set)" )
print("\n a∩b\n a_set & b-set : ", a_set & b_set )
print(" a_set.intersection(b_set) : ",  a_set.intersection(b_set),  " * a_set.intersection(b_set) == b_set.intersection(a_set)")
print("\n a-b\n a_set - b-set : ", a_set - b_set )
print(" a_set.difference(b_set) : ",  a_set.difference(b_set),  " * a_set.difference(b_set) != b_set.difference(a_set)")
print("\n (a∩b)\na_set.symmetric_difference(b_set) ",  a_set.symmetric_difference(b_set), " * b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set)")

a_set={1, 2, 3}
b_set={1, 2, 3, 4}
print("# a⊆b : a_set.issubset(b_set) ", a_set.issubset(b_set), "* Is Sub Set" )
print("# b⊇a : b_set.issuperset(a_set) ", b_set.issuperset(a_set), " * Is Super Set")
