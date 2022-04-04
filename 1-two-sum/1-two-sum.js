/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
   let memory = {}
   for(let [index, num] of nums.entries() ){
       if(memory[num] !== undefined) return [memory[num], index]
       memory[target - num] = index
   }
};