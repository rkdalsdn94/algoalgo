# 프로그래머스 - Lv1 - 상위 n개 레코드 - SELECT 문제
/**
SELECT 문제
[핵심 아이디어]
    1. DATETIME 기준으로 정렬하여 가장 빠른 날짜의 데이터를 찾는다.
    2. LIMIT을 사용하여 첫 번째 결과만 반환한다.

[풀이 과정]
    1. ANIMAL_INS 테이블에서 NAME 컬럼을 선택한다.
    2. DATETIME 컬럼을 기준으로 오름차순 정렬하여 가장 빠른 날짜(가장 먼저 들어온 동물)를 맨 앞에 위치시킨다.
    3. LIMIT 1을 사용하여 첫 번째 결과만 가져온다.
 */

SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1;
