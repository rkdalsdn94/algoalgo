/*
파이썬이랑 똑같이 풀었다. 근데 아직 뭔가 어색하다..
뭔가 좀 더 연습해야 될거 같다.
*/

function solution(board, moves) {
  var answer = 0;
  let temp = [];
  let move = [];

  for (let x of moves) {
    move.push(x - 1);
  }
  // console.log(move);

  for (const i of move) {
    for (const j of board) {
      if (j[i] != 0) {
        temp.push(j[i]);
        j[i] = 0;
        // console.log(temp[temp.length - 1], temp[temp.length - 2], temp);

        if (
          temp.length >= 2 &&
          temp[temp.length - 1] == temp[temp.length - 2]
        ) {
          answer += 2;
          temp.pop();
          temp.pop();
        }
        break;
      }
    }
  }

  return answer;
}

console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
); // 4
