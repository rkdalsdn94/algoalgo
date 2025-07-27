# 프로그래머스 sql - Lv1 - 나이 정보가 없는 회원 수 구하기 - IS NULL 문제
/**
    IS NULL 문제

    IS NULL 조건을 이용해서 나이 정보가 없는 회원의 수를 구하는 문제이다.
    또한, COUNT(*)를 사용하여 전체 행의 수를 구할 수 있다.
 */

SELECT
    COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;
