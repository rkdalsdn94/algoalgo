# 프로그래머스 sql - Lv2 - 루시와 엘라 찾기 - String, Date 문제
/**
    String, Date 문제

    [핵심 아이디어]
    1. IN 연산자를 사용하여 여러 개의 특정 이름에 해당하는 동물들을 한 번에 필터링
    2. ORDER BY를 사용하여 ANIMAL_ID 기준 오름차순 정렬
    3. 성별 조건 없이 이름 조건만 적용하여 해당하는 모든 동물 조회

    [풀이 과정]
    1. ANIMAL_INS 테이블에서 ANIMAL_ID, NAME, SEX_UPON_INTAKE 컬럼 선택
    2. WHERE 절에서 IN 연산자로 지정된 6개 이름('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')에 해당하는 동물들만 필터링
    3. ORDER BY ANIMAL_ID로 아이디 순(오름차순)으로 정렬하여 결과 출력
 */

SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;
