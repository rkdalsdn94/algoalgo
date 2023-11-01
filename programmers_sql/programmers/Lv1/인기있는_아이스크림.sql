# 프로그래머스 - Lv1 - 인기있는 아이스크림 - SELECT 문제
/**
  문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/133024

  SELECT 후 정렬만 하면 되는 간단한 문제이다.
 */

SELECT flavor
FROM first_half
ORDER BY total_order DESC, shipment_id
