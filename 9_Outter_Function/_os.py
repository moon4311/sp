import os, shutil,glob,tempfile

os.environ # 환경변수 조회
os.environ['path'] # 환경변수 path  조회


print( os.getcwd() ) # 디렉토리 위치 리턴
os.chdir("D:/program/python/9_Outter_Function") # 디렉토리 위치 변경
print("#### 폴더/파일의  생성/수정/삭제  ")
#os.mkdir("test1")  # 디렉토리 생성
#os.rmdir("test1")  # 디렉토리 삭제 ( 비어있어야 삭제 가능 )
#os.unlink("test1_copy.txt") # 파일삭제
#os.rename("test1.txt","test.txt")  # before파일을 after파일로 이름 변경


shutil.copy("test.txt","test_copy.txt")


os.system("dir")  # 시스템 명령어 dir 실행

f = os.popen("dir") # 실행한 시스템 명령어 결과값 리턴받기
print(f.read())


result=glob.glob("D:/program/python/*") # 폴더 + 파일 스캔해서 리스트 반환  * , ? 사용 가능
print(result)

filename = tempfile.mktemp()
print(filename)
f = tempfile.TemporaryFile()
f.close()

