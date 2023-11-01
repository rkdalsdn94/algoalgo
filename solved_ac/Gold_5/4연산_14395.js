// 백준 - 골드5 - 4연산 - (Python 파일의 풀이 참고)

const fs = require('fs');
let [s, t] = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);

function solve(s, t) {
  let queue = [[s, '']];
  const maximum = 10 ** 9 + 1;
  let result = -1;
  let checked = new Set();

  if (s === t) {
    return 0;
  }

  while (queue.length > 0) {
    let [a, res] = queue.shift();

    if (a === t) {
      return res;
    }

    let nx = a * a;
    if (0 <= nx < maximum && !checked.has(nx)) {
      queue.push([nx, res + '*']);
      checked.add(nx);
    }

    nx = a + a;
    if (0 <= nx < maximum && !checked.has(nx)) {
      queue.push([nx, res + '+']);
      checked.add(nx);
    }

    nx = a / a;
    if (!checked.has(nx)) {
      queue.push([nx, res + '/']);
      checked.add(nx);
    }
  }

  return -1;
}

let res = solve(s, t);
console.log(res);
