/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const search = (nums, target) => {
    let left = 0,
        right = nums.length - 1
    while(left <= right){
        let mid = left + Math.floor( (right - left) /2 )
        if(nums[mid] === target){
            return mid
        }else if (nums[mid] < target){
            left = mid + 1
        }else{
            right = mid - 1
        }
    }
    return -1
};

/*
we're doing it by Binary Search, so we have 3 pointers left, irght and middle, and we look to se if the target is more than middle pointer we increment left else we decrement right, until we find our target or our right is equal to our left or more, then we return -1
*/