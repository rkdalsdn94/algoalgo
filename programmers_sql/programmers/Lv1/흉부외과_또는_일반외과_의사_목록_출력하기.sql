# 프로그래머스 sql - Lv1 - 흉부외과 또는 일반외과 의사 목록 출력하기 - SELECT 문제
/**
    SELECT 문제

    [핵심 아이디어]
    1. 특정 진료과(CS: 흉부외과, GS: 일반외과) 의사만 필터링
    2. DATE_FORMAT 함수를 사용하여 날짜를 'YYYY-MM-DD' 형식으로 변환
    3. 다중 정렬 조건 적용 (고용일자 내림차순 → 이름 오름차순)
    4. IN 연산자를 활용한 효율적인 조건 처리

    [풀이 과정]
    1단계: 출력할 컬럼 선택 (DR_NAME, DR_ID, MCDP_CD, HIRE_YMD)
    2단계: WHERE 절로 진료과 조건 필터링 (CS 또는 GS)
    3단계: DATE_FORMAT으로 고용일자 형식을 'YYYY-MM-DD'로 변환
    4단계: ORDER BY로 정렬 조건 적용
           - 1차: HIRE_YMD DESC (고용일자 최신순)
           - 2차: DR_NAME ASC (이름 가나다순)
 */

SELECT
    DR_NAME,
    DR_ID,
    MCDP_CD,
    DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC;
