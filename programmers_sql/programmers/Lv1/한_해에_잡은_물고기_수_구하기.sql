# 프로그래머스 sql - Lv1 - 한 해에 잡은 물고기 수 구하기 - String, Date 문제
/**
    String, Date 문제

    [핵심 아이디어]
        1. FISH_INFO 테이블에서 TIME 컬럼을 기준으로 2021년도 데이터 필터링
        2. YEAR() 함수를 사용하여 날짜에서 연도 추출
        3. WHERE 절로 2021년도 조건 지정
        4. COUNT() 함수로 해당 조건의 레코드 수 계산

    [풀이 과정]
        1. FISH_INFO 테이블에서 TIME 컬럼의 연도가 2021인 데이터만 필터링
        2. WHERE YEAR(TIME) = 2021 조건으로 2021년도 데이터만 선택
        3. COUNT(*)로 조건에 맞는 물고기의 총 개수 계산
 */

SELECT
    COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE YEAR(TIME) = 2021;
