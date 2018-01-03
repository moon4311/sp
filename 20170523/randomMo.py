import random

print(random.random())

print(random.randrange(1,7),'# 1 이상 7 미만')
print(random.randrange(1,7))
print(random.randrange(1,7))

abc = ['a','b','c','d','e']
random.shuffle(abc)
print(abc)
random.shuffle(abc)
print(abc)

print(random.choice(abc))
print(random.choice(abc))
print(random.choice(abc))
print(random.choice(abc))
print(random.choice(abc))
print(random.choice(abc))