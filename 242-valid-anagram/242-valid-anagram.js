/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(!s || !t)return false
    let x = s.split('').sort().join('');
    let y = t.split('').sort().join('');
    console.log(x, y)
    
    return y === x ? true  : false
    
};