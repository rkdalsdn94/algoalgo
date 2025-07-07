# 프로그래머스 sql - Lv1 - 조건에 맞는 회원수 구하기 - SELECT 문제
/**
  SELECT 문제

  where 절을 이용해서 조건에 맞는 회원수를 구하는 문제이다.
  where 절을 이용해서 joined 날짜와 age를 조건으로 걸어주면 된다.
  날짜를 '2021-01-01' ~ '2021-12-31'로 걸어주고, age는 20 ~ 29로 걸어주면 된다.
  이 방식으로 처음에는 >=, <= 이런 식으로 풀었지만, 이후 MySQL 내장 함수인 YEAR()를 사용했다.
 */

SELECT
    COUNT(*) AS users
FROM user_info
WHERE joined >= '2021-01-01'
  AND joined <= '2021-12-31'
  AND age >= 20
  AND age <= 29;

# or (YEAR() 함수 사용)
SELECT
    COUNT(*) AS users
FROM user_info
WHERE YEAR(joined) = 2021
  AND age BETWEEN 20 AND 29;
