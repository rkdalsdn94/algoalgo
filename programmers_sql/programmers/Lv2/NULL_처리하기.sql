# 프로그래머스 sql - Lv2 - NULL 처리하기 - IS NULL 문제
/**
    IS NULL 문제

    [핵심 아이디어]
        1. NULL 값을 다른 값으로 치환하는 함수를 사용
        2. IFNULL, COALESCE, CASE WHEN 등을 활용하여 NULL 처리
        3. 결과를 ANIMAL_ID 순으로 정렬

    [풀이 과정]
        1. ANIMAL_INS 테이블에서 필요한 컬럼들을 선택
        2. NAME 컬럼이 NULL인 경우 "No name"으로 치환
        3. ANIMAL_ID 기준으로 오름차순 정렬하여 결과 출력
 */

SELECT ANIMAL_TYPE,
       IFNULL(NAME, 'No name') AS NAME,
       SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
