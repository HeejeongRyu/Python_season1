def count_matching_numbers(numbers, winning_numbers):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    cnt = 0
    #cnt_b = 0
    #arr2 = winning_numbers[:6]
    #arr3 = winning_numbers[6]
    #arr4 = []
    #for i in numbers : 
    #    if i in arr2 : 
    #        cnt += 1
    #    if i == arr3 :
    #        cnt_b += 1
    #arr4.append(cnt)
    #arr4.append(cnt_b)
    #return arr4
    for num in numbers:
        if num in winning_numbers:
            cnt = cnt + 1

    return cnt


def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    #rslt = count_matching_numbers(numbers, winning_numbers)
    cnt = count_matching_numbers(numbers, winning_numbers[:6])
    b_cnt = count_matching_numbers(numbers, winning_numbers[6:])
    
    if cnt == 6:
        return 1000000000
    elif cnt == 5 and b_cnt == 1:
        return 50000000
    elif cnt == 5:
        return 1000000
    elif cnt == 4:
        return 50000
    elif cnt == 3:
        return 5000
    else:
        return 0
        
    #print(rslt)
    #if rslt[0] == 6 :
    #    return 1000000000
    #if rslt[0] == 5 and rslt[1] == 1:
    #    return 50000000
    #if rslt[0] == 5 and rslt[1] == 0:
    #    return 1000000
    #if rslt[0] == 4 :
    #    return 50000
    #if rslt[0] == 3 :
    #    return 5000
    
        


# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
