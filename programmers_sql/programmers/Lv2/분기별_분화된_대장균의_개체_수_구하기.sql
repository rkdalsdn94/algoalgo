# 프로그래머스 SQL - Lv2 - 분기별 분화된 대장균의 개체 수 구하기 - String, Date 문제
/**
    String, Date 문제

    [핵심 아이디어]
        1. MONTH() 함수를 사용하여 날짜에서 월 정보를 추출
        2. CASE 문을 활용하여 월별 분기 구분 (1~3월: 1Q, 4~6월: 2Q, 7~9월: 3Q, 10~12월: 4Q)
        3. GROUP BY를 사용하여 분기별로 데이터를 그룹화하고 COUNT()로 개체 수 집계

    [풀이 과정]
        1. ECOLI_DATA 테이블에서 DIFFERENTIATION_DATE 컬럼의 월 정보를 MONTH() 함수로 추출
        2. CASE 문으로 월 범위에 따른 분기 분류:
           - 1~3월(월 <= 3): '1Q'
           - 4~6월(월 <= 6): '2Q'
           - 7~9월(월 <= 9): '3Q'
           - 10~12월(나머지): '4Q'
        3. GROUP BY QUARTER로 분기별 그룹화 수행
        4. COUNT(*)로 각 분기별 대장균 개체 수 계산
        5. ORDER BY QUARTER로 분기 순서대로 오름차순 정렬
 */

SELECT
    CASE
        WHEN MONTH(DIFFERENTIATION_DATE) <= 3 THEN '1Q'
        WHEN MONTH(DIFFERENTIATION_DATE) <= 6 THEN '2Q'
        WHEN MONTH(DIFFERENTIATION_DATE) <= 9 THEN '3Q'
        ELSE '4Q'
        END AS QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER
