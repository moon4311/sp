#  readline
print("\nreadline()")
f = open("D:\program\python\새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#  readlines
print("\nreadlines()")
f = open("D:\program\python\새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#  read
print("\nread()")
f = open("D:\program\python\새파일.txt",'r')
data = f.read()
print(data)
f.close()