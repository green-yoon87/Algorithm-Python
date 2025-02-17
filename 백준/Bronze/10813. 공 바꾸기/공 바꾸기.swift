import Foundation 

let input = readLine()!.split(separator: " ").map{ Int(String($0))!}
let n = input[0]
let m = input[1] 
var arr: [Int] = (0...n).map{ $0 }

(1...m).forEach {
    _ in
    let input = readLine()!.split(separator: " ").map{ Int(String($0))!}
    let temp = arr[input[0]]
    arr[input[0]] = arr[input[1]]
    arr[input[1]] = temp
}
let answer = arr.enumerated().filter{
    (idx, num) in 
    return idx != 0 
}.map{
    (idx, num) in 
    return String( num)}
.joined(separator: " ")
print(answer)