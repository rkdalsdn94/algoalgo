# 프로그래머스 sql - Lv3 - 조건별로 분류하여 주문상태 출력하기 - String, Date 문제
/**
String, Date 문제

[핵심 아이디어]
    1. CASE WHEN 구문을 사용하여 출고일자(OUT_DATE)를 기준으로 조건 분기
    2. NULL 체크를 먼저 수행 (NULL은 비교 연산이 불가능하므로 IS NULL 사용)
    3. 날짜 비교를 통해 기준일(2022-05-01) 이전/이후 판단

[풀이 과정]
    1. OUT_DATE가 NULL인 경우 → '출고미정'
    2. OUT_DATE가 2022-05-01 이전이거나 같은 경우 → '출고완료'
    3. OUT_DATE가 2022-05-01 이후인 경우 → '출고대기'
    4. 주문 ID 기준 오름차순 정렬
*/

SELECT
    ORDER_ID,
    PRODUCT_ID,
    DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
    CASE
        WHEN OUT_DATE IS NULL THEN '출고미정'
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        ELSE '출고대기'
        END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID;
