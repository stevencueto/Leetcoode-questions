/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
     s = s.replace(/[^a-z0-9]/gi, '')
    console.log(s)
    let left = 0;
    let right = s.length - 1
    while(left < right){
        if(s[left].toLowerCase() !== s[right].toLowerCase()) return false
        left++
        right--
    }
    return true
};

/*make a variable to with no special characters which is a string using regular expressions,
create a left index variable to keep track of the left pointer
create a right index variable to keep track of the right index
create a while loop to se if the pointers are equal, if they are keep looping, if they are not, break out of the while loop and return false
make sure .toLowerCase() the characters
*/