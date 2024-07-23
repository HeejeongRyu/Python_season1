from random import randint


def generate_numbers(n):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    arr = []
    while len(arr) < n :
        a = randint(1,45)
        if a not in arr:
            arr.append(a)
    return arr


def draw_winning_numbers():
    # 여기에 코드를 작성하세요
    darr = generate_numbers(7)
    return sorted(darr[:6]) + darr[6:]
    #while True :
    #    a = randint(1,45)
    #    if a not in darr:
    #        darr.append(a)
    #        break
            
    #return darr


# 테스트 코드
print(draw_winning_numbers())
