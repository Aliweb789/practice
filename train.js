
//====================================================================================

/* A-TASK:
    Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

//masalaning yechimi:
const countLetter = function(a, b) {
    let count = 0;
    for (const letter of b) {
        if(letter === a) {
            count++
        }
    }
    console.log("solution: ", count + " same letters")
}

countLetter("e", "engineer") //==>solution: 3
