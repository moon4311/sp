# list = []
# 같은항목 중복 가능

print("\n *** list 생성 *** ")
a_list = ["dog","cat","bear"]
print("a_list : ", a_list)


# 항목추가, 변경, 삭제 가능
print("\n *** 항목 추가 (중복가능) *** ")
a_list += ["tiger"]
print("a_list += ['tiger'] : " , a_list)
a_list.append("bird1")
print("a_list.append('bird1') : ", a_list , " * 맨뒤로 ")
a_list.extend(['mouse2','hamster2'])
print("a_list.extend(['mouse2','hamster2']) : ", a_list, " * 맨뒤로 ")
a_list.insert(1,"bird3")
print("a_list.insert(1,'bird3'): ", a_list, " * 원하는 위치" )



print("\n *** 항목 읽기 *** ")
print("a_list[1], a_list[-2] : ", a_list[1]," , " , a_list[-2], " * 마이너스는 뒤에서 순서")
print("'bird1' in a_list : " , 'bird1' in a_list , " * 존재 여부")
print("a_list.count('bird1') : ", a_list.count('bird1'), " * 갯수 파악" )
print("a_list.index('bird1') : ", a_list.index('bird1'), " * 위치 파악" )
print("len(a_list) : ", len(a_list) , " * list 길이")
print("a_list[:] == a_list : [True] ", a_list[:] , " * 전체선택")
print("a_list[1:3] : ",  a_list[1:3] , " * start 포함 , end 미포함 ")
print("a_list[1:-1] : ",  a_list[1:-1] , " * 뒤로도 가능")
print("a_list[0:3] == a_list[:3] : [True] ", a_list[:3] , "* 0 생략가능")
print("a_list[3:] : ",  a_list[3:] , " * ~ 끝까지")


print("\n *** 항목 변경 *** ")
a_list.sort()
print("a_list.sort() : ",a_list , " * 순서 정렬")
a_list.sort(reverse=1)
print("a_list.sort(reverse=1) : ",a_list , " * 0이 아니면 역정렬")
a_list.reverse()
print("a_list.reverse() : ",a_list , "* 순서 뒤집기")



print("\n *** 항목 삭제 *** ")
del a_list[4]
print("del a_list[4] : " , a_list, "* 원하는 위치 삭제한 뒤 남은 것 출력")
a_list.remove("cat")
print("a_list.remove('cat') : ",a_list, " * 원하는 객체 첫번째 항목만 삭제")
a_list.pop(-1)
print("a_list.pop(-1) : ", a_list.pop(-1) , "* 원하는 위치 뽑아서 출력 (공백일 경우 마지막 항목) ")