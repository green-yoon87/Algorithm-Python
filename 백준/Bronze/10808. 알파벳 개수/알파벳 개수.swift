if let line = readLine() {
    let input = line.lowercased().map { String($0) }
    var dict: [String: Int] = [:]

    input.forEach {
        if let cnt = dict[$0]  { dict[$0] = cnt + 1 }
        else { dict[$0] = 1 }
    }

    let answer: [String] = "abcdefghijklmnopqrstuvwxyz".map {
        if let cnt = dict[String($0)] { return String(cnt) }
        else { return "0" }
    }
    
    print(answer.joined(separator: " "))
}