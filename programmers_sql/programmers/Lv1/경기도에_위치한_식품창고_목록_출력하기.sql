# 프로그래머스 sql - Lv1 - 경기도에 위치한 식품창고 목록 출력하기 - IS NULL 문제
/**
    IS NULL 문제

    [핵심 아이디어]
        1. NULL 값 처리를 위한 IFNULL 함수 활용
        2. 문자열 패턴 매칭을 위한 LIKE 연산자 사용
        3. 결과 정렬을 위한 ORDER BY 절 활용

    [풀이 과정]
        1. SELECT 절에서 필요한 컬럼들(WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, FREEZER_YN)을 선택
        2. IFNULL(FREEZER_YN, 'N')를 사용하여 냉동시설 여부가 NULL인 경우 'N'으로 출력
        3. WHERE 절에서 ADDRESS LIKE '%경기도%'를 사용하여 경기도에 위치한 창고만 필터링
        4. ORDER BY WAREHOUSE_ID를 사용하여 창고 ID 기준 오름차순 정렬
 */

SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '%경기도%'
ORDER BY WAREHOUSE_ID;
