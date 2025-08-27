# 프로그래머스 sql - Lv2 - 특정 물고기를 잡은 총 수 구하기 - SELECT 문제
/**
    SELECT 문제

    [핵심 아이디어]:
    - FISH_NAME_INFO 테이블에서 'BASS'와 'SNAPPER'에 해당하는 FISH_TYPE을 찾아
    - FISH_INFO 테이블에서 해당 물고기들의 총 개수를 구한다

    [풀이 과정]:
    1. FISH_INFO와 FISH_NAME_INFO 테이블을 FISH_TYPE으로 조인
    2. WHERE 조건으로 FISH_NAME이 'BASS' 또는 'SNAPPER'인 레코드만 필터링
    3. COUNT(*)로 총 개수를 계산하여 FISH_COUNT로 출력
 */

SELECT
    COUNT(*) AS FISH_COUNT
FROM FISH_INFO FI
    JOIN FISH_NAME_INFO FNI ON FI.FISH_TYPE = FNI.FISH_TYPE
WHERE FNI.FISH_NAME IN ('BASS', 'SNAPPER');
