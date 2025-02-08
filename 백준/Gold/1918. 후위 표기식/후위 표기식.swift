import Foundation

let input = Array(readLine()!).map{ String($0) }
var output: [String] = []
var operators: [String] = [] 
var priorityDict: [String: Int] = ["-" : 1, "+" : 1, "/" : 2, "*" : 2]

for c in input {
    switch c {
        case "-", "+", "/", "*":
        while let str = operators.last, let lastPriority = priorityDict[str], 
        let priority = priorityDict[c], lastPriority >= priority {
            output.append(operators.removeLast())
        }
        operators.append(c)
        case "(":
        operators.append(c)
        case ")": // 여는 괄호 나오기 전까지 operator pop
        while let str = operators.last, str != "(" {
            output.append(operators.removeLast())
        }
        operators.removeLast() // 여는 괄호 제거 
        default:
        output.append(c) 
    }
}
while !operators.isEmpty {
    output.append(operators.removeLast())
}
print(output.joined(separator: ""))
