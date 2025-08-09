# 프로그래머스 sql - Lv2 - 물고기 종류 별 잡은 수 구하기 - GROUP BY, JOIN 문제
/**
    GROUP BY, JOIN 문제

    [핵심 아이디어]
        1. FISH_INFO와 FISH_NAME_INFO 테이블을 FISH_TYPE으로 조인한다
        2. 물고기 종류별로 그룹화하여 각 종류별 잡은 수를 계산한다
        3. 잡은 수를 기준으로 내림차순 정렬한다

    [풀이 과정]
        1. FISH_INFO 테이블과 FISH_NAME_INFO 테이블을 FISH_TYPE 컬럼으로 INNER JOIN한다
        2. FISH_TYPE과 FISH_NAME으로 GROUP BY하여 물고기 종류별로 그룹화한다
        3. COUNT 함수를 사용하여 각 그룹의 물고기 잡은 수를 계산한다
        4. ORDER BY를 사용하여 잡은 수(FISH_COUNT) 기준으로 내림차순 정렬한다
 */

SELECT
    COUNT(*) AS FISH_COUNT,
    B.FISH_NAME AS FISH_NAME
FROM FISH_INFO A
    JOIN FISH_NAME_INFO B ON A.FISH_TYPE = B.FISH_TYPE
GROUP BY A.FISH_TYPE, B.FISH_NAME
ORDER BY FISH_COUNT DESC
