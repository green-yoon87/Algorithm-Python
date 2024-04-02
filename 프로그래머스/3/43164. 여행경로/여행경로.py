answer = ["ICN"]
value = []
def solution(tickets):
    global answer
    global value
    countries = []
    ticketDict, visited = {}, {}

    for ticket in tickets:
        if ticketDict.get(ticket[0], 0) == 0:
            ticketDict[ticket[0]] = [ticket[1]]
        else:
            ticketDict[ticket[0]].append(ticket[1])
        if ticketDict.get(ticket[1], 0) == 0:
            ticketDict[ticket[1]] = []
        if visited.get(ticket[0] +" "+ticket[1], 0 ) == 0:
            visited[ticket[0] +" "+ticket[1]] = 1
        else:
            visited[ticket[0] +" "+ticket[1]] +=1
    dfs("ICN", visited, tickets, ticketDict)
    return value

def dfs(node, visited, tickets, ticketDict):
    global answer
    global value
    if len(node.split() ) >1:
        visited[node.split()[1] + " " + node.split()[0]] -=1
    node = node.split()[0]
    ticketDict[node].sort()
    if len(answer) == len(tickets) +1 and not value:
        value = answer[:]
        return 
    temp = ticketDict[node]
    for i in temp:
        if visited.get(node+" "+i, 0) > 0:
            answer.append(i)
            dfs(i+" "+node, visited, tickets, ticketDict)
            answer.pop()
            visited[node + " "+ i] +=1
   