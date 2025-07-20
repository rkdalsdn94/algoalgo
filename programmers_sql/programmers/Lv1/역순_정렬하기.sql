# 프로그래머스 sql - Lv1 - 역순 정렬하기 - SELECT 문제
/**
    SELECT 문제

    단순하게 ANIMAL_INS 테이블에서 NAME과 DATETIME 컬럼을 선택하고, ANIMAL_ID를 기준으로 내림차순 정렬하는 문제이다.
 */

SELECT
    NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
