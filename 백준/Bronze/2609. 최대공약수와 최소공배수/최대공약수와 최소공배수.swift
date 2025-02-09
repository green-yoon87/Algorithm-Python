import Foundation

let input = readLine()!.split(separator: " ").map{ Int(String($0))!}
let num1 = input[0]
let num2 = input[1]
var gcd: Int = 1

for i in stride(from: num1, through: 1, by: -1) {
    if num2 % i == 0 && num1 % i == 0 { gcd = i; break }
}
print(gcd)
print(num1 * num2 / gcd)
