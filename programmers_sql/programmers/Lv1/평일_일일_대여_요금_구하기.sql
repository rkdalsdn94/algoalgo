# 프로그래머스 sql - Lv1 - 평일 일일 대여 요금 구하기 - SELECT 문제
/**
    SELECT 문제

    [핵심 아이디어]
        1. CAR_RENTAL_COMPANY_CAR 테이블에서 평일(월~금) 대여 요금(DAY_FEE) 계산
        2. CAR_TYPE이 'SUV'인 차량만 필터링
        3. AVG 함수를 사용하여 평균 대여 요금 계산

    [풀이 과정]
        1. CAR_RENTAL_COMPANY_CAR 테이블에서 CAR_TYPE이 'SUV'인 행을 선택
        2. DAILY_FEE 컬럼의 평균값을 계산하여 결과 출력
 */

SELECT
    ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';
