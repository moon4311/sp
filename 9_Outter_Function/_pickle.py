import pickle
########  바이너리 파일 (파일을 열어도 내용을 알아 볼 수 없다)
f = open("test.txt","wb")
data = {1:'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open("test.txt","rb")
data = pickle.load(f)
print(data)
f.close()
########   텍스트파일 (아스키코드를 이용한 파일 , 내용을 보고 읽을 수 있다)
f = open("test2.txt","w")
f.write("{1:'python', 2: 'you need'}")
f.close()

f = open("test2.txt","r")
print(f.read())
f.close()