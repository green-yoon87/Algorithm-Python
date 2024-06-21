struct Stack {
    var arr: [Int] = []
    var size: Int {
        return arr.count
    }
    var empty: Int {
        return arr.isEmpty ? 1 : 0
    }
    var top: Int {
        return arr.isEmpty ? -1 : arr[arr.count - 1]
    }
    mutating func push(_ num: Int){
        self.arr.append(num)
    }
    mutating func pop() -> Int {
        return self.arr.popLast() ?? -1
    }
}

var stack = Stack()
let T = Int(readLine()!)!
for _ in 0..<T{
    let input = readLine()!.split(separator: " " )
    if input.count >= 2{
        stack.push( Int(input[1])!)
    }
    else{
        // pop, size, empty, top
        switch input[0]{
            case "pop":
                print(stack.pop())
            case "size":
                print(stack.size)
            case "empty":
                print(stack.empty)
            case "top":
                print(stack.top)
            default:
                break
        }
    }
}