# 프로그래머스 sql - Lv2 - 조건에 맞는 도서와 저자 리스트 출력하기 - JOIN 문제
/**
    JOIN 문제

    [핵심 아이디어]
        1. BOOK 테이블과 AUTHOR 테이블을 INNER JOIN하여 도서와 저자 정보를 결합
        2. WHERE 절로 특정 카테고리('경제')의 도서만 필터링
        3. DATE_FORMAT 함수를 사용하여 PUBLISHED_DATE를 요구 형식으로 변환
        4. ORDER BY 절로 PUBLISHED_DATE 기준 오름차순 정렬

    [풀이 과정]
        1. BOOK 테이블에서 필요한 컬럼(BOOK_ID, PUBLISHED_DATE) 선택
        2. AUTHOR 테이블과 AUTHOR_ID를 기준으로 INNER JOIN 수행
        3. AUTHOR 테이블에서 AUTHOR_NAME 컬럼 선택
        4. WHERE 절로 CATEGORY가 '경제'인 도서만 필터링
        5. DATE_FORMAT 함수로 PUBLISHED_DATE를 'YYYY-MM-DD' 형식으로 변환
        6. ORDER BY 절로 PUBLISHED_DATE 기준 오름차순 정렬하여 최종 결과 출력
 */

SELECT
    B.BOOK_ID,
    A.AUTHOR_NAME,
    DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B
    JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE B.CATEGORY = '경제'
ORDER BY B.PUBLISHED_DATE;
