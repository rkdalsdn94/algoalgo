def solution(n):
    ans = 0
    
    while n>0:
        if n % 2 == 0:
            n = n // 2
        else:
            ans += 1
            n -= 1
    
    return ans
print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5