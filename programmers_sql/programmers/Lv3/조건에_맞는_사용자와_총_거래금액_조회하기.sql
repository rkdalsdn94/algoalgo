# 프로그래머스 SQL - Lv3 - 조건에 맞는 사용자와 총 거래금액 조회하기 - JOIN, GROUP BY 문제
/**
JOIN, GROUP BY 조회

[핵심 아이디어]
    1. 완료된 거래(STATUS='DONE')를 작성자별로 그룹화
    2. 각 작성자의 총 거래금액을 SUM으로 계산
    3. HAVING으로 70만원 이상 필터링
    4. USER 테이블과 조인하여 닉네임 가져오기

[풀이 과정]
    1. BOARD 테이블에서 완료된 거래만 필터링하고 작성자별 총액 계산
    2. 총액이 700000 이상인 작성자만 선택
    3. USER 테이블과 조인하여 사용자 정보 결합
    4. 총거래금액 기준 오름차순 정렬
 */

SELECT
    U.USER_ID,
    U.NICKNAME,
    SUM(B.PRICE) AS TOTAL_SALES
FROM
    USED_GOODS_BOARD B
        INNER JOIN USED_GOODS_USER U
                   ON B.WRITER_ID = U.USER_ID
WHERE
    B.STATUS = 'DONE'  -- 완료된 거래만 포함
GROUP BY
    U.USER_ID, U.NICKNAME  -- 사용자별로 그룹화
HAVING
    SUM(B.PRICE) >= 700000  -- 총 거래금액이 70만원 이상
ORDER BY
    TOTAL_SALES ASC;  -- 총거래금액 오름차순 정렬
