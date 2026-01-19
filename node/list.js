// import {as} from "./a"
// console.log(as(7,8))


// function ayush(a) {
//     if (a == 1){
//         console.log("done")
//         return
//     }
//     console.log(a)
//     ayush(a-1)

// }
// console.log(ayush(10))






// function fector(x) {
//     if (x == 0){
//         // console.log("Invalid input")
//         return 1;

//     }
//         return x * fector(x-1)

// }
// console.log(fector(6))






// function array_sum(arr) {
//     if (arr.length === 0 ) {
//         return 0 ;
//     }
//     return arr[0 ] + array_sum(arr.slice(1))

    
// }

// console.log(array_sum([2,4,56,786]))




function sumOfdigit(n )   {
    if (n === 0){
        return 0
    }
    let a =  n % 10
    let remaning = Math.floor(n / 10)


    return a + sumOfdigit(remaning)

}
console.log(sumOfdigit(589))
