function solution(nums) {

    var answer = 0;
    let temp = new Set();
    
    for(const number of nums){
        temp.add(number);
    }
    
    if( temp.size < nums.length/2){
        return temp.size;
    } else { 
        return nums.length/2;
    }
    
}

console.log(solution([3,1,2,3])) // 2
console.log(solution([3,3,3,2,2,4])) // 3
console.log(solution([3,3,3,2,2,2])) // 2