def plus_one(x):
    return x+1
print(list (map (plus_one, [1,2,3,4,5,6]) ) )

result = list( map (lambda x : x+1 , [1,2,3,4,5,6]))
print("result : " , result)
