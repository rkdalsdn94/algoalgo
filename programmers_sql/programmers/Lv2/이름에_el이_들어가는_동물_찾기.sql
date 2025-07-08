# 프로그래머스 sql - Lv2 - 이름에 el이 들어가는 동물 찾기 - String, Date 문제
/**
    String, Date 문제

    name 컬럼에 'el'이 들어가는 동물의 이름과 ID를 찾는 문제이다.
    name 컬럼에서 'el'이 들어가는 동물의 이름과 ID를 찾기 위해서는 LIKE 연산자를 사용해야 한다.
    또한, ANIMAL_TYPE이 'Dog'인 동물만 찾기 위해서는 WHERE 절을 사용해야 한다.
    마지막으로, 이름을 오름차순으로 정렬하기 위해 ORDER BY 절을 사용해야 한다.
 */

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE name LIKE '%el%'
  AND ANIMAL_TYPE = 'Dog'
ORDER BY name;
