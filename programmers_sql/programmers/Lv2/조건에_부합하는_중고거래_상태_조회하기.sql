# 프로그래머스SQL - Lv2 - 조건에 부합하는 중고거래 상태 조회하기 - SELECT 문제
/**
  문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/164672

  단순한 SELECT 문제이다.
  status 컬럼의 값에 따라 '판매중', '예약중', '거래완료'으로 잘 변경하면 단순한 SELECT 조회 문제다.
 */

SELECT
    board_id,
    writer_id,
    title,
    price,
    CASE
        WHEN status = 'SALE' THEN '판매중'
        WHEN status = 'RESERVED' THEN '예약중'
        WHEN status = 'DONE' THEN '거래완료'
    END AS status
FROM used_goods_board
WHERE DATE_FORMAT(created_date, '%Y-%m-%d') = '2022-10-05'
ORDER BY board_id DESC
