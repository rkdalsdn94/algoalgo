# 백준 - 15720 - 카우버거 - 실버5 - 수학, 구현, 그리디, 정렬 문제
'''
수학, 구현, 그리디, 정렬 문제


zip함수와 list slicing 을 통해 답을 쉽게 풀었다.

풀이 과정
1. input값들을 잘 입력받고 list형식을 입력 받을 때 내림차순으로 정렬하는 것만 주의하면 된다. -> 최대 세트 할인을 만들기 위해 내림차순 정렬을 한다.
2. 할인을 안한 값은 전체 가격들의 합을 구하면 되므로 origin_num이라는 변수에 전체 값을 더하면 된다.
3. 내림차순 정렬한 리스트들을 zip함수를 이용해 세 리스트의 값을 하나씩 꺼내면서 10% 할인된 값을 구한다.
    3.1 zip함수는 인자에 있는 이러터블한 값들의 길이가 달라지면 반복을 멈추므로 몇 번째 인덱스까지의 값을 구했는지 확인하기 위한 temp_idx를 1씩 더한다.
4. 세트로 구하지 못한 값들이 있을수 있으므로 temp_idx 이후의 값들을 sum과 list slicing을 이용해 discount_num 변수에 더하고 출력한다.
'''

b, c, d = map(int, input().split())
b_list = sorted(list(map(int, input().split())), reverse=True)
c_list = sorted(list(map(int, input().split())), reverse=True)
d_list = sorted(list(map(int, input().split())), reverse=True)

# 테스트
# b, c, d = 3, 3, 2
# b_list = sorted([2000, 3000, 2500], reverse=True)
# c_list = sorted([800, 1300, 1000], reverse=True)
# d_list = sorted([500, 1000], reverse=True)

origin_num = sum(b_list) + sum(c_list) + sum(d_list)
discount_num = 0
temp_idx = 0

for i, j, z in zip(b_list, c_list, d_list):
    discount_num += int((i + j + z) * 0.9)
    temp_idx += 1

discount_num += sum(b_list[temp_idx:]) + sum(c_list[temp_idx:]) + sum(d_list[temp_idx:])

print(origin_num, discount_num, sep='\n')
