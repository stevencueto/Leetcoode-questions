/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const initialOne = x.toString().split('');
    const comparePalidrome = x.toString().split('').reverse();
    const whatEver = [];
    for(let i =0; i < initialOne.length; i++){
        if (initialOne[i] === (comparePalidrome[i]))
        whatEver.push(initialOne[i])
    }
    if(whatEver.length === initialOne.length){
        return true
    }else{
        return false
    }
};
