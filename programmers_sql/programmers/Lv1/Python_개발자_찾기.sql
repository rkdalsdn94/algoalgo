# 프로그래머스 sql - Lv1 - Python 개발자 찾기 - 단순 SELECT 문제
/**
    단순 SELECT 문제

    [핵심 아이디어]
        1. DEVELOPER_INFOS 테이블에서 SKILL_1, SKILL_2, SKILL_3 컬럼을 기준으로 'Python' 기술을 가진 개발자 찾기
        2. WHERE 절에서 각 기술 컬럼에 'Python'이 포함된 조건 필터링
        3. ID 기준으로 오름차순 정렬하여 결과 출력

    [풀이 과정]
        1. DEVELOPER_INFOS 테이블에서 ID, EMAIL, FIRST_NAME, LAST_NAME 컬럼 선택
        2. WHERE 절에서 SKILL_1, SKILL_2, SKILL_3 중 하나라도 'Python'인 조건 필터링
        3. ORDER BY로 ID 기준 오름차순 정렬하여 최종 결과 출력
 */

SELECT
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python'
   OR SKILL_2 = 'Python'
   OR SKILL_3 = 'Python'
ORDER BY ID;
