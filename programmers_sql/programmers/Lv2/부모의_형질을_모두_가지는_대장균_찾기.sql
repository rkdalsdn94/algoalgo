# 프로그래머스 SQL - Lv2 - 부모의 형질을 모두 가지는 대장균 찾기 - SELECT 문제
/**
  SELCET 문제

  [핵심 아이디어]
    GENOTYPE을 2진수로 해석하여 각 비트가 형질을 나타냄.
    부모의 형질을 모두 보유 = (A.GENOTYPE & B.GENOTYPE) = B.GENOTYPE

  [풀이 과정]
    1. SELF JOIN으로 자식(A)과 부모(B) 개체 연결 (A.PARENT_ID = B.ID)
    2. 비트 AND 연산으로 자식이 부모의 모든 형질을 보유하는지 확인
    3. 조건: A.GENOTYPE & B.GENOTYPE = B.GENOTYPE
    4. 결과를 ID 기준 오름차순 정렬
*/

SELECT A.ID, A.GENOTYPE, B.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA A JOIN ECOLI_DATA B ON A.PARENT_ID = B.ID
WHERE A.GENOTYPE & B.GENOTYPE = B.GENOTYPE
ORDER BY A.ID
