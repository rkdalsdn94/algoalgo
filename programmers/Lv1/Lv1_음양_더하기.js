/*
너무 간단해서 따로 코드 설명은 안하는데 다른 사람 풀이를 가져와봤다.

return absolutes.reduce((acc, val, i) => acc + (val * (signs[i] ? 1 : -1)), 0);
위 처럼 아예 한줄로 가능하다..
훨씬 간결하고 가독성 좋게 코드를 짤 수 있다...

JS를 다시 공부해야 될거 같다.
*/

function solution(absolutes, signs) {
  let answer = 0;
  const temp = absolutes.map(function (e, i) {
    // console.log(e, i);
    return [e, signs[i]];
  });
  // console.log(temp);

  for (i of temp) {
    // console.log(i)
    answer += i[1] ? i[0] : -i[0];
  }

  return answer;
}
