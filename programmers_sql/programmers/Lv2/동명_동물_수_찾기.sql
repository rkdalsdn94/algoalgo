# 프로그래머스 sql - Lv2 - 동명 동물 수 찾기 - group by 문제
/**
  group by 문제

  group by 를 이용해서 문제를 푸는데 같은 이름이 1 이상인 행만 출력해야 된다.
  즉 group by 내에서 조건 절이 필요하고, group by에서 조건을 쓰려면 having 절을 사용하면 된다.
 */

SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME;
