'''
단순 구현

9번 자연수 입력받고, 최댓값 출력 후 최댓값이 몇 번째에 나오는지 출력하기
'''

arr = [ int(input()) for _ in range(9) ]

# 테스트
# arr = [3, 29, 38, 12, 57, 74, 40, 85, 61] # 85 \n 8

print(max(arr))
print(arr.index(max(arr)) + 1)
