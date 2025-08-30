# 프로그래머스 sql - Lv2 - 자동차 평균 대여 기간 구하기 - String, Date 문제
/**
    String, Date 문제

    [핵심 아이디어]
        1. DATEDIFF 함수를 사용하여 각 대여 기록의 대여 기간 계산 (당일 포함을 위해 +1)
        2. GROUP BY로 자동차별 그룹화하여 평균 대여 기간 계산
        3. HAVING 절로 평균 대여 기간이 7일 이상인 자동차만 필터링
        4. ROUND 함수로 소수점 둘째 자리에서 반올림
        5. ORDER BY로 평균 대여 기간 내림차순, 자동차 ID 내림차순 정렬

    [풀이 과정]
        1. CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 각 대여 기록의 대여 기간을
           DATEDIFF(END_DATE, START_DATE) + 1로 계산 (당일 포함)
        2. GROUP BY CAR_ID로 자동차별로 그룹화
        3. AVG 함수로 각 자동차의 평균 대여 기간 계산
        4. HAVING 절로 평균 대여 기간이 7일 이상인 자동차만 필터링
        5. ROUND 함수로 평균값을 소수점 둘째 자리에서 반올림
        6. ORDER BY 절로 평균 대여 기간 내림차순, 자동차 ID 내림차순으로 정렬
 */

SELECT
    CAR_ID,
    ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVG(DATEDIFF(END_DATE, START_DATE) + 1) >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;
