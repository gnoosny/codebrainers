let integer = 3;
let float = 5.45
let boolean = true;
let nullType = null;
let string = "string";
let undefinedType = undefined;
const symbolType = Symbol('foo');
let notANumber = NaN;
let object = {'key1': 'element', 'key2': 'element'}
let array = [integer, float, boolean, nullType, string, undefinedType, symbolType, notANumber, object];

console.log(array);

for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}
///czym jest symbol??