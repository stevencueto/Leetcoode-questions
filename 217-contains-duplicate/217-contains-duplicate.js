/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate =(nums)=> {
    const hs = {}
    for(const num of nums){
        if(hs[num] !== undefined) return true
        hs[num] = num
    }
    return false
};