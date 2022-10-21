# 백준 - 실버2 - 안녕 - dp, 완전 탐색, 배낭 문제
'''
dp, 완전 탐색, 배낭 문제

배낭 문제 푸는 방식으로 문제를 풀었다.
배낭 문제가 어떤건지 잘 모른다면 https://www.youtube.com/watch?v=A8nOpWRXQrs 여기 링크에서 배우면 좋을거 같다.
위의 링크에서 푸는 방식과 동일하게 문제를 풀었다.

- 재귀함수로 말고 반복문으로 문제를 풀 수 있다.
- 원래 이론상 모든 재귀는 반복문으로 표현이 가능하다.
- 당연히 모든 반복문을 재귀로 바꿀수도 있다.
'''
n = int(input())
hp = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

# 테스트
# n = 3
# hp = [0,1,21,79]
# happy = [0,20,30,25] # 50
# n = 1
# hp = [0,100]
# happy = [0,20] # 0
# n = 8
# hp = [0,100, 15, 1, 2, 3, 4, 6, 5]
# happy = [0,49, 40, 1, 2, 3, 4, 5, 4] # 59
# n = 4
# hp = [0,100,50,20,13]
# happy = [0,20,30,40,50] # 120
# n = 8
# hp = [0,100, 26, 13, 17, 24, 33, 100, 99]
# happy = [0,34, 56, 21, 1, 24, 34, 100, 99] # 135
# n = 12
# hp = [0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# happy = [0,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100] # 1200

def knapsack(n, MAX_HP, hp, happy):
    if n <= 0 or MAX_HP <= 0:
        return 0
    if hp[n] >= MAX_HP:
        return knapsack(n - 1, MAX_HP, hp, happy)
    else:
        left = knapsack(n - 1, MAX_HP, hp, happy)
        right = knapsack(n - 1, MAX_HP - hp[n], hp, happy)
        return max(left, happy[n] + right)

print(knapsack(n, 100, hp, happy))
