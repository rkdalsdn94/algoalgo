# 프로그래머스 sql - Lv1 - 잔챙이 잡은 수 구하기 - SELECT 문제
/**
    SELECT 문제

    [핵심 아이디어]
        1. FISH_INFO 테이블에서 LENGTH 컬럼이 NULL인 행을 필터링
        2. COUNT 함수를 사용하여 해당 행의 개수 계산

    [풀이 과정]
        1. FISH_INFO 테이블에서 LENGTH가 NULL인 행을 선택
        2. COUNT(*)로 해당 행의 개수를 계산하여 결과 출력
 */

SELECT
    COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE LENGTH IS NULL
