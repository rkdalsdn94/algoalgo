# 프로그래머스 SQL - Lv3 - 오랜 기간 보호한 동물 2 - String, Date 문제
/**
String, Date 문제

[핵심 아이디어]
    1. 입양을 간 동물만 대상 (ANIMAL_OUTS 테이블 기준으로 조인)
    2. 보호 기간 = 입양일(OUTS.DATETIME) - 보호 시작일(INS.DATETIME)
    3. DATEDIFF 함수로 날짜 차이 계산
    4. 보호 기간이 긴 순으로 정렬 후 상위 2마리 선택

[풀이 과정]
    1. ANIMAL_OUTS와 ANIMAL_INS를 ANIMAL_ID로 INNER JOIN (입양 간 동물 필터링)
    2. DATEDIFF(입양일, 보호시작일)로 보호 기간 계산
    3. 보호 기간 내림차순 정렬 (긴 순서)
    4. LIMIT 2로 상위 2마리만 선택
*/

SELECT
    O.ANIMAL_ID,
    O.NAME
FROM ANIMAL_OUTS O
JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
ORDER BY
    DATEDIFF(O.DATETIME, I.DATETIME) DESC  -- 보호 기간 = 입양일 - 보호시작일
LIMIT 2;  -- 상위 2마리만 선택
