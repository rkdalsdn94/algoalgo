# 프로그래머스 sql - Lv2 - 진료과별 총 예약 횟수 출력하기 - GROUP BY 문제
/**
GROUP BY 문제

[핵심 아이디어]
    1. 날짜 범위 조건으로 2022년 5월 전체 데이터를 필터링한다.
    2. GROUP BY를 사용하여 진료과코드별로 그룹화하고 COUNT()로 예약 건수를 집계한다.
    3. ORDER BY를 사용하여 예약건수 오름차순, 진료과코드 오름차순으로 정렬한다.

[풀이 과정]
    1. WHERE 절에서 2022년 5월 전체 기간의 예약을 조회하기 위해 날짜 범위 조건을 설정한다.
    2. GROUP BY로 진료과코드(MCDP_CD)별로 데이터를 그룹화한다.
    3. COUNT(*)로 각 진료과별 예약 건수를 계산한다.
    4. ORDER BY로 예약건수 기준 오름차순, 동일한 경우 진료과코드 기준 오름차순으로 정렬한다.
    5. 컬럼명을 AS를 사용하여 요구사항에 맞게 변경한다.
*/

SELECT
    MCDP_CD AS '진료과 코드',
    COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD;
