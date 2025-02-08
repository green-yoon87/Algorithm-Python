import Foundation 

let input = readLine()!.split(separator: " ").map{ String($0) }
let str1 = input[0] + input[1]
let str2 = input[2] + input[3]
print(Int(str1)! + Int(str2)!)