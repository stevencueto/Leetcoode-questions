/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = (nums1, nums2)=> {
    const newArr = nums1.concat(nums2)
    newArr.sort((a,b)=> a -b)
    if(newArr.length % 2 === 1){
        return newArr[Math.floor(newArr.length / 2)]
    }else{
        const result1 = newArr[(newArr.length / 2) - 1]
        const result2 = newArr[Math.ceil(newArr.length / 2)]
        return (result1 + result2) / 2
    }
};