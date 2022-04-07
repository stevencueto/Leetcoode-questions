/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const gSum = (nums.length * (nums.length + 1)) / 2;
    const totalSum = nums.reduce((acc, el) => acc + el, 0);
    
    return gSum - totalSum
};