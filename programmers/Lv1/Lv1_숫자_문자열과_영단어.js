/*
전에 파이썬으로 풀었던 방식대로 풀었다...
다른 사람 풀이 보니까 아래와 같이 푼 사람이 있었다.

function solution(s) {
    let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    var answer = s;

    for(let i=0; i< numbers.length; i++) {
        let arr = answer.split(numbers[i]);
        answer = arr.join(i);
    }

    return Number(answer);
}

js를 잘 못 다루는 느낌도 있고, 연습을 좀 더 해야될거 같다고 느꼈다.
*/

function solution(s) {
  var answer = '';
  word_dic = {
    zero: '0',
    one: '1',
    two: '2',
    three: '3',
    four: '4',
    five: '5',
    six: '6',
    seven: '7',
    eight: '8',
    nine: '9',
  };
  let word = '';

  for (var i of s) {
    // console.log(i, word)
    if (!isNaN(i)) {
      answer += i;
      // console.log(i);
    } else {
      // console.log(i);
      word += i;
      // console.log(word);

      if (word in word_dic) {
        // console.log('test');
        answer += word_dic[word];
        word = '';
      }
    }
    // console.log(answer);
  }

  return Number(answer);
}

console.log(solution('one4seveneight')); // 1478
console.log(solution('23four5six7')); // 234567
console.log(solution('2three45sixseven')); // 234567
console.log(solution('123')); // 123
