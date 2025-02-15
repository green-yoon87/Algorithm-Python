import Foundation 
let input1 = readLine()!.split(separator: " ").map{Int(String($0))!}
let a = input1[0]
let b = input1[1]
let m = Int(readLine()!)!
var input2 = readLine()!.split(separator: " ").map{Int(String($0))!}

var multiplier = 1 
var num = 0
while !input2.isEmpty {
    let element = input2.removeLast()
    num += multiplier * element 
    multiplier *= a 
}
var answer: [Int] = [] 
while true {
    answer.append(num % b)
    if num / b == 0 {
        break 
    }
    num /= b
}
answer.reverse()
print(answer.map{String($0)}.joined(separator: " "))