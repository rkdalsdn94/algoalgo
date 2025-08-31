# 프로그래머스 SQL - Lv2 - 노선별 평균 역 사이 거리 조회하기 - GROUP BY 문제
/**
    GROUP BY 문제

    [핵심 아이디어]
        1. SUBWAY_DISTANCE 테이블에서 노선(ROUTE)별로 그룹화하여 집계 함수 활용
        2. 각 노선의 역 사이 거리(D_BETWEEN_DIST)를 SUM과 AVG로 집계
        3. ORDER BY 절에서 문자열 정렬 함정을 피하기 위해 원본 숫자값으로 정렬

    [풀이 과정]
        1. GROUP BY ROUTE로 노선별 그룹화
        2. SUM(D_BETWEEN_DIST)로 총 누계 거리 계산 후 ROUND(..., 1)로 소수 둘째자리에서 반올림
        3. AVG(D_BETWEEN_DIST)로 평균 역 사이 거리 계산 후 ROUND(..., 2)로 소수 셋째자리에서 반올림
        4. CONCAT 함수로 단위(km) 추가하여 최종 문자열 형태로 출력
        5. ORDER BY 절에서 CONCAT된 문자열이 아닌 원본 숫자값 SUM(D_BETWEEN_DIST)으로 내림차순 정렬
        6. 문자열로 정렬하면 "10km" < "2km" 같은 사전순 정렬이 되므로 주의 필요
 */

SELECT
    ROUTE,
    CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
    CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC;
