/**
 * @param {number} n
 * @return {string[]}
 */
const fizzBuzz =(n)=> {
    const storage = []
    const nums = Array.from(Array(n + 1).keys())
    for(let [index, num] of nums.entries()){
        if(num % 3 === 0 & num % 5 === 0){
            storage[index] = "FizzBuzz";
        }else if(num % 3 === 0 ){
            storage[index] = "Fizz";
        }else if(num % 5 === 0) {
            storage[index] = "Buzz";
        }else{
            storage[index] = `${num}`
        }
    }
    storage.shift()
    return storage
};