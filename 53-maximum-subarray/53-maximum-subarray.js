/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = (nums)=> {
    let results = nums[0]
    for (let i = 1; i < nums.length; i++){
        nums[i] = Math.max(nums[i], nums[i] + nums[i -1])
        results = Math.max(results, nums[i])
    }
    return results
};

//make a for loop and a variable called results; results is going to return the maximun sum of the array, use a built in function called Math.max to determin whether nums[i] is larger then my result and then modify the result variable, return the result at the end of the forloop