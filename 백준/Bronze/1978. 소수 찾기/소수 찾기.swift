import Foundation 

let _ = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map{ Int(String($0))!}
var answer: Int = 0
for num in input {
    if isPrime(num) { answer += 1}
}
print(answer)

func isPrime(_ num: Int) -> Bool {
    if num == 1 { return false }
    else if num == 2 || num == 3 { return true }
    else if num % 2 == 0 || num % 3 == 0 { return false }
    for i in stride(from: 5, through: Int(sqrt(Double(num))), by: 2) {
        if num % i == 0 { return false }
    }
    return true
}