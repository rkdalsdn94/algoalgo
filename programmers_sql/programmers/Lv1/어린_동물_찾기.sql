# 프로그래머스 sql - Lv1 - 어린 동물 찾기 - 단순 SELECT 문제
/**
    단순 SELECT 문제

    단순히 INTAKE_CONDITION이 'Aged'가 아닌 동물의 ANIMAL_ID와 NAME을 조회하는 문제이다.
 */

SELECT
    ANIMAL_ID,
    NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID
