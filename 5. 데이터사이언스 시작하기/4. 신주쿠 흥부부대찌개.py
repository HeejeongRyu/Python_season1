import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 여기에 코드를 작성하세요
#won_array = [int(yen * 10.08) for yen in revenue_in_yen]
revenue_in_yen_np = np.array(revenue_in_yen)
won_array = revenue_in_yen_np * 10.08

# 테스트 코드
won_array
