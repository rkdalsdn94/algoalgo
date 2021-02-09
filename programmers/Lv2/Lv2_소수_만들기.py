from itertools import combinations
def solution(nums):
    answer = 0

    nums = list(combinations(nums, 3))
    for i in nums:
        temp = True
        for j in range(2, sum(i)//2 + 1):
            if sum(i) % j == 0:
                temp = False
                break
        if temp:
            answer += 1
    
    return answer
print(solution([1,2,3,4])) # 1
print(solution([1,2,7,6,4])) # 4