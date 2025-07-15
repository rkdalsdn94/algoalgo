# 프로그래머스 sql - Lv2 - DATETIME에서 DATE로 형 변환 - String, Date 문제
/**
    String, Date 문제

    [핵심 아이디어]
        1. DATETIME 형식을 DATE 형식으로 변환하는 함수 사용
        2. DATE_FORMAT 또는 CAST 함수를 활용하여 변환
        3. 결과를 ANIMAL_ID 순으로 정렬

    [풀이 과정]
        1. ANIMAL_INS 테이블에서 DATETIME 컬럼을 DATE 형식으로 변환
        2. 변환된 DATE 값을 ANIMAL_ID 기준으로 오름차순 정렬하여 결과 출력
 */

SELECT ANIMAL_ID, NAME,
       DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
