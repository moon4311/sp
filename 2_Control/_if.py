# 0 , "" , [] , () , {}  모두 거짓

money = 1
if money :
    print("택시")
else :
    print("도보")

# x or y  /  x and y   /  not x
_list = ["x","y"]
_tuple = ("x","y")
_str = "xyz"
if "x" in _list :     print(True)
if "z" not in _tuple :   pass  # 아무일도 하지 않게 설정
if "x" in _str :     print(True)

print("*** 반복문 중첩 ***")

if not _list :    pass
elif not _tuple :    pass
elif not _str :    pass
else :    print("else ")
