# 프로그래머스 sql - Lv1 - 여러 기준으로 정렬하기 - SELECT, 정렬 문제
/**
  SELECT, 정렬 문제

  단순한 SELECT + 정렬 문제이다.
  `NAME`과 `DATETIME`의 정렬 조건만 만족하면 된다.
 */

SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC
