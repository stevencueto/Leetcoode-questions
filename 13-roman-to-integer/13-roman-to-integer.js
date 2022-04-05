/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const romanNumber = {
        I: 1,
        V: 5,
        X: 10,
        L:50,
        C:100,
        D:500,
        M:1000,
    }
    let finalValue = 0;
    for(let i =0; i < s.length; i++){
       if (s[i] === "I" && s[i + 1] === "V"){
           finalValue += 4;
           console.log(finalValue)
       }else if(s[i] === "I" && s[i + 1] === "X"){
           finalValue += 9;
       }else if(s[i] === "X" && s[i + 1] === "L"){
           finalValue += 40;
       }else if(s[i] === "X" && s[i + 1] === "C"){
            finalValue += 90;
       }else if(s[i] === "C" && s[i + 1] === "D"){
            finalValue += 400;
       }else if(s[i] === "C" && s[i + 1] === "M"){
            finalValue += 900;
       }else if ((s[i] === "V" && s[i - 1] === "I") || (s[i] === "X" && s[i - 1] === "I") || (s[i] === "L" && s[i - 1] === "X") || (s[i] === "C" && s[i - 1] === "X") || (s[i] === "D" && s[i - 1] === "C") || (s[i] === "M" && s[i - 1] === "C")){
            finalValue += 0
       }else{
            finalValue += romanNumber[s[i]];
       }
    }

    return finalValue;
    
};
