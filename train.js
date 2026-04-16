//"MITASK-A"
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
