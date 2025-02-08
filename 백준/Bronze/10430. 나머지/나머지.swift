import Foundation 
//첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let a = input[0]
let b = input[1]
let c = input[2]
let arr: [Int] = [(a + b) % c, (a % c + b % c) % c, (a * b) % c, (a % c * b % c) % c ]
arr.forEach { print($0)}