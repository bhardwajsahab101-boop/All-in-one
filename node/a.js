
// a ={
//     name1 : "ayush",
//     age : 17,
//     class : "AIFT"
// }
// console.log(a)
// // modifing value of the object
// a.age = 78
// // modifing value of the object.
// a["name1"] = "sharma"

// console.log(a)
// // deleteing values from object.
// delete a.age ;
// console.log(a)
// // asscesing values of objects.
// let asdf = "aman"
// console.log(asdf)

// let age = 17
// let persion ={ 
//     name:"ayush",
//     age : age
// }
// console.log(persion)

// let persion1 = ["ayush",17,"AIFT"]
// console.log(persion1[0])

// persion1.push("student")
// console.log(persion1)
// persion1.pop("AIFT")
// console.log(persion1)



// let a = {
//     namee : "Ayush",
//     age : 17,
//     study :"Btech",
// }

// console.log(a.namee)
// let b = [1,3,45,6,7]
// b.slice(3,0,9)
// console.log(b)
// function sharma(names , ages , education) {
//     this.names = names;
//     this.ages = ages;
//     this.education = education;
// }



// fruits.push("orange");         // Adds "orange" to the end
// console.log(fruits);          // Output: ["apple", "banana", "orange"]

// fruits.pop();                // Removes the last element ("orange")
// console.log(fruits);          // Output: ["apple", "banana"]

// fruits.unshift("grape");      // Adds "grape" to the beginning
// console.log(fruits);          // Output: ["grape", "apple", "banana"]

// fruits.shift();              // Removes the first element ("grape")
// console.log(fruits);          // Output: ["apple", "banana"]

// let fruits = ["apple", "banana"];

// fruits.splice(0, 3, "kiwi");  // Adds "kiwi" at index 1
// console.log(fruits);          // Output: ["apple", "kiwi", "banana"]

// fruits.splice(0, 1);          // Removes the element at index 0 ("apple")
// console.log(fruits);          // Output: ["kiwi", "banana"]

// let marks =  prompt("whar is your marks : ")
// let cases ;
// switch (cases) {
//     case(marks>50):
//         document.write("you are pass")
//         break;

//     default:
//         break;
// }

// if 5 > 6? 
  
// class Ayush {
//     constructor(name,age) {
//         this.name = name
//         this.age = age
//     }
// }
// const person = new Ayush("ayush",18)
// console.log(person)




/* making set in javascript */


// const numbers = new Set();
// numbers.add(7);
// numbers.add(8);
// numbers.add(9);
// numbers.add(10);

// console.log(numbers)



/* converting a array into a set  */

// let arr = [1,45,77,1,2,3,4,1]
// const number = new Set(arr)
// console.log(number)



var as = (a,b) => a+b

console.log(as(3,5))

module.exports = {as};