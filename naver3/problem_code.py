import threading
import random




def tiiimer(n):
    
    print("n : ",n)
    print("now :",now)

    while n != now:
        n = n-1
        time.sleep(0.01)

        if n == now:
            print("시간이 다 되었습니다.")

            while True :
                a = random.randint(1,50)
                b = random.randint(1,50)

                print(f'{a} + {b} = :', end='')
                x = int(input())

                if x != a+b:
                    print('오답입니다. 다시!!')
                    print()
                    continue

                print(f'{a} - {b} = :', end='')
                x = int(input())

                if x != a-b:
                    print('오답입니다. 다시!!')
                    print()
                    continue

                print(f'{a} * {b} = :', end='')
                x = int(input())

                if x != a*b:
                    print('오답입니다. 다시!!')
                    print()
                    continue
                break

            listsay = ["일어나세요", "빨리 일어나세요", "good", "...", "화이팅!!!"]
            print(random.choice(listsay))
            
    

def ttttt():

    import tkinter
    
    chang = tkinter.Tk()

    chang.geometry("1000x500")
    chang.title("알람")
    chang.option_add("*Font", "맑은고딕 100")
    chang['bg'] = '#ff6f61'

    enter = tkinter.Entry(chang)
    print("3enter :",enter)
    enter.pack()
    print("1enter :",enter)

    btn = tkinter.Button(chang)
    btn.config(text='다음')
    btn.config(width = 5, height = 1)
    print("2enter :",enter)
    btn.config(command = put)

    btn.place(x=300, y=200)

    chang.mainloop()

def put():
    a = enter.get()
    print(a)

def chang_thread():

    thread=threading.Thread(target=ttttt)

    thread.daemon=True

    thread.start()

import time
from datetime import datetime
now = int(time.time())

chang_thread()

while True:

    print("당신이 일어나고 싶은 년도를 입력하세요.")
    a = int(input())

    print("당신이 일어나고 싶은 월을 입력하세요.")
    b = int(input())

    print("당신이 일어나고 싶은 일을 입력하세요.")
    c = int(input())

    print("당신이 일어나고 싶은 시간을 입력하세요. (예를 들어, 오후 3시일 경우, 15시로..)")
    d = int(input())

    print("당신이 일어나고 싶은 분을 입력하세요.")
    e = int(input())

    print("당신이 일어나고 싶은 초를 입력하세요.")
    f = int(input())

    ddd = "%d-%d-%d %d:%d:%d"%(a,b,c,d,e,f)
    timestamp = int(time.mktime(datetime.strptime(ddd, '%Y-%m-%d %H:%M:%S').timetuple()))
    print("in timestamp :",timestamp)
    if now >= timestamp:
        print("제대로 된 날짜와 시간을 입력하세요.")
        continue

    else:
        break
print("out timestamp :",timestamp)
tiiimer(timestamp)

    
        
