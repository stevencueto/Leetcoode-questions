/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
const merge = (nums1, m, nums2, n)=> {
    let first = m - 1;
    let second = n - 1;
    let indx = n + m - 1;
    
    while(second >= 0){
        let arr1 = nums1[first]
        let arr2 = nums2[second]
        
        if(arr1 > arr2){
            nums1[indx] = arr1
            indx--
            first--
        }else{
            nums1[indx] = arr2;
            indx--
            second--
        }
    }
};