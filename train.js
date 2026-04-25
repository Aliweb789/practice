
/* E-Task:
    Savol: shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
    Masalan: getReverse("hello") return qilsin "olleh"
*/
//masalaning yechimi"
    const getReverse = function(text) {
        const result = text.split("").reverse().join("")
        console.log(result)
    }
getReverse("hello")
















/* D-TASK:
    Savol: shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiniga tegishli birinchi indexni qaytarsin. 
    Masalan: getHighestindex([5, 21, 12, 21, 8]) return qiladi 1 sonini
*/

//masalaning yechimi:
/*    const getHighestindex1 = function(arr) {
        let max = arr[0];
        let max_index = 0;
        for (let i = 1; i < arr.length; i++) {
            if(arr[i] > max) {
                max = arr[i];
                max_index = i;
            }
        }
        console.log("solution is : " + max_index);
    }

    getHighestindex1([5, 21, 12, 21, 8])

    const getHighestindex2 = function(arr) {
        max_numb = Math.max(...arr);
        max_index = arr.indexOf(max_numb);
        console.log("solution is : " + max_index);
    }

    getHighestindex2([5, 21, 12, 22, 8])

*/
/* C-TASK:
    Savol: Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
    Masalan: checkContent("mitgroup", "gmtiprou") return qiladi true;
*/

//masalaning yechimi:
/*
const checkContent = function (text1, text2) {
    let count = 0;
    for (const letter of text1) {
        if (text2.includes(letter)) count++
    }
    bool_result = (count === text1.length) && (count === text2.length);
    console.log("solution is : " + bool_result);
}
checkContent("mitgroup", "gmtiprou")
*/
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

