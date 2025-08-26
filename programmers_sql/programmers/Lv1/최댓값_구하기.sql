# 프로그래머스 sql - Lv1 - 최댓값 구하기 - SUM, MAX, MIN 문제
/**
    SUM, MAX, MIN 문제

    [핵심 아이디어]
        1. ANIMAL_INS 테이블에서 DATETIME 컬럼의 최댓값을 찾기
        2. MAX() 함수를 사용하여 DATETIME 컬럼의 최대값 계산
        3. 결과를 '시간'이라는 별칭으로 출력

    [풀이 과정]
        1. ANIMAL_INS 테이블에서 DATETIME 컬럼의 최댓값을 선택
        2. MAX(DATETIME) 함수를 사용하여 최댓값 계산
        3. AS 키워드로 결과에 '시간'이라는 별칭 지정
 */

SELECT
    MAX(DATETIME) AS `시간`
FROM ANIMAL_INS
