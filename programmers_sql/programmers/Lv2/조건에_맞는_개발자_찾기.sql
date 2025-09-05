# 프로그래머스 SQL - Lv2 - 조건에 맞는 개발자 찾기 - SELECT 문제
/**
  SELECT 문제

  [핵심 아이디어]
    - SKILL_CODE는 여러 스킬 코드의 비트 OR 연산 결과
    - 특정 스킬 보유 여부는 비트 AND 연산으로 확인
    - A & B > 0 이면 A에 B 스킬이 포함되어 있음

  [풀이 과정]
    1. SKILLCODES 테이블에서 Python과 C#의 CODE 값을 서브쿼리로 조회
    2. 각 개발자의 SKILL_CODE와 해당 스킬 CODE를 비트 AND 연산
    3. 결과가 0보다 크면 해당 스킬을 보유한 것으로 판단
    4. Python 또는 C# 중 하나라도 보유한 개발자를 필터링
    5. ID 기준 오름차순 정렬
*/

SELECT
    D.ID,
    D.EMAIL,
    D.FIRST_NAME,
    D.LAST_NAME
FROM DEVELOPERS D
WHERE D.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') > 0
   OR D.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') > 0
ORDER BY D.ID;
