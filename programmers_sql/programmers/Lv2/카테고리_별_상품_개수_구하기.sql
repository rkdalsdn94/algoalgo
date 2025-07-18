# 프로그래머스 sql - Lv2 - 카테고리 별 상품 개수 구하기 - String, Date 문제
/**
String, Date 문제

[핵심 아이디어]
    1. PRODUCT_CODE의 앞 2자리를 추출하여 카테고리 코드로 사용
    2. 추출한 카테고리 코드별로 그룹화하여 상품 개수 계산
    3. 카테고리 코드 기준으로 오름차순 정렬

[풀이 과정]
    1. LEFT 함수를 사용하여 PRODUCT_CODE의 앞 2자리를 추출
    2. 추출한 카테고리 코드로 GROUP BY하여 각 카테고리별 상품 개수 계산
    3. COUNT(*)를 사용하여 각 그룹의 레코드 수 계산
    4. ORDER BY CATEGORY로 카테고리 코드 기준 오름차순 정렬
*/

SELECT
    LEFT(PRODUCT_CODE, 2) AS CATEGORY,
    COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE, 2)
ORDER BY CATEGORY;
