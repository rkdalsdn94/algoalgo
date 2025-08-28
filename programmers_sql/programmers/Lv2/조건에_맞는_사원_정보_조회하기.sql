# 프로그래머스 sql - Lv2 - 조건에 맞는 사원 정보 조회하기 - GROUP BY 문제
/**
    GROUP BY 문제

    [핵심 아이디어]
        2022년 상반기와 하반기 평가 점수를 합산하여 최고점을 구한 후, 해당 점수를 받은 사원 정보를 조회

    [풀이 과정]
        1. HR_GRADE 테이블에서 2022년 데이터만 필터링
        2. 각 사원별로 상반기(1)와 하반기(2) 점수를 합산 (GROUP BY + SUM 사용)
        3. 합산된 점수 중 최댓값을 구함 (서브쿼리에서 MAX 사용)
        4. 최댓값과 같은 점수를 받은 사원들을 찾아서 HR_EMPLOYEES와 조인
        5. 필요한 컬럼들(점수, 사번, 성명, 직책, 이메일)을 선택하여 출력
 */

SELECT
    annual_scores.SCORE,
    annual_scores.EMP_NO,
    e.EMP_NAME,
    e.POSITION,
    e.EMAIL
FROM (
         -- 각 사원별 2022년 연간 점수(상반기 + 하반기) 계산
         SELECT
             EMP_NO,
             SUM(SCORE) AS SCORE
         FROM HR_GRADE
         WHERE YEAR = 2022
         GROUP BY EMP_NO
     ) annual_scores
         JOIN HR_EMPLOYEES e ON annual_scores.EMP_NO = e.EMP_NO
WHERE annual_scores.SCORE = (
    -- 2022년 연간 최고 점수 구하기
    SELECT MAX(total_score.SCORE)
    FROM (
             SELECT
                 EMP_NO,
                 SUM(SCORE) AS SCORE
             FROM HR_GRADE
             WHERE YEAR = 2022
             GROUP BY EMP_NO
         ) total_score
);
