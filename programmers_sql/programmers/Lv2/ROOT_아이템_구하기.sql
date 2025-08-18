# 프로그래머스 sql - Lv2 - ROOT 아이템 구하기 - IS NULL 문제
/**
  IS NULL 문제

  [핵심 아이디어]
    1. ITEM_TREE 테이블에서 PARENT_ITEM_ID가 NULL인 루트 아이템을 찾기
    2. ITEM_INFO 테이블과 JOIN하여 아이템 이름을 가져오기
    3. IS NULL 조건을 사용하여 PARENT_ITEM_ID가 NULL인 조건 필터링
    4. ITEM_ID 기준으로 오름차순 정렬

  [풀이 과정]
    1. ITEM_TREE 테이블에서 ITEM_ID와 PARENT_ITEM_ID를 선택
    2. ITEM_INFO 테이블과 INNER JOIN하여 ITEM_NAME을 가져옴
    3. WHERE 절에서 IS NULL 조건으로 PARENT_ITEM_ID가 NULL인 루트 아이템만 필터링
    4. ORDER BY로 ITEM_ID 기준 오름차순 정렬하여 최종 결과 출력
 */

SELECT
    IT.ITEM_ID,
    II.ITEM_NAME
FROM ITEM_TREE IT
    JOIN ITEM_INFO II ON IT.ITEM_ID = II.ITEM_ID
WHERE IT.PARENT_ITEM_ID IS NULL
ORDER BY IT.ITEM_ID;
