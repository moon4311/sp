class Service:
     secret = "영구는 배꼽이 두 개다"
     def __init__(self, name):  # 객체를 만들 때 항상 실행된다
         self.name = name
     def sum(self, a, b):
         result = a + b
         print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))


# 이전 방식
#pey = Service()
#pey.name="홍길동"
#pey.sum(1,1)

print("Class 안에 새로운 변수 생성이 가능하다 -> 클래스 안에 없는 변수도 사용 가능")
# __init__ 방식
babo = Service("홍길동")
babo.sum(1,1)
