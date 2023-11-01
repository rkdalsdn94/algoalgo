# 프로그래미스 - Lv1 - 12세 이하인 여자 환자 목록 출력하기
/**
  문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/132201

  아래 두 풀이 모두 정답처리 된다.

  COALESCE, IFNULL 차이는 다음과 같다.
  IFNULL은 두 개의 인수만을 받아들이고, 첫 번째 인수가 NULL이 아니면 두 번째 인수를 반환하는 반면,
  COALESCE는 두 개 이상의 인수를 받아들이고, 첫 번째로 NULL이 아닌 값을 반환합니다.
  이러한 차이점으로 인해 COALESCE는 다중 인수를 처리할 때 유용하다.

  또한, ORDER BY 의 기본 값은 오름차순(ASC) 이므로
    age를 내림차순(DESC)으로 정렬한 뒤 pt_name만 적어두면 ASC으로 잘 정렬된다.
 */

SELECT pt_name, pt_no, gend_cd, age, COALESCE(tlno, 'NONE')
FROM patient WHERE age <= 12 AND gend_cd = 'w'
ORDER BY age DESC, pt_name;

-- SELECT pt_name, pt_no, gend_cd, age, IFNULL(tlno, 'NONE')
-- FROM patient WHERE age <= 12 AND gend_cd = 'w'
-- ORDER BY age DESC, pt_name;
