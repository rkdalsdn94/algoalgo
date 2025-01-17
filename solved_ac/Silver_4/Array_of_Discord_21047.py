# 백준 - 실버4 - Array of Discord - 21047 - 완전 탐색, 해 구성하기 문제
'''
완전 탐색, 해 구성하기 문제

핵심 아이디어
    - 모든 숫자가 같은 경우, 첫 번째 숫자의 마지막 자리를 증가시켜 정렬을 깨뜨린다.
    - 각 숫자의 각 자릿수를 변경해보며 정렬이 깨지는지 확인한다.
    - 정렬이 깨지는 경우를 찾으면 해당 숫자를 출력한다.

풀이 과정
    1. N을 입력받는다.
    2. N개의 숫자를 입력받는다.
    3. 모든 숫자가 같은 경우, 첫 번째 숫자의 마지막 자리를 증가시켜 정렬을 깨뜨린다.
    4. 각 숫자의 각 자릿수를 변경해보며 정렬이 깨지는지 확인한다.
    5. 정렬이 깨지는 경우를 찾으면 해당 숫자를 출력한다.
'''

def can_unsort(n, numbers):
    # 모든 숫자가 같은 경우 처리
    if all(x == numbers[0] for x in numbers):
        # 첫 번째 숫자의 마지막 자리를 증가시켜 정렬을 깨뜨림
        num_str = str(numbers[0])
        if num_str[-1] != '9':
            numbers[0] = int(num_str[:-1] + str(int(num_str[-1]) + 1))
            return numbers

    # 각 숫자의 각 자릿수를 변경해보며 정렬이 깨지는지 확인
    for i in range(n):
        num_str = str(numbers[i])
        for digit_pos in range(len(num_str)):
            original_digit = num_str[digit_pos]

            # 각 자릿수를 0-9로 변경해봄
            for new_digit in range(10):
                if str(new_digit) == original_digit:
                    continue

                # 첫 자리가 0이 되는 경우는 제외
                if digit_pos == 0 and new_digit == 0 and len(num_str) > 1:
                    continue

                # 새로운 숫자 생성
                new_num_str = num_str[:digit_pos] + str(new_digit) + num_str[digit_pos + 1:]
                new_num = int(new_num_str)

                # 임시로 숫자를 변경하여 정렬이 깨지는지 확인
                temp_numbers = numbers.copy()
                temp_numbers[i] = new_num

                # 정렬이 깨졌는지 확인
                if any(temp_numbers[j] > temp_numbers[j + 1] for j in range(n - 1)):
                    return temp_numbers

    return "impossible"

n = int(input())
numbers = list(map(int, input().split()))

# 테스트
# n = 4
# numbers = [2020, 2020, 2020] # 2021 2020 2020
# n = 2
# numbers = [1, 9999999] # impossible
# n = 4
# numbers = [1, 42, 4711, 9876]
'''
    1 42 4711 1876
    예제에서는 마지막 값이 3876인데, 내 코드는 1876이 나옴
    문제 출력 조건 - 유효한 솔루션이 여러 개 있는 경우 아무 솔루션이나 허용됩니다.
'''

result = can_unsort(n, numbers)
if isinstance(result, list):
    print(*result)
else:
    print(result)
