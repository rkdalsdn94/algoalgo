# 프로그래머스SQL - Lv1 - 조건에 부합하는 중고거래 댓글 조회하기 - SELECT 문제
/**
  간단한 JOIN과 DATE_FORMAT으로 DATE의 포맷 형식을 조심하고,
  '테이블에서 2022년 10월에 작성된' 이라고 되어 있는데,
  별 생각없이 `USED_GOODS_REPLY`테이블의 created_date 컬럼을 WHERE 절에서 사용했다가 틀렸었다.

  MySQL에서 JOIN의 기본 값은 INNER JOIN으로 되어 있어어서 INNER를 생략하고 JOIN만 사용해도 상관 없다.
 */


SELECT
    a.title,
    a.board_id,
    b.reply_id,
    b.writer_id,
    b.contents,
    DATE_FORMAT(b.created_date, '%Y-%m-%d')
FROM used_goods_board a
JOIN used_goods_reply b
ON a.board_id = b.board_id
WHERE DATE_FORMAT(a.created_date, '%Y-%m') = '2022-10' -- 여기서 board 테이블을 기준으로 조건을 달아야 됨
ORDER BY b.created_date, a.title;
