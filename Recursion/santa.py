def santa(wish_list, N, max, visited = [], curr = 1, count = 0):
    if curr > N:
        if count > max:
            max = count
        return max
 
    m = 0
    if visited[curr] == 0 and visited[curr - 1] == 0:
        visited[curr] = 1
        count += wish_list[curr - 1]
        m = santa(wish_list, N, max, visited,  curr + 1, count)
        visited[curr] = 0
        count -= wish_list[curr - 1]
 
    n = santa(wish_list, N, max, visited,  curr + 1, count)
    if m > n:
        return m
    else:
        return n
 
def help_santa(wish_list, max = 0):
    a = 0
    N = len(wish_list)
    visited = [0 for i in range(N + 1)]
    m = santa(wish_list, N, max, visited)
    for i in wish_list:
        a += i
    return a - m
    
wish_list = [155, 44, 52, 58, 250, 225, 109, 178]
print(help_santa(wish_list))
