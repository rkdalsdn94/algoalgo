# 프로그래머스 sql - Lv1 - 자동차 대여 기록에서 장기/단기 대여 구분하기 - String, Date 문제
/**
  String, Date 문제

  [핵심 아이디어]
    2022년 9월 필터링: START_DATE가 2022년 9월에 속하는 레코드만 선택
    대여 기간 계산: DATEDIFF 함수로 시작일과 종료일 간의 차이 계산 (+1 포함)
    조건부 분류: 30일 이상이면 '장기 대여', 미만이면 '단기 대여'
    정렬: HISTORY_ID 기준 내림차순

  [풀이 과정]
    WHERE 절로 2022년 9월 데이터 필터링
    DATEDIFF 함수로 대여 기간 계산 (종료일 - 시작일 + 1)
    CASE WHEN으로 30일 기준 장기/단기 구분
    ORDER BY로 ID 내림차순 정렬
 */

SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여'
        ELSE '단기 대여'
        END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE YEAR(START_DATE) = 2022 AND MONTH(START_DATE) = 9
ORDER BY HISTORY_ID DESC;
