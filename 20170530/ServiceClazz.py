class Service:
    secret = "영구는 ㅌㅌ."


pey = Service()

print(pey.secret)

Service.secret = "떙구는 ..ㅁㅁ"

print(pey.secret)
