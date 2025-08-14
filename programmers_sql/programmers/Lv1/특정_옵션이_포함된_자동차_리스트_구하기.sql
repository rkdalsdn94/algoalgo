# 프로그래머스 sql - Lv1 - 특정 옵션이 포함된 자동차 리스트 구하기 - String, Date
/**
    String, Date 문제

    [핵심 아이디어]
        1. CAR_RENTAL_COMPANY_CAR 테이블에서 OPTIONS 컬럼에 '네비게이션'이 포함된 행을 필터링
        2. LIKE 연산자와 와일드카드(%)를 사용하여 문자열 패턴 매칭 수행
        3. 결과를 CAR_ID 기준으로 내림차순 정렬하여 출력

    [풀이 과정]
        1. CAR_RENTAL_COMPANY_CAR 테이블에서 OPTIONS 컬럼이 '네비게이션' 문자열을 포함하는 행을 선택
        2. WHERE절에서 LIKE '%네비게이션%' 조건을 사용하여 해당 옵션이 포함된 자동차 필터링
        3. SELECT절로 CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS 컬럼을 조회
        4. ORDER BY CAR_ID DESC로 자동차 ID 기준 내림차순 정렬
*/

SELECT
    CAR_ID,
    CAR_TYPE,
    DAILY_FEE,
    OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;
