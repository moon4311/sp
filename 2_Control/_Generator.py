def generator_test(n):
    print("2 ------- Generator Start --------------")

    while(n < 3):
        print("3  << Before Yield >>")
        yield n
        print("7 After yield n : ",n)
        n += 1
        print("8 << Before Yield >>")

    print("--------Generator End -------------")


print("1 ----------Main Function Start -----------")

for i in generator_test(0):
    print("4 ----Start For ----")
    print ("5   Yield i is : ", i)
    print("6 ----End For ----")

print("----------Main Function End -----------")