import pandas as pd

# 여기에 코드를 작성하세요
a_list = [
    ['Taylor Swift','December 13, 1989','Singer-songwriter'],
    ['Aaron Sorkin','June 9, 1961','Screenwriter'],
    ['Harry Potter','July 31, 1980','Wizard'],
    ['Ji-Sung Park','February 25, 1981','Footballer']
]
df = pd.DataFrame(a_list, columns = ['name','birthday','occupation'])
# 테스트 코드
df
