# 프로그래머스 sql - Lv2 - 고양이와 개는 몇 마리 있을까 - GROUP BY 문제
/**
    GROUP BY 문제

    [핵심 아이디어]
        1. ANIMAL_INS 테이블에서 ANIMAL_TYPE 컬럼을 기준으로 그룹화
        2. COUNT 함수를 사용하여 각 동물 유형의 개수 계산
        3. ORDER BY 절로 ANIMAL_TYPE 기준 오름차순 정렬로 Cat을 Dog보다 먼저 조회

    [풀이 과정]
        1. ANIMAL_INS 테이블에서 ANIMAL_TYPE과 해당 타입의 개수를 조회
        2. GROUP BY ANIMAL_TYPE으로 동물 유형별 그룹화
        3. COUNT(ANIMAL_ID)로 각 그룹의 동물 개수 계산
        4. ORDER BY ANIMAL_TYPE으로 알파벳 순 정렬 (Cat → Dog 순서)
 */
SELECT
    ANIMAL_TYPE,
    COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
