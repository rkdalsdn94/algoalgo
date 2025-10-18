# 프로그래머스 SQL - Lv3 - 부서별 평균 연봉 조회하기 - GROUP BY, JOIN 문제
/**
GROUP BY, JOIN 문제

[핵심 아이디어]
    1. HR_DEPARTMENT와 HR_EMPLOYEES 테이블을 DEPT_ID 기준으로 JOIN
    2. 부서별로 GROUP BY하여 평균 연봉 계산
    3. ROUND 함수로 소수점 첫째 자리에서 반올림
    4. 평균 연봉 기준 내림차순 정렬

[풀이 과정]
    1. HR_DEPARTMENT(HD)와 HR_EMPLOYEES(HE)를 DEPT_ID로 조인
    2. DEPT_ID로 그룹화하여 각 부서의 평균 연봉 계산
    3. ROUND 함수로 AVG(SAL)의 소수점 첫째 자리 반올림
    4. AVG_SAL 기준 내림차순 정렬로 결과 출력
 */

SELECT
    HD.DEPT_ID,
    HD.DEPT_NAME_EN,
    ROUND(AVG(HE.SAL), 0) AS AVG_SAL
FROM
    HR_DEPARTMENT HD
        INNER JOIN HR_EMPLOYEES HE ON HD.DEPT_ID = HE.DEPT_ID
GROUP BY
    HD.DEPT_ID, HD.DEPT_NAME_EN
ORDER BY
    AVG_SAL DESC;
