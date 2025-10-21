# 프로그래머스 SQL - Lv3 - 대장균의 크기에 따라 분류하기 1 - SELECT 문제
/**
  SELECT 문제

  [핵심 아이디어]
    CASE문을 사용하여 SIZE_OF_COLONY 값에 따라 'LOW', 'MEDIUM', 'HIGH'로 분류
    ORDER BY 절을 사용하여 ID 기준 오름차순 정렬

  [풀이 과정]
    1. ECOLI_DATA 테이블에서 ID와 SIZE_OF_COLONY 컬럼 선택
    2. CASE문을 사용하여 SIZE_OF_COLONY 값에 따라 크기 분류:
       - 100 이하: 'LOW'
       - 101~1000: 'MEDIUM'
       - 1001 이상: 'HIGH'
    3. 결과를 ID 기준으로 오름차순 정렬
 */

SELECT
    ID,
    CASE
        WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
        WHEN SIZE_OF_COLONY <= 1000 THEN 'MEDIUM'
        ELSE 'HIGH'
    END AS SIZE
FROM ECOLI_DATA
ORDER BY ID ASC;
