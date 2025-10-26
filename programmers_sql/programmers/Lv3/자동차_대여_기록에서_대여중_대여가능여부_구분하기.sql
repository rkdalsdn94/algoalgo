# 프로그래머스 SQL - Lv3 - 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기 - GROUP BY 문제
/**
  [문제 분류]
    GROUP BY, CASE 문, 조건부 집계

  [핵심 아이디어]
    - 한 자동차가 여러 대여 기록을 가질 수 있으므로 CAR_ID로 그룹화
    - 특정 날짜(2022-10-16)가 대여 시작일과 종료일 사이에 있는지 확인
    - MAX 함수와 CASE 문을 조합하여 각 자동차별로 해당 날짜에 대여 중인지 판단

  [풀이 과정]
    1. CAR_ID로 그룹화하여 각 자동차의 모든 대여 기록을 집계
    2. 각 대여 기록에서 '2022-10-16'이 START_DATE와 END_DATE 사이에 있으면 1, 아니면 0 반환
    3. MAX 함수로 해당 자동차의 모든 기록 중 하나라도 1이 있으면 '대여중', 없으면 '대여 가능' 표시
    4. CAR_ID를 기준으로 내림차순 정렬
 */

SELECT
    CAR_ID,
    CASE
        WHEN MAX(
                CASE
                    WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1
                    ELSE 0
                END
             ) = 1 THEN '대여중'
        ELSE '대여 가능'
        END AS AVAILABILITY
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY
    CAR_ID
ORDER BY
    CAR_ID DESC;
