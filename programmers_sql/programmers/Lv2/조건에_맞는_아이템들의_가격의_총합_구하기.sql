# 프로그래머스 sql - Lv2 - 조건에 맞는 아이템들의 가격의 총합 구하기 - 집계함수(SUM) 문제
/**
    집계함수(SUM) 문제

    [핵심 아이디어]
        1. 특정 조건(RARITY='LEGEND')을 만족하는 레코드들을 필터링한다.
        2. 조건을 만족하는 레코드들의 PRICE 컬럼 값들을 SUM 함수로 합계를 구한다.
        3. 결과 컬럼명을 요구사항에 맞게 'TOTAL_PRICE'로 지정한다.

    [풀이 과정]
        1. FROM절에서 ITEM_INFO 테이블을 대상으로 조회한다.
        2. WHERE절에서 RARITY = 'LEGEND' 조건으로 희귀도가 'LEGEND'인 아이템들만 필터링한다.
        3. SELECT절에서 SUM(PRICE) 함수로 필터링된 아이템들의 가격 총합을 계산한다.
        4. AS TOTAL_PRICE로 결과 컬럼명을 문제에서 요구한 이름으로 지정한다.
*/

SELECT
    SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY = 'LEGEND';
