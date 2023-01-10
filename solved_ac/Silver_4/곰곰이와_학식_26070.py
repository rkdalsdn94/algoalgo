# 백준 - 실버4 - 곰곰이와 학식 - 26070 - 구현, 그리디, 시뮬레이션 문제
'''
구현, 그리디, 시뮬레이션 문제

생각보다 까다로운 문제였다. 식권 리스트에서 다음 칸을 비교하면서 현재 값보다 다음 값이 더 크다면 temp를 1씩 증가시킨다.
위에서 만든 temp에 3을 더한 만큼 반복하면서 현재 반복중인 숫자 i를 3의 나머지로 구하면 인덱스 값을 구할 수 있으므로,
음식의 인덱스와 식권의 인덱스의 값들을 비교하면서 음식과 식권의 숫자를 빼고, res를 더해가며 답을 구하면 된다.
'''

food_list = list(map(int, input().split()))
coupon_list = list(map(int, input().split()))

# 테스트
# food_list = [10, 30, 20]
# coupon_list = [6, 100, 1] # 57

res = 0
temp = 0

for i in range(2):
    if coupon_list[i] <= coupon_list[i + 1]:
        temp = i + 1

for i in range(temp, temp + 3):
    i %= 3
    
    if food_list[i] >= coupon_list[i]:
        res += coupon_list[i]
        food_list[i] -= coupon_list[i]
    else:
        res += food_list[i]
        coupon_list[i] -= food_list[i]
        coupon_list[(i + 1) % 3] += coupon_list[i] // 3

print(res)
