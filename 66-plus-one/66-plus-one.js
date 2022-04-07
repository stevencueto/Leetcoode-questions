/**
 * @param {number[]} digits
 * @return {number[]}
 */
const plusOne = (digits) => {
    let indx = digits.length - 1;
    while(indx >= 0){
        digits[indx] += 1;
        if(digits[indx] > 9){
            digits[indx] = 0;
            indx--;
            if(indx < 0){
                digits.unshift(1);
            }
        }else{
            break;
        }
    }
    return digits;
};