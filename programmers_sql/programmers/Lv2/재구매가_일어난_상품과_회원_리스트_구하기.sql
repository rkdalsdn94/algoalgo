# 프로그래미스 - Lv2 - 재구매가 일어난 상품과 회원 리스트 구하기 - SELECT 문제
/**
  GROUP BY와 HAVING 절을 이용해서 문제를 풀면 된다.

  MySQL에서 그루핑을 할 때 Group By를 이용하면 된다. (복수개의 컬럼도 그루핑 할 수 있음)
  따라서, user_id와 product_id를 그루핑하고,
  count(*) 함수를 사용해 중복되는 값(재구매)이 있는 경우를 출력하면 된다.

  아래와 같이 예제로 사용하기 위해 데이터베이스와 테이블과 row를 만든 뒤
  실행할 쿼리에서 주석되어 있는 부분을 해제한 뒤 쿼리를 실행하면 쉽게 이해할 수 있다.

    CREATE DATABASE sql_quiz_solved;
    USE sql_quiz_solved;
    CREATE TABLE online_sale (
        online_sale_id  INTEGER  NOT NULL,
        user_id     INTEGER NOT NULL,
        product_id     INTEGER NOT NULL,
        sales_amount     INTEGER NOT NULL,
        sales_date     DATE NOT NULL
    );
    INSERT INTO
        online_sale
    VALUES
        (1,	1,	3,	2,	'2022-02-25'),
        (2,	1,	4,	1,	'2022-03-01'),
        (4,	2,	4,	2,	'2022-03-12'),
        (3,	1,	3,	3,	'2022-03-31'),
        (5,	3,	5,	1,	'2022-04-03'),
        (6,	2,	4,	1,	'2022-04-06'),
        (2,	1,	4,	2,	'2022-05-11');
 */

SELECT user_id, product_id -- , count(*) -- 여기 부분 주석 해제한 뒤 쿼리를 실행하면 쉽게 이해할 수 있다.
FROM online_sale
GROUP BY user_id, product_id
HAVING COUNT(*) > 1
ORDER BY user_id, product_id DESC;
