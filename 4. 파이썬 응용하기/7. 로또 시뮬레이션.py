from random import randint


def generate_numbers(n):
    # 여기에 코드를 작성하세요
    arr = []
    for i in range(n):
        a = randint(1,45)
        if a not in arr:
            arr.append(a)
    return arr


# 테스트 코드
print(generate_numbers(6))
