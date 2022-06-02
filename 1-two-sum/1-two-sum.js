/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
   let hs = {}
   for(let [index, num] of nums.entries() ){
       if(hs[num] !== undefined) return [hs[num], index]
       hs[target - num] = index
   }
};