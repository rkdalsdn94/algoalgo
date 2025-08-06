# 프로그래머스 sql - Lv2 - 가격대 별 상품 개수 구하기 - GROUP BY 문제
/**
    GROUP BY 문제

    [핵심 아이디어]
    1. TRUNCATE 함수를 사용하여 가격을 만원 단위로 자른다
    2. TRUNCATE(PRICE, -4)는 만의 자리 아래를 0으로 만들어 만원 단위 그룹을 생성한다
    3. 그룹별로 COUNT(*)를 사용하여 상품 개수를 센다

    [풀이 과정]
    1. TRUNCATE(PRICE, -4)로 가격을 만원 단위로 변환
        - 4590 → 0, 11100 → 10000, 22200 → 20000
    2. 변환된 가격대별로 GROUP BY를 수행
    3. COUNT(*)로 각 그룹의 상품 개수 계산
    4. ORDER BY로 가격대 기준 오름차순 정렬
 */

SELECT
    TRUNCATE(PRICE, -4) AS PRICE_GROUP,
    COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY TRUNCATE(PRICE, -4)
ORDER BY PRICE_GROUP;
