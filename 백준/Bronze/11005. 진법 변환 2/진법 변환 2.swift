// 60466175 36
import Foundation 

let input = readLine()!.split(separator: " ").map{ Int(String($0))!}
let arr: [String] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
var n = input[0]
let v = input[1]
var answer = ""
while true {
    let remain = n % v
    var element = ""
    if remain >= 10 { element = arr[remain - 10]}
    else {element = String(remain)}
    answer = element + answer 
    if n / v == 0 { break }
    n /= v
}
print(answer)