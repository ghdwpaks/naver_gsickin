import datetime
import random
 

now=datetime.datetime.now()
season = ""
time = ""

kor_foods = ['불고기','돼지국밥']
ch_foods = ['짜장면','짬뽕']
jp_foods = ['라멘','초밥']
eng_foods = ['햄버거','피자']
snack_foods = ["떡볶이",'순대']

foods_data = [kor_foods,ch_foods,jp_foods,eng_foods,snack_foods]

if 3<=now.month<=5:
    season="봄"

if 6<=now.month<=8:
    season="여름"

if 9<=now.month<=11:
    season="가을"

if now.month<=2 or now.month==12:
    season="겨울"



if 0<=now.hour<6:
    time="새벽"
if 6<=now.hour<12:
    time="아침"
if 12<=now.hour<18:
    time="오후"
if 18<=now.hour<21:
    time="저녁"
if 21<=now.hour<=24:
    time="밤"

print("season :",season)
print("time :",time)

#print("number :",number)

i = 0


number = input(""" 맛있는 메뉴를 추천해드리겠습니다. 드시려는 음식이 

한식이면 1을,

중식이면 2를,

일식이면 3을,

양식이면 4를,

분식이면 5를,

메뉴를 추천받고 싶으면 6을 입력해주세요. >""")
    
foods_num = int(number) - 1
while True :
    ans_ok = ''
    random.shuffle(foods_data[foods_num])

    if number == 1:
        print("entered 1")
        #entered def
        input("한식을 드시고 싶으시군요!")
        #input("한식을 드시고 싶으시군요! {한식메뉴중 랜덤한개} 는 어떠세요? 메뉴가 마음에 들면 1을, 아니면 2를 입력해주세요.")
        for i in range(len(foods_data[foods_num])) :
            ans_ok = input("{} 는 어떠세요? 메뉴가 마음에 들면 1을, 아니면 2를 입력해주세요.".format(foods_data[foods_num][i]))
            if ans_ok == '1' :
                print("메뉴가 마음에 드셨다니 다행이네요. 맛있게 드시고, 기회가 된다면 다음에 또 만나요!")
                break
            elif ans_ok == '2' :
                continue


    if number == 2:
        print("entered 2")
        #input("중식을 드시고 싶으시군요! ~~~~~~~~한식이랑 흐름 똑같이 블라블라")


    if number == 3:
        print("entered 3")


    if number == 4:
        print("entered 4")
        

    if number == 5:
        print("entered 5")

    if ans_ok == '1' :
        break

    i += 1