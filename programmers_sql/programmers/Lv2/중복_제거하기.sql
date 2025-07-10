# 프로그래머스 sql - Lv2 - 중복 제거하기 - COUNT, DISTINCT 문제
/**
COUNT, DISTINCT 문제

[핵심 아이디어]
    1. 중복되는 이름을 하나로 처리하기 위해 DISTINCT 키워드 사용
    2. NULL 값은 집계에서 제외하기 위해 WHERE 조건 추가
    3. COUNT와 DISTINCT를 함께 사용하여 고유한 이름의 개수 계산

[풀이 과정]
    1. ANIMAL_INS 테이블에서 NAME 컬럼을 대상으로 조회
    2. WHERE NAME IS NOT NULL 조건으로 NULL 값 제외
    3. COUNT(DISTINCT name)으로 중복을 제거한 후 개수 계산
    4. 결과를 count라는 별칭으로 반환
*/

SELECT
    COUNT(DISTINCT name) as count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;
