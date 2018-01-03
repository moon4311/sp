class HousePark:
    lastname="박"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self,place):
        print("%s, %s여행을가다" % (self.fullname, place))
    def love(self, other):
        print("%s, %s LOVE " % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼 " % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self,place, day):
        print("%s, %s여행 %d일 가네  " % (self.fullname, place, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet
pey.__add__(juliet)

