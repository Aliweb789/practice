
/* C-TASK:
    Savol: Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
    Masalan: checkContent("mitgroup", "gmtiprou") return qiladi true;
*/

//masalaning yechimi:
const checkContent = function (text1, text2) {
    let count = 0;
    for (const letter of text1) {
        if (text2.includes(letter)) count++
    }
    bool_result = (count === text1.length) && (count === text2.length);
    console.log("solution is : " + bool_result);
}
checkContent("mitgroup", "gmtiprou")

/* B-TASK:
    Savol: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// //masalaning yechimi:
// const countDigits = function(text) {
//     let count = 0;
//     for (const isNumber of text) {
//         // console.log(typeof isNumber);
//         if(isNumber % 1 == 0) count++
//     }
//     console.log("solution is : " + count);
// }

// countDigits("ad2a54y79we87t450sfgb9")




/* A-TASK:
    Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

//masalaning yechimi:
/*
const countLetter = function(a, b) {
    let count = 0;
    for (const letter of b) {
        console.log(letter)
        if(letter === a) {
            count++
        }
    }
    console.log("solution: ", count + " same letters")
}

countLetter("e", "engineer") //==>solution: 3

*/

