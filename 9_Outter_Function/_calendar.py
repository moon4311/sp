import calendar
cal = calendar

_calend=cal.calendar(2018) ## 출력 X 데이터반환 O

f= open("_calendar.txt","w")
f.write(_calend)
f.close()

f = open("_calendar.txt","r")
print(f.read())
f.close()

# cal.prcal(2018)  ## 출력 O 데이터 반환 X

_week = cal.weekday(2017,7,11)
print(_week)

_monthrange = cal.monthrange(2017,7) # ( 1일의 요일 , 월 말일)
print(_monthrange)

