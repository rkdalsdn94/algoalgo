# 백준 - 브론즈1 - 당신은 운명을 믿나요? - 27930 - 그리드, 문자열 문제
'''
그리드, 문자열 문제

단순히 문자열을 그리디하게 부교하면 되는 문제이다.

풀이 과정
 1. 입력을 받는다.
 2. korea, yonsei를 각각 변수에 저장한다.
 3. k_temp, y_temp를 0으로 초기화한다.
 4. s를 반복하면서 korea와 yonsei의 각 문자열을 비교한다.
 5. 만약 korea의 k_temp번째 문자열과 같다면 k_temp를 1 증가시킨다.
 6. 만약 yonsei의 y_temp번째 문자열과 같다면 y_temp를 1 증가시킨다.
 7. 만약 k_temp가 5가 되면 korea를 출력하고 반복을 종료한다.
 8. 만약 y_temp가 6이 되면 yonsei를 출력하고 반복을 종료한다.
'''

s = input()

# 테스트
# s = 'KOYONSEREAI' # KOREA
# s = 'YYOONNSSEEII' # YONSEI

korea, yonsei = 'KOREA', 'YONSEI'
k_temp, y_temp = 0, 0

for i in s:
    if i == korea[k_temp]:
        k_temp += 1
    if i == yonsei[y_temp]:
        y_temp += 1

    if k_temp == 5:
        print(korea)
        break
    if y_temp == 6:
        print(yonsei)
        break
