def solution(n):
    for i in range(1, n+1):
        if n % i == 1:
            return i

print(solution(10)) # 3
print(solution(12)) # 11