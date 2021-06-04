import datetime
import random
 

now=datetime.datetime.now()
season = ""
time = ""

kor_foods = ['불고기','돼지국밥',"닭발","냉면","콩국수","제육볶음"]
ch_foods = ['짜장면','짬뽕',"탕짜면"]
jp_foods = ['라멘','초밥',"텐동","가츠동","에비후라이동","오야꼬동","오꼬노미야키"]
eng_foods = ['햄버거','피자',"파스타","스테이크","필라프"]
snack_foods = ["떡볶이",'순대',"불닭볶음면"]

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



def get_choose(foodname) :
    ans_ok = input("{} 는 어떠세요? 메뉴가 마음에 들면 1을, 아니면 2를 입력해주세요.".format(foodname))
    if ans_ok == '1' :
        print("메뉴가 마음에 드셨다니 다행이네요. 맛있게 드시고, 기회가 된다면 다음에 또 만나요!")
        return False
    elif ans_ok == '2' :
        return True

print("안녕하세요. 『오늘 밥 뭐먹지?』 프로그램에 방문해주셔서 감사합니다. 현재 계절은 {}이고 {}이네요.".format(season,time))

number = input(""" 맛있는 메뉴를 추천해드리겠습니다. 드시려는 음식이 
한식이면 1을,
중식이면 2를,
일식이면 3을,
양식이면 4를,
분식이면 5를,
메뉴를 추천받고 싶으면 6을 입력해주세요.\n>""")
    
foods_num = int(number) - 1
able_pass = True
while able_pass :
    ans_ok = ''
    if number != '6' :
        random.shuffle(foods_data[foods_num])

    country_name = ""
    if number == '1' :
        country_name = "한"
    elif number == "2" :
        country_name = "중"
    elif number == "3" :
        country_name = "일"
    elif number == "4" :
        country_name = "양"
    elif number == "5" :
        country_name = "분"


    if not number == '6':
        print("{}식을 드시고 싶으시군요!".format(country_name))
        for i in range(len(foods_data[foods_num])) :
            able_pass = get_choose(foods_data[foods_num][i])
            if not able_pass :
                break
    elif number == '6' :
        print("메뉴를 추천받고 싶으시군요!")
        country = int(random.randrange(len(foods_data)))
        food = int(random.randrange(len(foods_data[country])))

        able_pass = get_choose(foods_data[country][food])
        if not able_pass :
            break
