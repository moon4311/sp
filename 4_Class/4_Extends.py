class HousePark:
    lastname="박"
    def __init__(self,name):
        self.fullname = self.lastname + name
    #def setname(self,name):
    #    self.fullname = self.lastname + name
    def travel(self,place):
        print("%s, %s여행을가다" % (self.fullname, place))



class HouseKim(HousePark):  # Extends
    lastname = "김"

    def travel(self,place, day):       # Override
        print("%s, %s여행을 %d일 가네." % (self.fullname, place, day))


#pey = HousePark()
pey = HousePark("응용")

print(pey.lastname)

#pey.setname("응용")
print(pey.fullname)

pey.travel("부산")

key = HouseKim("이용")
print(key.fullname)
key.travel("순천",5)

