# 프로그래머스 - Lv1 - 이름이 없는 동물의 아이디 - IS NULL 문제
/**
  IS NULL을 활용화면 되는 단순한 문제
 */

SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NULL ORDER BY ANIMAL_ID;
