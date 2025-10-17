# 프로그래머스 SQL - Lv3 - 즐겨찾기가 가장 많은 식당 정보 출력하기 - GROUP BY 문제
/**
GROUP BY 문제

[핵심 아이디어]
    - 음식 종류별로 즐겨찾기수가 가장 많은 식당을 찾는 문제
    - ROW_NUMBER() 윈도우 함수를 사용하여 각 음식 종류 내에서 순위를 매김
    - 순위가 1인 레코드만 필터링하여 최종 결과를 도출

[풀이 과정]
    1. PARTITION BY FOOD_TYPE: 음식 종류별로 그룹을 나눔
    2. ORDER BY FAVORITES DESC: 각 그룹 내에서 즐겨찾기수 기준 내림차순 정렬
    3. ROW_NUMBER()로 각 그룹 내 순위를 1부터 부여
    4. WHERE rn = 1: 각 음식 종류별 1등만 선택
    5. ORDER BY FOOD_TYPE DESC: 최종 결과를 음식 종류 기준 내림차순 정렬
*/

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (
         SELECT
             FOOD_TYPE,
             REST_ID,
             REST_NAME,
             FAVORITES,
             ROW_NUMBER() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS rn
         FROM REST_INFO
     ) ranked
WHERE rn = 1
ORDER BY FOOD_TYPE DESC;
