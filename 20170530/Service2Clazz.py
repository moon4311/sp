class Service:
    secret = "영구는 ..."
    def setname(self, name):
        self.name = name
    def sum(self,a,b):
        result = a + b
        print("%s님 %s + %s = %s입니다" % (self.name, a , b , result))

pey = Service()

pey.setname("홍길동")

print(pey.name)