import random
def random_pop(data):
    # number = random.randint(0 , len(data)-1 )
    number = random.choice(data)
    # return data.pop(number)
    data.remove(number)
    return  number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    random.shuffle(data)  # data 섞기 (셔플)
    while data : print(random_pop(data))

