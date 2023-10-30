// 백준 - 브론즈3 - 약수 구하기 - 2501
/**
 * python 파일의 풀이 참고
 */

let fs = require('fs');
let [A, B] = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);

let arr = [];

for(let i = 1; i <= A; i++) {
    if(A % i == 0) {
        arr.push(i)
    }

    if(arr.length == B) {
        console.log(arr[B - 1])
        break;
    }
}

if(arr.length < B) {
    console.log(0)
}
