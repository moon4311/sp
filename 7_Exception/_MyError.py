class MyError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):   ## Exception 정보가 나오려면 __str__을 구현해야 한다.
        return self.msg

def say_nick(nick):
    if nick == '바보':
        raise MyError("허용되지 않는 별명입니다.")
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

