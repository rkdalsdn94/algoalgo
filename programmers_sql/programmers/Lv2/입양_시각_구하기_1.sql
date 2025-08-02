# 프로그래머스 sql - Lv2 - 입양 시각 구하기 - GROUP BY 문제
/**
    GROUP BY 문제

    [핵심 아이디어]
        1. ANIMAL_OUTS 테이블에서 DATETIME 컬럼을 기준으로 시간(HOUR) 추출
        2. HOUR(DATETIME) 함수로 시간 단위로 그룹화
        3. COUNT 함수를 사용하여 각 시간대의 입양 건수 계산
        4. ORDER BY 절로 시간(HOUR) 기준 오름차순 정렬

    [풀이 과정]
        1. ANIMAL_OUTS 테이블에서 DATETIME 컬럼의 시간(HOUR)을 추출
        2. HOUR(DATETIME) BETWEEN 9 AND 19 조건으로 오전 9시부터 오후 7시까지 필터링
        3. GROUP BY HOUR(DATETIME)으로 시간별 그룹화
        4. COUNT(*)로 각 시간대의 입양 건수 계산
        5. ORDER BY hour로 결과를 시간 순으로 정렬
 */

SELECT
    HOUR(DATETIME) as HOUR,
    COUNT(*) as COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR(DATETIME)
ORDER BY hour;
