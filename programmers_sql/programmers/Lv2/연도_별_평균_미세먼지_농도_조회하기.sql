# 프로그래머스 sql - Lv2 - 연도 별 평균 미세먼지 농도 조회하기 - String, Date 문제
/**
    String, Date 문제

    [핵심 아이디어]
        1. AIR_POLLUTION 테이블에서 YEAR(YM) 함수를 사용하여 연도 추출
        2. ROUND 함수를 사용하여 PM_VAL1과 PM_VAL2의 평균값을 소수점 둘째 자리까지 반올림
        3. GROUP BY 절로 연도별로 그룹화
        4. ORDER BY 절로 연도 기준 오름차순 정렬

    [풀이 과정]
        1. AIR_POLLUTION 테이블에서 YEAR(YM)으로 연도 추출
        2. PM_VAL1과 PM_VAL2의 평균값을 ROUND 함수로 소수점 둘째 자리까지 반올림
        3. GROUP BY YEAR로 연도별 그룹화
        4. ORDER BY YEAR로 결과를 연도 순으로 정렬
 */

SELECT
    YEAR(YM) AS `YEAR`,
    ROUND(AVG(PM_VAL1), 2) AS `PM10`,
    ROUND(AVG(PM_VAL2), 2) AS `PM2.5`
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR
ORDER BY YEAR;
