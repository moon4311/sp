def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

# 다음과 같이 간단히 쓸 수 있다.
def two_times2(x) : return x*2

result = list( map(two_times2, [1,2,3,4]))
print(result)

# lambda 를 사용하면 더 간략히 만들 수 있따.
result=list ( map( lambda a:a*2,[1,2,3,4] ) )

print(map(lambda a:a*2,[1,2,3,4]))
print(result)