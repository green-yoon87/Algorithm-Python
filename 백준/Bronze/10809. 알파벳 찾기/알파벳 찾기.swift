import Foundation 

let input = Array(readLine()!).map{String($0)}
var dict: [String: Int] = [:]

for (idx, str) in input.enumerated() {
    if dict[str] == nil { dict[str] = idx }
}

let arr: [String] = "abcdefghijklmnopqrstuvwxyz".map { 
    if let cnt = dict[String($0)] {return String(cnt)}
    else {return "-1"}
}
print(arr.joined(separator: " "))