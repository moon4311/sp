# 3의배수 또는 5의배수
data = 0
for i in range(1000):
    if i%3 == 0 or i%5 == 0 :     data += i

print(data)