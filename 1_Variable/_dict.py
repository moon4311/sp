# dict =  {}
# Java의 Map
# key : value 구조
# 중복 키를 사용하면 안된다

a_dict = {'server': 'db.diveintopython3.org',  'database': 'mysql'}

print(" map 기능 a_dict['server'] : ",  a_dict)
print("\n *** 항목 추가 (중복X) *** ")
a_dict['user'] = 'mark'
print(" a_dict['user'] : ",  a_dict)


print("\n *** 항목 읽기 *** ")

print("\nkey값 얻기\na_dict.keys() : ", a_dict.keys(), "\nlist(a_dict.keys()) : ", list(a_dict.keys()))
print("\nvalue값 얻기\na_dict.values() : ", a_dict.values(), "\nlist(a_dict.values()) :", list(a_dict.values()) )
print("\nitems 얻기\na_dict.items() : ", a_dict.items(), "\nlist(a_dict.items()) :", list(a_dict.items()) )
print("\nkey로 value 찾기1\na_dict.get('server'): ", a_dict.get("server")," * 값이 없으면 None 리턴")
print("\nkey로 value 찾기2\na_dict['server']: ", a_dict["server"], " * 값이 없으면 오류발생")
print("\n Key 있는지 조회\n'server' in a_dict : ", "server" in a_dict)


print("\n *** 항목 수정 *** ")
a_dict['database']='blog'
print(" a_dict['database'] : ",  a_dict)
a_dict.update()
print(" a_dict.update() : ",  a_dict)



print("\n *** 항목 삭제 *** ")
del a_dict["server"]
print(" del a_dict['server'] : ", a_dict)
a_dict.clear()
print(" a_dict.clear() : ", a_dict)
print("\n * none == null &&  none not in(false, 0) && none ⇔ not none")