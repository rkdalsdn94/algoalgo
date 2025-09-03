# 프로그래머스 SQL - Lv2 - 업그레이드 된 아이템 구하기 - SELECT 문제
/**
  SELECT 문제

  [핵심 아이디어]
    RARE 아이템을 부모로 가지는 모든 직계 자식 아이템들을 찾는 문제

  [풀이 과정]
    1. ITEM_INFO에서 RARITY가 'RARE'인 아이템들을 식별
    2. ITEM_TREE를 통해 해당 아이템들이 부모가 되는 업그레이드 관계를 찾음
    3. 업그레이드된 아이템들의 상세 정보를 ITEM_INFO에서 가져옴
    4. ITEM_ID 기준 내림차순 정렬
 */

SELECT
    I2.ITEM_ID,
    I2.ITEM_NAME,
    I2.RARITY
FROM ITEM_INFO AS I1
JOIN ITEM_TREE AS T ON I1.ITEM_ID = T.PARENT_ITEM_ID
JOIN ITEM_INFO AS I2 ON T.ITEM_ID = I2.ITEM_ID
WHERE I1.RARITY = 'RARE'
ORDER BY I2.ITEM_ID DESC;
