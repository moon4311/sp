# r - read 읽기만 할때
# w - write 내용을 쓸 때  * 기존파일이 있는 경우 덮어쓰기 됨
# a - add 파일 마지막에 새로운 내용 추가

f = open("D:\program\python\새파일.txt","w")
for i in range(1,11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)
f.close()

