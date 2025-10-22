# 프로그래머스 SQL - Lv3 - 없어진 기록 찾기 - JOIN 문제
/**
JOIN 문제

[핵심 아이디어]
    입양 기록(ANIMAL_OUTS)은 있지만 보호소 입소 기록(ANIMAL_INS)이 없는
    데이터 유실 케이스를 찾는 문제입니다.
    LEFT JOIN 후 NULL 체크로 해결할 수 있습니다.

[풀이 과정]
    1. ANIMAL_OUTS를 기준 테이블로 설정 (입양 기록이 있는 동물들)
    2. ANIMAL_INS를 ANIMAL_ID 기준으로 LEFT JOIN
    3. JOIN 결과에서 ANIMAL_INS.ANIMAL_ID IS NULL인 레코드 필터링 (입소 기록이 없는 = 데이터가 유실된 경우)
    4. ANIMAL_ID 오름차순 정렬
 */

SELECT
    O.ANIMAL_ID,
    O.NAME
FROM
    ANIMAL_OUTS O
    LEFT JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE
    I.ANIMAL_ID IS NULL  -- 입소 기록이 없는 경우
ORDER BY
    O.ANIMAL_ID ASC;
