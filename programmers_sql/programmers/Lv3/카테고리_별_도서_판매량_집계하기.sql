# 프로그래머스 sql - Lv3 - 카테고리 별 도서 판매량 집계하기 - GROUP BY 문제
/**
  GROUP BY 문제

[핵심 아이디어]
    1. BOOK과 BOOK_SALES 테이블을 BOOK_ID로 조인하여 카테고리 정보와 판매 정보 결합
    2. 2022년 1월 판매 데이터만 필터링 (YEAR, MONTH 함수 활용)
    3. 카테고리별로 그룹화하여 판매량 합산 (GROUP BY + SUM)
    4. 카테고리명 기준 오름차순 정렬

[풀이 과정]
    1. BOOK과 BOOK_SALES를 BOOK_ID로 조인
    2. WHERE 절로 2022년 1월 데이터만 필터링
    3. GROUP BY로 카테고리별 판매량 합산
    4. ORDER BY로 카테고리명 오름차순 정렬
 */

SELECT
    B.CATEGORY,
    SUM(BS.SALES) AS TOTAL_SALES
FROM
    BOOK B
        INNER JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
WHERE
    YEAR(BS.SALES_DATE) = 2022
  AND MONTH(BS.SALES_DATE) = 1
GROUP BY
    B.CATEGORY
ORDER BY
    B.CATEGORY ASC;
