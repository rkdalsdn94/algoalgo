// 풀이는 python 파일을 보면 된다.

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = +input[0];
const n_list = input[1].split(' ').map(Number);

const stack = [];
const res = new Array(n).fill(-1);

for (let i = 0; i < n; i++) {
    while (stack.length > 0 && stack[stack.length - 1][1] < n_list[i]) {
        const [idx, value] = stack.pop();
        res[idx] = n_list[i];
    }
    stack.push([i, n_list[i]])
}

console.log(...res);
