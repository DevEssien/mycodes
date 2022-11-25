let n = 09;

function reverse(n) {
    let int = String(n);
    let rev = "";
    if (int[0] === "-") rev += "-";
    for (let i = int.length - 1; i >= 0; i--) {
        if (int[i] !== "0") {
            for (let j = int.length - 1; j >= 0; j--) {
                if (int[j] !== "-") {
                    rev += int[j];
                    continue;
                } else {
                    rev += "";
                }
            }
            return rev;
        }
        // return rev;
    }
}

console.log(reverse(n));
// if (int[0] === "-") rev += "-";
// for (let i = int.length - 1; i >= 0; i--) {
//   if (int[i] !== '0') {
//     for (let i = int.length - 1; i >= 0; i--) {
//         if (int[i] !== "-") {
//             rev += int[i];
//             continue;
//         } else {
//             rev += "";
//         }
//     }
//   }
// }

// for (let i = int.length - 1; i >= 0; i--) {
//     if (int[i] !== "-") {
//         rev += int[i];
//         continue;
//     } else {
//         rev += "";
//     }
// }
// console.log(rev);
