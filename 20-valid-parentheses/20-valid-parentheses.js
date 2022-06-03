/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const hs = {
        '{': '}',
        '[' : ']',
        '(':')'
    }
    
    const heap = []
    
    for (let char of s){
        if(hs[char]){
            heap.push(hs[char])
        }else if( heap.pop() !== char){
           return false
        }
    }
    
    return (!heap.length)
};
