# 프로그래머스 SQL - Lv3 - 대여 기록이 존재하는 자동차 리스트 구하기 - String, Date 문제
/**
String, Date 문제

[핵심 아이디어]
    1. CAR 테이블과 RENTAL_HISTORY 테이블을 CAR_ID로 조인
    2. 자동차 종류가 '세단'이고 대여 시작일이 10월인 레코드 필터링
    3. DISTINCT로 중복 제거 후 내림차순 정렬

[풀이 과정]
    1. 두 테이블을 CAR_ID 기준으로 INNER JOIN
    2. WHERE 절로 CAR_TYPE = '세단' 조건 적용
    3. MONTH(START_DATE) = 10 조건으로 10월 대여 시작 필터링
    4. DISTINCT로 중복된 CAR_ID 제거
    5. ORDER BY로 내림차순 정렬
 */

SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR C
         JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
              ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE = '세단'
  AND MONTH(H.START_DATE) = 10
ORDER BY C.CAR_ID DESC;
