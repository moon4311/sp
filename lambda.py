
def hap(x, y):
    return x + y

print(hap(10,20))


tt=(lambda x,y : x + y)(10,20)
print(tt)


tt=map(lambda x : x ** 2, range(5))
print(list(tt))


from functools import reduce

ss =[0,1,2,3,4]
sma = sum(ss)
tt = reduce(lambda x, y : x + y, ss)
ts = reduce(lambda x, y: y + x, 'abcde')  # -> 4) e +   3) d +  2)  c +  1) b + a
print(tt)
print(sma)
print(ts)


tt = list(filter(lambda x:x < 5 , range(10)))
print(tt)