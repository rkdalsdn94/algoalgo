# 백준 - 브론즈3 - 세 수 - 10817 - 단순 구현 문제
'''
단순 구현 문제

단순하게 정렬 후 가운데 값을 출력하면 된다.
'''

nums = sorted(list(map(int, input().split())))

# 테스트
# nums = [20,30,10] # 20
# nums = [30,30,10] # 30
# nums = [40,40,40] # 40
# nums = [20,10,10] # 10


print(nums[1])
