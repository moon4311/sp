# for 변수 in 리스트(or 튜플 or 문자열) :

test_list = ['one','two','three']

for i in test_list:
    print(i)


a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
for b in a:
    print(b[0])

marks = [90, 25,  67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다." % number)

number = 0
for mark in marks:
    number = number + 1
    if mark < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." % number)


a = range(1,11)
print(a)
sum = 0
for i in a:
    sum +=i
print(sum)

for number in range(len(marks)):
    if marks[number] < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))


print("*** 9 X 9 ***")

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')
print(" * end=\" \" 다음줄로 넘기지 않기 위해 씀 ")


# 리스트 안에 for문 넣기
a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)
print(result)
#  -----> 이렇게 고칠수 있다.
result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
# [결과 for 변수 in 타겟 if 조건   ]  결포변인타이프조건
# [표현식 for 항목 in 반복가능객체 if 조건]

# [ 표현식 for 항목1 in 반복객체1 if 조건1
#          for 항목2 in 반복객체2 if 조건2
#          for 항목N in 반복객체N if 조건N  ]
#

result = [x*y for x in range(2,10)
              for y in range(1,10)]

print(result)