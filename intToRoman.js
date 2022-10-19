const n = 1994;

const intToRoman = (number) => {
    const checkStd = (number) => {
        switch (number) {
            case 1000:
                return "M";
            case 900:
                return "CM";
            case 500:
                return "D";
            case 400:
                return "CD";
            case 100:
                return "C";
            case 90:
                return "XC";
            case 50:
                return "L";
            case 40:
                return "XL";
            case 10:
                return "X";
            case 9:
                return "IX";
            case 5:
                return "V";
            case 4:
                return "IV";
            case 1:
                return "I";
            default:
                return "";
        }
    };

    let romanNumeral = "";

    function checkLessStd(number) {
        let stdToMinus;
        while (number > 0) {
            if (number >= 1000) {
                stdToMinus = 1000;
            } else if (number < 1000 && number >= 900) {
                stdToMinus = 900;
            } else if (number < 1000 && number >= 500) {
                stdToMinus = 500;
            } else if (number < 500 && number >= 400) {
                stdToMinus = 400;
            } else if (number < 400 && number >= 100) {
                stdToMinus = 100;
            } else if (number < 100 && number >= 90) {
                stdToMinus = 90;
            } else if (number < 90 && number >= 50) {
                stdToMinus = 50;
            } else if (number < 50 && number >= 40) {
                stdToMinus = 40;
            } else if (number < 40 && number >= 10) {
                stdToMinus = 10;
            } else if (number < 10 && number >= 9) {
                stdToMinus = 9;
            } else if (number < 9 && number >= 5) {
                stdToMinus = 5;
            } else if (number < 5 && number >= 4) {
                stdToMinus = 4;
            } else if (number < 4 && number >= 1) {
                stdToMinus = 1;
            }
            number -= stdToMinus;
            romanNumeral += checkStd(stdToMinus);
        }
    }

    if (!(checkStd(n) === "")) {
        romanNumeral += checkStd(n);
    } else {
        checkLessStd(n);
    }

    return romanNumeral;
};

console.log(intToRoman(n));
