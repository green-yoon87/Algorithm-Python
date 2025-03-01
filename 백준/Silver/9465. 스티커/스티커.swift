import Foundation 

let t = Int(readLine()!)!
(1...t).forEach { _ in
    let n = Int(readLine()!)!
    var stickers: [[Int]] = []
    for _ in 1...2 {
        let sticker = readLine()!.split(separator: " ").map{ Int(String($0))!}
        stickers.append(sticker)
    }
    var nothing = 0
    var leftSticker = stickers[0][0]
    var rightSticker = stickers[1][0]
    if n > 1 {
        for i in 1...(n - 1) {
            var tempNothing = max(leftSticker, rightSticker)
            var tempLeftSticker = max(nothing, rightSticker) + stickers[0][i]
            var tempRightSticker = max(nothing, leftSticker) + stickers[1][i]
            
            nothing = tempNothing 
            leftSticker = tempLeftSticker
            rightSticker = tempRightSticker
        }
    }
    print(max(nothing, max(leftSticker, rightSticker)))
}