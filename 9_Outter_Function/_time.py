import time

_time = time.time()  # 초단위 반환
print( _time )

_localtime = time.localtime( _time )  #연 월 일 시 분 초
print( _localtime )

_asctime = time.asctime( _localtime ) # 날짜와 시간을 알아보기 쉬운 상태로 변환
print( _asctime )

_ctime = time.ctime()  # 현재 시간 리턴
print( _ctime )

_strftime = time.strftime('%x %X', _localtime )  # 포맷 변경
print( "_strftime : ", _strftime )
_strftime = time.strftime('%U %W', _localtime )  # 포맷 변경
print( "_strftime : ", _strftime )

