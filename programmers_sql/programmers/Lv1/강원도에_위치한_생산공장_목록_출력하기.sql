# 프로그래머스 sql - Lv1 - 강원도에 위치한 생산공장 목록 출력하기 - SELECT 문제
/**
    SELECT 문제

    [핵심 아이디어]
        1. SELECT 절에서 필요한 컬럼들을 선택
        2. WHERE 절에서 특정 조건을 만족하는 행을 필터링
        3. ORDER BY 절을 사용하여 결과를 정렬

    [풀이 과정]
        1. FOOD_FACTORY 테이블에서 FACTORY_ID, FACTORY_NAME, ADDRESS 컬럼을 선택
        2. WHERE 절에서 ADDRESS LIKE '강원도%'를 사용하여 강원도에 위치한 생산공장만 필터링
        3. ORDER BY 절을 사용하여 FACTORY_ID 기준으로 오름차순 정렬
 */

SELECT
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID;
