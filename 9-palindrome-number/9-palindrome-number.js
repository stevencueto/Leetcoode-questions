/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = (x) => {
    const initialOne = x.toString().split('');
    const comparePalidrome = x.toString().split('').reverse();
    const storage = [];
    for(let i =0; i < initialOne.length; i++){
        if (initialOne[i] === (comparePalidrome[i]))
        storage.push(initialOne[i])
    }
    if(storage.length === initialOne.length){
        return true
    }else{
        return false
    }
};
