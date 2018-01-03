import threading,time

def say(msg):
    while True: # 3개의 쓰레드가 계속 돈다.-> 메인쓰레드가 끝나면 종료
        time.sleep(1)
        print(msg)

for msg in ['you 1','need 1','python 1']:
    t = threading.Thread(target=say,args=(msg,))
    t.daemon = True  # 데몬쓰레드로  메인이 죽을때 같이 죽는다.
    t.start()

for i in range(50):
    time.sleep(0.2)
    print(i)


##########    같은 결과
class MyThread(threading.Thread):
    def __init__(self,msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True

    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)
for msg in ['you 2','need 2', 'python 2']:
    t = MyThread(msg)
    t.start()

for i in range(50):
    time.sleep(0.1)
    print(i)