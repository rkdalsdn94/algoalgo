# 백준 - 브론즈2 - ZOAC2 - 18238 - 구현, 문자열, 그리디 문제
'''
구현, 문자열, 그리디 문제

풀이 과정
1. 초기값을 'A'로 시작하는 temp 변수를 만든다.
2. 입력으로 들어온 글자가 왼쪽으로 돌렸을 때와 오른쪽으로 돌렸을 때 어디 쪽이 더 가까운지 값을 구한다.
    2.1 아스키 코드 값으로 비교 하는데 temp에 값을 담으면서 비교하면 된다.
    2.2 왼쪽 값은 입력으로 들어온 글자를 temp로 빼면된다.
    2.3 오른쪽 값은 temp값에서 입력으로 들어온 글자의 아스키 값을 빼면 된다.
3. min() 함수로 두 값중 더 작은 값을 res에 더한다.
4. 입력으로 들어온 글자를 모두 계산한 후에 res를 출력하면 된다.
'''

word = input()

# 테스트
# word = 'ZOAC' # 26
# word = 'LBOLVUEEPMOIENMG' # 100

res = 0
temp = 'A'

for i in word:
    turn_left = ord(i) - ord(temp)
    turn_right = ord(temp) - ord(i)

    if turn_left < 0:
        turn_left += 26
    if turn_right < 0:
        turn_right += 26
    
    res += min(turn_left, turn_right)
    temp = i

print(res)
