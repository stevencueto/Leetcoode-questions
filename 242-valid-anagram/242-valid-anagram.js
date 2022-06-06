/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length !== t.length)return false
    let x = s.split('').sort().join('');
    let y = t.split('').sort().join('');
    
    return y === x ? true  : false
    
};