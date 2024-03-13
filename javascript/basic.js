console.log('Hello World');

// variables

//before es6
// var FristName = 'Balaji';

// present
let FristName = "Balaji Sai" ;
let LastName = 'Nadakuditi';

console.log(FristName);
console.log(LastName);

// constants

const PI = 3.14;
console.log(PI);
// PI = 3.15; Error

// Data Types

// Primitive Data Types
// String
let name = 'Balaji';
console.log(name);
// Number
let age = 21;
console.log(age);
// Boolean
let isMarried = false;
console.log(isMarried);
// null
let nullValue = null;
console.log(nullValue);
// undefined
let undefinedValue;
console.log(undefinedValue);
// dynamic typing
let dynamicType = 'Balaji';
console.log(dynamicType);
console.log(typeof dynamicType);
dynamicType = 21;
console.log(dynamicType);
console.log(typeof dynamicType);

console.log(typeof nullValue);

// Reference Data Types

// Object
let person = {
    name: 'Balaji',
    age: 21
};
console.log(person);
console.log(person.name);
console.log(person['name']);
person.name = 'Balaji Sai';
// Array  
let arr = [1.2, 'Balaji', true, null, undefined, {name: 'Balaji', age: 21}];
console.log(arr);
console.log(arr[0]);

arr[7] = 'Nadakuditi';
console.log(arr);
console.log(arr.length);

