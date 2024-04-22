def solution(edges):
    answer = []
    vertex, donut, bar, eight  = 0, 0, 0, 0
    max_val = max(map(max, edges))	
    vertexEdge = 0
    edgeIn = [[] for _ in range(max_val+1)]
    edgeOut = [[] for _ in range(max_val+1)]
    for edge in edges:
        edgeOut[edge[0]].append(edge[1])
        edgeIn[edge[1]].append(edge[0])
    for i in range(0, max_val +1):
        if len(edgeIn[i]) >=2 and len(edgeOut[i]) ==2:
            eight +=1
        elif len(edgeOut[i] ) >=2 and len(edgeIn[i]) ==0:
            vertex = i 
            vertexEdge = len(edgeOut[i] )
        elif len(edgeIn[i]) >= 1 and len(edgeOut[i]) == 0:
            bar +=1
            
    answer.append(vertex)
    answer.append(vertexEdge - bar - eight)
    answer.append(bar)
    answer.append(eight)
    
    return answer