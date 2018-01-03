import math

print(math.pi)

print(math.sin(math.pi/2))


a_list = ['a',  'b',  'mpilgrim',  'z',  'example']

print("list : ",  a_list)

## list[-a]  뒤에서부터 a번째
print("list[-1] ",  a_list[-1])
print("list[-3] ",  a_list[-3])
print("list[0] list[-5] : ",  a_list[0],  a_list[-5])

# slicing a list
#   list[start:end] start 포함,  end 미포함
'''print("a_list[1:3]",  a_list[1:3])
print("a_list[1:-1]",  a_list[1:-1])
print("a_list[0:3]",  a_list[0:3])
print("a_list[:3]",  a_list[:3])
print("a_list[3:]",  a_list[3:])
print("a_list[:]",  a_list[:])
'''

## adding items to a list
a_list = a_list + ["3", 6]
print("a_list + [] :: ",  a_list)

#a_list.append(true) # 항목 한개 더할때
print("append(true) :: ",  a_list)
a_list.extend(['four', 'aaa']) # 리스트끼리 합칠 떄
print("extend(['four', 'aaa']) :: ",  a_list)
a_list.insert(0, 'new') # 원하는 위치에 항목 하나 넣을떄
print("insert(0, 'new') :: ",  a_list)

## searching for values in a list
print('a_list.count(a) : ',  a_list.count('a'))
print('a in a_list : ',  'a' in a_list)
print('a_list.index(a) : ',  a_list.index('a'))

## delete value in a list
print(a_list)
del a_list[1]
print("del a_list[1] :: ",  a_list)

a_list.remove('b')
print('a_list.remove(b) : ', a_list)

## removing items from a list : bonus round
print('a_list.pop() : ',  a_list.pop(),  "# 공백일 경우 맨 뒤")
print('a_list.pop(0) : ',  a_list.pop(0), "# 해당 순서 ")


# tuple are faster than lists
# tuple can't modified
a_tuple = ("a",  "b",  "mpilgrim",  "z",  "example")

# list(a_tuple)    / tuple(a_list)   형변환 방법
newlist = list(a_tuple)
newlist.append("a")
print("newlist : ",  newlist)
newlist=tuple(newlist)
print("newlist : ",  newlist)

(monday,  tuesday,  wednesday,  thursday,  friday,  saturday,  sunday) = range(7)
#  0       1        2           3        4       5         6
# range(a)  0부터 a-1까지   / range(a, b)  a부터 b-1까지
print(monday)

# sets

a_set = {1}
print('a_set : ',  a_set,  type(a_set))

# a_list = ['a',  'b',  'mpilgrim',  true,  false,  42]
a_set = set(a_list)
print(a_set)


a_set = set()  #  -> class 'set'
not_sure = {}  #  -> class 'dict'


# #### list = []   / tuple = ()   / set = {}
a_set = {1, 2}
a_set.add(4)
print("a_set.add(4) : ", a_set)
a_set.add(1)
print("a_set.add(1) : ", a_set,  "# sets are bags of unique values")

a_set.update({2, 4, 6})
print("a_set.update({a, b}) : ",  a_set,  "# duplicate values are ignored")
a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
print("a_set.update({a, b}, {c, d}) : ",  a_set,  "# set possible update() method with any number of arguments")
a_set.update([10, 20, 30])
print("a_set.update([a, b, c]) : ",  a_set)

a_set.discard(10)
print("a_set.discard(10) : ",  a_set)
a_set.remove(13)
print("a_set.remove(13) : ",  a_set)

print("a_set.pop() : ",  a_set.pop(),  "# the pop() method removes a single value from a set and returns the value.")
print("a_set.pop() : ",  a_set.pop(),  "# there is no “last” value in a set")
print("a_set.pop() : ",  a_set.pop())
# a_set.clear()
# print("a_set.clear() : ",  a_set)

print("9 in a_set : ",  9 in a_set)

b_set = {1,  2,  3,  5,  6,  8,  9,  12,  15,  17,  18,  21}
print("# a∪b a_set.union(b_set) : ",  a_set.union(b_set),  "a_set.union(b_set) == b_set.union(a_set)" )
print("# a∩b a_set.intersection(b_set) : ",  a_set.intersection(b_set),  "a_set.intersection(b_set) == b_set.intersection(a_set)")
print("# a-b a_set.difference(b_set) : ",  a_set.difference(b_set),  "a_set.difference(b_set) != b_set.difference(a_set)")
print("# (a∩b)'a_set.symmetric_difference(b_set) ",  a_set.symmetric_difference(b_set), "b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set)")

a_set={1, 2, 3}
b_set={1, 2, 3, 4}
print("# a⊆b : a_set.issubset(b_set) ", a_set.issubset(b_set))
print("# b⊇a : b_set.issuperset(a_set) ", b_set.issuperset(a_set))


a_dict = {'server': 'db.diveintopython3.org',  'database': 'mysql'}

print("# map 기능 a_dict['server'] : ",  a_dict['server'])

a_dict['database']='blog'
print("#modify  a_dict['database'] : ",  a_dict['database'])
a_dict['user'] = 'mark'
print("#add  a_dict['user'] : ",  a_dict['user'])


print("# none == null &&  none not in(false, 0'') && none ⇔ not none")
