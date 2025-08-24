# 프로그래머스 sql - Lv1 - 잡은 물고기의 평균 길이 구하기 - IS NULL 문제
/**
  IS NULLL 문제

    [핵심 아이디어]
        1. FISH_INFO 테이블에서 LENGTH가 NULL인 경우를 처리하기 위해 IFNULL 함수를 사용
        2. 평균 길이를 계산할 때 NULL 값을 10으로 대체하여 계산

    [풀이 과정]
        1. FISH_INFO 테이블에서 LENGTH 컬럼을 선택
        2. IFNULL 함수를 사용하여 LENGTH가 NULL인 경우 10으로 대체
        3. AVG 함수를 사용하여 평균 길이를 계산하고 소수점 둘째 자리까지 반올림
        4. 최종 결과를 AVERAGE_LENGTH라는 별칭으로 출력
 */

SELECT
    ROUND(AVG(IFNULL(LENGTH, 10)), 2) AS AVERAGE_LENGTH
FROM FISH_INFO
