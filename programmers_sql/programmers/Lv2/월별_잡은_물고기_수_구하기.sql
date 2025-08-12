# 프로그래머스 sql - Lv2 - 월별 잡은 물고기 수 구하기 - GROUP BY 문제
/**
    GROUP BY 문제

    [핵심 아이디어]
        1. FISH_INFO 테이블에서 TIME 컬럼을 기준으로 월(MONTH) 추출
        2. MONTH(TIME) 함수로 월 단위로 그룹화
        3. COUNT 함수를 사용하여 각 월의 물고기 잡은 수 계산
        4. ORDER BY 절로 월 기준 오름차순 정렬

    [풀이 과정]
        1. FISH_INFO 테이블에서 TIME 컬럼의 월(MONTH)을 추출
        2. GROUP BY MONTH(TIME)으로 월별 그룹화
        3. COUNT(*)로 각 월의 물고기 잡은 수 계산
        4. ORDER BY MONTH(TIME)으로 결과를 월 순으로 정렬
*/

SELECT
    COUNT(*) AS FISH_COUNT,
    MONTH(TIME) AS MONTH
FROM FISH_INFO
GROUP BY MONTH(TIME)
ORDER BY MONTH(TIME);
