/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length !== t.length)return false
    const sHs = {}
    const tHs = {}
    for(let i = 0; i < s.length; i++){
        sHs[s[i]] =  sHs[s[i]] + 1 || 1
        tHs[t[i]] =  tHs[t[i]] + 1 || 1
    }
    for(const key in sHs){
        if(sHs[key] !== tHs[key]) return false
    }
    
    return true
};

//it has a constant time and space complexity
//but it can be even more efficient, by using one hashmap

