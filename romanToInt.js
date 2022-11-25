const romans = "I";

const standard = { M: 1000, D: 500, C: 100, L: 50, X: 10, V: 5, I: 1 };

let int = 0;
for (let index = 0; index <= romans.length - 1; index++) {
    if (standard[romans[index + 1]] === undefined) {
        int += standard[romans[index]];
        break;
    }
    if (standard[romans[index]] >= standard[romans[index + 1]]) {
        int += standard[romans[index]];
    } else {
        int -= standard[romans[index]];
    }
}

console.log(int);
