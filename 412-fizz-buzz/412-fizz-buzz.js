/**
 * @param {number} n
 * @return {string[]}
 */
const fizzBuzz =(n)=> {
    const storage = []
    while(n){
        if(n % 3 === 0 & n % 5 === 0){
            storage[n] = "FizzBuzz";
        }else if(n % 3 === 0 ){
            storage[n] = "Fizz";
        }else if(n % 5 === 0) {
            storage[n] = "Buzz";
        }else{
            storage[n] = `${n}`
        }
        n--
    }
    storage.shift()
    return storage
};