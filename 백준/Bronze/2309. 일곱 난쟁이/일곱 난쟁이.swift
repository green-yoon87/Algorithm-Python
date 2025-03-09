import Foundation 

var heights: [Int] = []
(1...9).forEach { _ in
    heights.append(Int(readLine()!)!)
}
let remain = heights.reduce(0, +) - 100
var exceptDwarfs: [Int] = [] 
for i in 0...7 {
    let height1 = heights[i]
    for j in (i + 1)...8 {
        if height1 + heights[j] == remain {
            exceptDwarfs = [height1, heights[j]]
            break
        } 
    }
}
heights.filter{ !exceptDwarfs.contains($0) }.sorted().forEach{
    print($0)
}