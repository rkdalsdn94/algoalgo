# 프로그래머스 sql - Lv2 - 중성화 여부 파악하기 - String, Date 문제
/**
    String, Date 문제

    [핵심 아이디어]
        1. SEX_UPON_INTAKE 컬럼에서 'Neutered' 또는 'Spayed' 키워드 검색
        2. CASE WHEN 문을 사용하여 조건에 따른 다른 값 출력
        3. LIKE 연산자로 문자열 패턴 매칭 수행

    [풀이 과정]
        1. ANIMAL_INS 테이블에서 ANIMAL_ID, NAME 컬럼 선택
        2. CASE WHEN 문으로 SEX_UPON_INTAKE 컬럼 값 검사:
           - 'Neutered' 또는 'Spayed' 포함 시 'O' 반환
           - 그 외의 경우 'X' 반환
        3. 결과를 ANIMAL_ID 기준으로 오름차순 정렬
*/

SELECT
    ANIMAL_ID,
    NAME,
    CASE
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%'
            OR SEX_UPON_INTAKE LIKE '%Spayed%'
            THEN 'O'
        ELSE 'X'
        END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
