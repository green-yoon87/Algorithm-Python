import Foundation 

let input = readLine()!.split(separator: " ").map{ String($0)}
var num = Array(input[0]).map{ String($0)}
let v = Int(input[1])!
var multiplier: Int = 1
var answer = 0 
let arr: [String] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
while !num.isEmpty {
    let n = num.removeLast()
    if let remain = Int(n) {
        answer += remain * multiplier
    } else {
        answer += getRemain(n) * multiplier
    }
    multiplier *= v
}
print(answer)
func getRemain(_ str: String) -> Int {
    for (idx, n) in arr.enumerated() {
        if n == str {return idx + 10}
    }
    return 0
}