def is_palindrome(word):
    # 여기에 코드를 작성하세요
    a = ''
    len_w = len(word)
    for i in range(len_w-1, -1, -1) :
        a += word[i]
    if a == word : 
        return True
    else : 
        return False
    

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
