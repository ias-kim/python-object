type a = {
    user: number;
    name: string
}




interface A {
    get(name: string): a
}


class child implements A {
    constructor(private a: Number, private b: String, private c: Object) {
        this.a = a
        this.b = b
        this.c = c
    }

    get(name: string): a {
        const newId = 1
        const newUser: a = {
            user: newId,
            name
        }
        return newUser
    }
}

interface IPerson {
    name: string,
    age: number,

    get(): void,
    getName(): string
}

interface Animal {
    name: string;
    bark(): void;
}

function prtValue<T extends IPerson> (
    o: CT<T>,
    key: keyof CT<T>
): CT<T>[keyof CT<T>] {
    return o[key];
}

type CT<T extends IPerson | Animal> = T extends IPerson ? IPerson : Animal

const val = prtValue<IPerson> ({
    name: "abc",
    age: 14,
    get() {},
    getName() {
        return this.name
    },
}, "age")


type User = {
    name: string;
    age: number;
    gender: string;
}

class IUser implements User {
    constructor(public name: string, public age: number, public gender: string) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }
}
var u1 = new IUser("ycjung", 2, "M")

function createdUser(name: string, age: number, gender: string): IUser {
    return new IUser(name, age, gender);
}

const newUser = createdUser("ycjung", 2, "M");


class Vector {
    constructor(private x: number, private y: number) {
        this.x = x;
        this.y = y;
    }
}
const v1 = new Vector(1, 2)
const v2 = new Vector(3, 4)

// v3 = v1 + v2