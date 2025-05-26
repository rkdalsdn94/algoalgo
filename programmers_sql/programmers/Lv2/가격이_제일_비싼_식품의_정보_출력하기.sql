# 프로그래머스 sql - Lv2 - 가격이 제일 비싼 식품의 정보 출력하기 - MAX, 서브쿼리 문제
/**
  MAX, 서브쿼리 문제

  MAX 함수와 서브 쿼리를 이용해서 풀 수 있다.
  또한, 조금 더 생각해보면 문제 분류에는 포함되지 않지만 ORDER BY 와 LIMIT 절을 이용해서 풀 수 있다
 */

-- 서브쿼리 사용
SELECT * FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE)
               FROM FOOD_PRODUCT);

-- ORDER BY + LIMIT 사용
SELECT * FROM FOOD_PRODUCT
ORDER BY PRICE DESC LIMIT 1;
