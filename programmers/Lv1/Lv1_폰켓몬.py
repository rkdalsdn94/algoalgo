def solution(nums):
    return min(len(nums)//2, len(set(nums)))


    # poket_num = len(nums) // 2
    # if poket_num < len(set(nums)):
    #     return poket_num
    # else:
    #     return len(set(nums))
print(solution([3, 1, 2, 3]))  # 2
print(solution([3, 3, 3, 2, 2, 4]))  # 3
print(solution([3, 3, 3, 2, 2, 2]))  # 2
