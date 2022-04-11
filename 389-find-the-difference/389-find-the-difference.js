/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
const findTheDifference =(s, t) =>{
    const hash = {}
    for(let i = 0; i < s.length; i++){
        hash[s[i]] = (hash[s[i]] | 0) + 1
    }
    for(let i = 0; i < t.length; i++){
        if(hash[t[i]] !== undefined && hash[t[i]] > 0){
            hash[t[i]]--
        }else{
            return t[i]
        }
    }
};