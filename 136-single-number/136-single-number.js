/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    const hash ={}
    for(const num of nums){
         hash[num] = hash[num] + 1 || 1
    }
    
    for(const key in hash){
        if(hash[key] === 1) return key
    }
};