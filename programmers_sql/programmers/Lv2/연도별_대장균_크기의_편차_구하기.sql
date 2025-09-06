# 프로그래머스 SQL - Lv2 - 연도별 대장균 크기의 편차 구하기 - SUM, MAX, MIN 문제
/**
  SUM, MAX, MIN 문제

  [핵심 아이디어]
    윈도우 함수를 사용해서 연도별 최대 크기를 구하고, 각 개체의 크기와의 차이를 계산하여 편차를 구한다.

  [풀이 과정]
    1. YEAR() 함수로 분화 날짜에서 연도를 추출
    2. MAX() OVER() 윈도우 함수로 연도별 최대 크기 계산
    3. 최대 크기에서 각 개체의 크기를 빼서 편차 계산
    4. 연도, 편차 순으로 오름차순 정렬
 */

SELECT
    YEAR(DIFFERENTIATION_DATE) AS YEAR,
    MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE))
        - SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM ECOLI_DATA
ORDER BY YEAR, YEAR_DEV;
