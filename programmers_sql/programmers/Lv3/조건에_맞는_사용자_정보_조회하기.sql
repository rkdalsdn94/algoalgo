# 프로그래머스 SQL - Lv3 - 조건에 맞는 사용자 정보 조회하기 - String, Date 문제
/**
String, Date 문제

[핵심 아이디어]
    1. GROUP BY + HAVING으로 게시글 3건 이상 작성한 사용자 식별
    2. JOIN을 통해 사용자 상세 정보 조회
    3. CONCAT으로 주소 결합, SUBSTR로 전화번호 포맷팅

[풀이 과정]
    1. 서브쿼리에서 게시글 3건 이상 작성한 WRITER_ID 추출
    2. 메인 쿼리에서 해당 사용자의 정보를 USED_GOODS_USER에서 조회
    3. 전체 주소를 CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2)로 생성
    4. 전화번호를 SUBSTR로 분할하여 'XXX-XXXX-XXXX' 형식으로 포맷팅
    5. USER_ID 기준 내림차순 정렬
 */

SELECT
    U.USER_ID,
    U.NICKNAME AS NICKNAME,
    CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) AS '전체주소',
    CONCAT(SUBSTR(U.TLNO, 1, 3), '-', SUBSTR(U.TLNO, 4, 4), '-', SUBSTR(U.TLNO, 8, 4)) AS '전화번호'
FROM USED_GOODS_USER U
WHERE U.USER_ID IN (
    -- 게시글을 3건 이상 등록한 사용자의 ID 조회
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(*) >= 3
)
ORDER BY U.USER_ID DESC;
