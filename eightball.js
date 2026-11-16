
function createEightBall(saltsString = "", useEnd = false) {
    let salts = [];
    let i = 0;
    let mode = "free";
    let theend = false;
    let useend = useEnd;

    const answers = [
        {"text": "● It is certain.", "val": 1},
        {"text": "● It is decidedly so.", "val": 1},
        {"text": "● Without a doubt.", "val": 1},
        {"text": "● Yes definitely.", "val": 1},
        {"text": "● You may rely on it.", "val": 1},
        {"text": "● As I see it, yes.", "val": 0.6},
        {"text": "● Most likely.", "val": 0.8},
        {"text": "● Outlook good.", "val": 0.7},
        {"text": "● Yes.", "val": 1},
        {"text": "● Signs point to yes.", "val": 0.9},
        {"text": "● Reply hazy, try again.", "val": 0.6},
        {"text": "● Ask again later.", "val": 0.6},
        {"text": "● Better not tell you now.", "val": 0.4},
        {"text": "● Cannot predict now.", "val": 0.4},
        {"text": "● Concentrate and ask again.", "val": 0.6},
        {"text": "● Don't count on it.", "val": 0.1},
        {"text": "● My reply is no.", "val": 0},
        {"text": "● My sources say no.", "val": 0.3},
        {"text": "● Outlook not so good.", "val": 0.2},
        {"text": "● Very doubtful. ", "val": 0.1}
    ];

    // Вспомогательные функции
    function getNumber(length, salt) {
        let sums = 0;
        for (let j = 0; j < salt.length; j++) {
            sums += salt.charCodeAt(j);
        }
        return Math.ceil(sums % length);
    }

    function getOne(ar, salt, justnum = false) {
        const length = ar.length;
        const num = getNumber(length, salt);

        if (justnum) return num;

        i += 1;
        if (i >= salts.length) {
            i = 0;
            theend = true;
        }

        return ar[num];
    }

    function answer() {
        let ans;
        if (mode === "free") {
            ans = answers[Math.floor(Math.random() * answers.length)].val;
        } else {
            ans = getOne(answers, salts[i]).val;
        }
        return ans > 0.5;
    }

    // Публичные методы
    function random(ar) {
        if (mode === "free") {
            return ar[Math.floor(Math.random() * ar.length)];
        } else {
            return getOneByEightBall(ar);
        }
    }

    function randomFromRange(minv, maxv) {
        const rlist = [];
        if (minv < maxv) {
            for (let j = minv; j <= maxv; j++) {
                rlist.push(j);
            }
        }

        if (mode === "free") {
            return rlist[Math.floor(Math.random() * rlist.length)];
        } else {
            return getOneByEightBall(rlist);
        }
    }

    function getOneByEightBall(ar, justnum = false) {
        let item = null;
        let yes = false;

        while (!yes) {
            item = getOne(ar, salts[i], justnum);
            yes = answer();
        }

        if (useend && theend) {
            return false;
        }

        return item;
    }

    function answerText(salt) {
        return getOne(answers, salt).text;
    }

    function getOneRandomByEightBall(ar) {
        let item = null;
        let yes = false;

        while (!yes) {
            item = ar[Math.floor(Math.random() * ar.length)];
            yes = answer();
        }

        return item;
    }

    function getOneBySalts(ar, justnum = false) {
        const item = getOne(ar, salts[i], justnum);

        if (useend && theend) {
            return false;
        }

        return item;
    }

    function setSalts(saltsStr) {
        const saltssplitted = saltsStr.split(" ");
        salts = [];
        for (const salt of saltssplitted) {
            if (salt !== "") {
                salts.push(salt);
            }
        }
        if (salts.length > 0) {
            mode = "salted";
        }
    }

    // Инициализация
    if (saltsString !== "") {
        setSalts(saltsString);
    }

    // Возвращаемый объект с публичными методами
    return {
        // Свойства
        salts: () => salts,
        mode: () => mode,
        theend: () => theend,
        useend: () => useend,
        answers: () => answers,

        // Методы
        random,
        randomFromRange,
        answer,
        getOneByEightBall,
        answerText,
        getOneRandomByEightBall,
        getOneBySalts,
        setSalts
    };
}

// Пример использования:
// const eightBall = createEightBall("my salt string", true);
// const result = eightBall.answer();
// const randomItem = eightBall.random([1, 2, 3, 4, 5]);

getbookwithsalt = function(salt = "") {
    let israndom = salt === "";
    let shelves = [
        { name: "first", books: 10},
        { name: "second", books: 12},
        { name: "third", books: 11},
        { name: "fourth", books: 12},
        { name: "fourth", books: 9}
    ];
    if (!israndom) {
        e8 = createEightBall(salt);

        shelve = e8.getOneBySalts(shelves);
        book = e8.getOneBySalts(Array.from(Array(shelve.books).keys())) + 1;
        paragraph = e8.getOneBySalts(Array.from(Array(10).keys())) + 1;
    } else {

        e8 = createEightBall();

        shelve = e8.random(shelves);
        book = e8.random(Array.from(Array(shelve.books).keys())) + 1;
        paragraph = e8.random(Array.from(Array(10).keys())) + 1;
    }

    return "shelve:" + shelve.name + "; book:" + book + "; paragraph: " + paragraph;
}

