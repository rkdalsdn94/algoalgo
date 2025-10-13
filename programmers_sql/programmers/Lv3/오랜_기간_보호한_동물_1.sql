# 프로그래머스 sql - Lv3 - 오랜 기간 보호한 동물 1 - JOIN 문제
/**
  JOIN 문제

[핵심 아이디어]
    1. ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블을 LEFT JOIN하여 입양되지 않은 동물 찾기
    2. LEFT JOIN 후 AO.ANIMAL_ID가 NULL인 레코드만 선택 (입양되지 않은 동물)
    3. 입양되지 않은 동물 중 보호 기간이 가장 긴 상위 3마리 선택
    4. 보호 시작일(DATETIME) 기준 오름차순 정렬

[풀이 과정]
    1. ANIMAL_INS와 ANIMAL_OUTS를 ANIMAL_ID로 LEFT JOIN
    2. WHERE 절에서 AO.ANIMAL_ID IS NULL 조건으로 입양되지 않은 동물 필터링
    3. DATETIME 기준 오름차순 정렬 후 LIMIT 3으로 상위 3마리 선택
    4. NAME과 DATETIME 컬럼 선택
    5. 결과 출력
 */

SELECT
    AI.NAME AS NAME,
    AI.DATETIME AS DATETIME
FROM
    ANIMAL_INS AI
LEFT JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE
    AO.ANIMAL_ID IS NULL
ORDER BY AI.DATETIME ASC
LIMIT 3;
