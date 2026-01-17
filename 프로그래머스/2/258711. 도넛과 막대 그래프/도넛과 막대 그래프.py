from collections import defaultdict

ans = [0, 0, 0, 0]

def whatFrom(graph, s):
    cur = graph[s][0]
    while 1:
        next_nodes = graph[cur]
        if len(next_nodes) == 2:
            ans[3] += 1
            return
        if len(next_nodes) == 0:
            ans[2] += 1
            return
        if cur == s:
            ans[1] += 1
            return
        cur = next_nodes[0]
        

def solution(edges):
    max_node = 0
    for start, end in edges:
        max_node = max(start, end, max_node)
    
    graph = [[] for _ in range(max_node + 1)]
    out_in_list = [0] * (max_node + 1)
    isolation = 0
    
     # 생성, 도넛, 막대, 8
    
    for start, end in edges:
        out_in_list[start] += 1
        out_in_list[end] -= 1
        
        graph[start].append(end)
    
    for idx, node in enumerate(out_in_list):
        if node >= 2:
            isolation = idx
            
    ans[0] = isolation

    for s_node in graph[isolation]:
        if len(graph[s_node]) == 0:
            ans[2] += 1
        elif len(graph[s_node]) == 2:
            ans[3] += 1
        else:        
            whatFrom(graph, s_node)
    return ans