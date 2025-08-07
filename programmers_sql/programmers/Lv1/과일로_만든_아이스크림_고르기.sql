# 프로그래머스 sql - Lv1 - 과일로 만든 아이스크림 고르기 - SELECT 문제
/**
    SELECT 문제

    [핵심 아이디어]
        1. FIRST_HALF 테이블에서 FLAVOR와 TOTAL_ORDER 컬럼을 선택
        2. WHERE 절로 TOTAL_ORDER가 3000 이상인 행 필터링
        3. FLAVOR가 'strawberry' 또는 'melon'인 행만 선택

    [풀이 과정]
        1. FIRST_HALF 테이블에서 FLAVOR와 TOTAL_ORDER 컬럼을 조회
        2. WHERE 절로 TOTAL_ORDER >= 3000 조건 추가
        3. FLAVOR IN ('strawberry', 'melon') 조건으로 특정 맛 필터링
 */

SELECT
    FLAVOR
FROM FIRST_HALF
WHERE TOTAL_ORDER >= 3000
  AND FLAVOR IN ('strawberry', 'melon')
