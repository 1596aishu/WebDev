
// Write a function deepEqual that takes two values and returns true only if they are the same value or are objects with 
// the same properties, where the values of the properties are equal when compared with a recursive call to deepEqual.
// To find out whether values should be compared directly (use the === operator for that) or have their properties compared, 
// you can use the typeof operator. If it produces an "object" for both values, you should do a deep comparison. 
// But you have to take one silly exception into account: because of a historical accident, typeof null also produces "object".
// The Object.keys function will be useful when you need to go over the properties of objects to compare them.


function deepEqual(a, b) {
    if (a == b) {
      return true;
    } 
    else if (typeof a == 'object'&& typeof b == 'object') {
        let keys = Object.keys(a).concat(Object.keys(b));
        for (p of keys) {
            if (typeof a[p] == 'object' && typeof b[p] == 'object') {
                if (deepEqual(a[p], b[p]) == false) {
                    return false;
                }
            } 
            else if (a[p] !== b[p]) {
                return false;
            }
        }
        return true;
    } 
    else {
        return false; 
    }
  }

obj1 = {
    fn:"Aishwarya",
    ls:"Chundury"
}
obj2 = {
    fn:"Aditya",
    number:2019501056
}

obj3 = {
    fn:"Aishwarya",
    ls:"Chundury"
}

str1 = "Aishwarya"
str2 = 1596
str3 = "Chundury"

console.log(deepEqual(obj1,obj2))
console.log(deepEqual(obj1,obj3))
console.log(deepEqual(str2,str1))
console.log(deepEqual(str3,str1))
console.log(deepEqual(str1,str1))