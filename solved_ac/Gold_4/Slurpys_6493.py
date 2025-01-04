# 백준 - 골드4 - Slurpys - 6493 - 문자열, 재귀, 정규 표현식 문제
'''
문자열, 재귀, 정규 표현식 문제

다른 사람의 풀이를 보면 정규 표현식으로도 풀 수 있는데.. 정규 표현식을 잘 몰라서 사용하지 않고 풀었다.

[문제 설명]
Slurpy는 Slimp와 Slump의 조합으로 이루어진 특별한 문자열 패턴입니다.
이 문제는 주어진 문자열이 Slurpy 패턴을 만족하는지 확인하는 것이 목표입니다.

[핵심 개념]
1. Slump 패턴의 규칙:
   - D나 E로 시작
   - F가 한 개 이상 연속으로 나타남
   - G로 끝나거나, 다른 Slump가 나온 후 G로 끝남
   예시: DFG, EFG, DFFFFFG, DFDFDFDFG
2. Slimp 패턴의 규칙:
   - A로 시작
   - 두 글자인 경우: AH
   - 그 외의 경우:
     a) AB로 시작하고 C로 끝나는 Slimp
     b) A로 시작하고 C로 끝나는 Slump
   예시: AH, ABAHC, ABABAHCC, ADFGC
3. Slurpy 패턴:
   - Slimp 다음에 Slump가 오는 형태
   예시: AHDFG, ADFGCDFFFFFG

[구현 방법]
1. 재귀적 패턴 확인:
   - 각 함수는 문자열의 시작 위치(start)와 길이(length)를 매개변수로 받음
   - 부분 문자열을 검사할 때 인덱스 범위를 주의깊게 확인
2. 문자열 처리 최적화:
   - 불필요한 문자열 복사를 피하기 위해 인덱스 기반으로 접근
   - start와 length 매개변수를 사용하여 부분 문자열을 지정

[시간 복잡도]
- O(N^2): N은 문자열의 길이
- 각 위치에서 가능한 모든 분할을 시도하기 때문

[예제 입력]
    2
    AHDFG
    DFGAH
[예제 출력]
    YES
    NO
'''

def is_slump(s: str, start: int, length: int) -> bool:
    """Slump 패턴을 확인하는 함수

    규칙:
    1. D나 E로 시작
    2. F가 하나 이상 연속으로 나타남
    3. G로 끝나거나 다른 Slump가 나온 후 G로 끝남
    """
    if (length < 1):
        return False

    # D나 E로 시작하고, F가 바로 다음에 오며, G로 끝나야 함
    if (s[start] in ['D', 'E'] and
            start + 1 < len(s) and s[start + 1] == 'F' and
            start + length - 1 < len(s) and s[start + length - 1] == 'G'):

        # F의 연속을 확인하고, F가 아닌 문자를 만나면 그 부분이 새로운 Slump인지 검사
        for i in range(1, length - 1):
            if s[start + i] != 'F':
                return is_slump(s, start + i, length - i)
        return True

    return False

def is_slimp(s: str, start: int, length: int) -> bool:
    """Slimp 패턴을 확인하는 함수

    규칙:
    1. A로 시작
    2. 두 글자면 AH
    3. 그 외에는:
       - AB[Slimp]C 형태
       - A[Slump]C 형태
    """
    if length < 1:
        return False

    if s[start] == 'A':  # A로 시작하는지 확인
        if length == 2 and s[start + 1] == 'H':  # AH 케이스
            return True
        elif length >= 3:  # 3글자 이상인 케이스
            if s[start + 1] == 'B':  # AB[Slimp]C 형태
                if (is_slimp(s, start + 2, length - 3) and
                        start + length - 1 < len(s) and s[start + length - 1] == 'C'):
                    return True
            elif (is_slump(s, start + 1, length - 2) and  # A[Slump]C 형태
                  start + length - 1 < len(s) and s[start + length - 1] == 'C'):
                return True

    return False

def is_slurpy(s: str) -> bool:
    """Slurpy 패턴을 확인하는 함수

    Slurpy = Slimp + Slump
    """
    length = len(s)
    if length < 5:  # 최소 길이 체크
        return False

    # 가능한 모든 분할점에서 Slimp와 Slump 패턴 확인
    for i in range(2, length - 2):
        if is_slimp(s, 0, i) and is_slump(s, i, length - i):
            return True

    return False

t = int(input())
for _ in range(t):
    s = input().strip()
    print("YES" if is_slurpy(s) else "NO")

'''
[예제 실행 과정]
입력: "AHDFG"
1. is_slurpy("AHDFG") 호출
2. i=2에서 분할 시도:
   - is_slimp("AH", 0, 2) -> True (AH 형태)
   - is_slump("DFG", 2, 3) -> True (DFG 형태)
3. 결과: "YES"

[주의사항]
1. 인덱스 범위 검사가 중요
2. 재귀 호출 시 부분 문자열의 길이 계산 주의
3. 최소 길이 조건 확인 필요
'''
