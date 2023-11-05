# 프로그래머스 - Lv1 - 조건에 맞는 도서 리스트 출력하기 - 단순 SELECT 문제
/**
  문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/144853

  조회하고자 하는 published_date 컬럼을 DATE_FORMAT 내장 함수를 이용해 출력 형식과 맞추고
  WHERE절로 년도와 카테고리만 비교하면 되니까 연도를 비교할 땐 YEAR 함수를 이용했다.
  위와 같이 조회된 쿼리에서 published_date컬럼을 기준으로 오름차순으로 출력하기 위해 ORDER BY를 이용했다.
 */

SELECT book_id, DATE_FORMAT(published_date, '%Y-%m-%d')
FROM book
WHERE YEAR(published_date) = 2021 AND category = '인문'
ORDER BY published_date DESC;
