/* L-TASK
    Sunday function yozing, u string qabul qilsin va string ichidagi hamma sozlarni chappasiga yozib va sozlarni ketma-ketligini buzmasdan stringni qaytarsin.
    MASALAN: reverseSentence("we like coding!") return "ew ekil gnidoc"
*/
const reverseSentence = (str) => {
    const arr = str.split(" ")
    console.log(arr);
    
    const new_arr = arr.map(value => {
       return value.split('').reverse().join('')
    })
    console.log(new_arr.join(" "));
    
}
reverseSentence("we like coding!")










/*J-TASK
    Shunday function yozing, u paramentridagi array ichida eng kop takrorlangan raqamni topin qaytarsin. 
    MASALAN: majorityElement([1, 2, 3, 4, 5, 6, 4, 3, 4]) return 4
*/
//     function majorityElement(arr) {
//     const counts = {};
    
//     for (let num of arr) {
//         counts[num] = (counts[num] || 0) + 1;
//     }
    
//     let maxCount = 0, result = null;
    
//     for (let [num, count] of Object.entries(counts)) {
//         if (count > maxCount) {
//             maxCount = count;
//             result = Number(num);
//         }
//     }
    
//     console.log(result)
// }
// majorityElement([1, 2, 3, 4, 5, 6, 4, 3, 4]);
/* H-TASK
    Savol: shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
    Masalan: getPositive([1, -4, 2]) return qiladi "12"
*/

// const getPositive = (arr)=> {
//     let text = ""
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] > 0) {
//             text += arr[i]
//         }
//     }
//     if(text == "") text = "No positive number here"
//     console.log(text)
// }

// getPositive([-1, -4, 2, 5, 'hello'])
/* F-TASK
    Savol: findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarshi kerak.
    Masalan: findDoublers("hello") return true return qiladi
    masalaning yexhimi:
*/
    // const findDoublers = function(str) {
    //     let count = 0
    //     for (let i = 0; i < str.length; i++) {
    //     for (let j = i + 1; j < str.length; j++) {
    //         if (str[i] === str[j]) {
    //             count++
    //         } 
    //     }
    // }
    // count > 0? console.log("the result is:", true): console.log("the result is:", false)
    // } 
    // findDoublers("helo")








/* E-Task:
    Savol: shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
    Masalan: getReverse("hello") return qilsin "olleh"
*/
//masalaning yechimi"
//     const getReverse = function(text) {
//         const result = text.split("").reverse().join("")
//         console.log(result)
//     }
// getReverse("hello")


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

