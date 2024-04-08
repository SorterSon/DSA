def climbing_stairs(n):
    if n == 1 | n == 2:
        return 1
    prev2 = 1
    prev = 1
    for i in range(2, n+1):
        curr = prev2 + prev
        prev2 = prev
        prev = curr
    return prev
    
def frog_jump(n, height):
    if n == 1:
        return 0
    if n == 2:
        return height[1] - height[0]
    prev2 = 0
    prev = height[1] - height[0]
    for i in range(2, n):
        curr = min(abs(height[i] - height[i-1]) + prev, abs(height[i] - height[i-2]) + prev2)
        prev2 = prev
        prev = curr
    return prev

def frog_jump_k_distance(n, k, height):
    if n == 1:
        return 0
    prev = [0 for _ in range(k)]
    for i in range(1, n):
        curr = 1e9
        for step in range(1, k+1):
            if i >= step:
                curr = min(curr, abs(height[i] - height[i-step]) + prev[i-step])
        prev = prev[1:].append(curr)
    return prev[-1]

def house_robber(arr, n):
    if n == 1:
        return arr[0]
    prev2 = 0
    prev = arr[0]
    for i in range(1, n):
        this = arr[i]
        if i > 1:
            this += prev2
        next = prev
        curr = max(this, next)
        prev2 = prev
        prev = curr
    return prev

def house_robber_circular(arr, n):
    if n == 1:
        return arr[0]
    temp1 = []
    temp2 = []
    for i in range(n):
        if i != 0:
            temp1.append(arr[i]) 
        if i != n-1:
            temp2.append(arr[i]) 
    return max(house_robber(temp1, n-1), house_robber(temp2, n-1))

def ninja_training(matrix, n):
    prev = [0 for _ in range(4)]
    for last in range(4):
        for task in range(3):
            if last != task:
                prev[last] = max(matrix[0][task], prev[last])
    for day in range(1, n):
        curr = [0 for _ in range(4)]
        for last in range(4):
            for task in range(3):
                if last != task:
                    curr[last] = max(matrix[day][task] + prev[task], curr[last])
        prev = curr
    return prev[-1]

def count_paths(matrix, m, n):
    if m == 1 and n == 1:
        return 1
    prev = [0 for _ in range(n)]
    for i in range(m):
        curr = [0 for _ in range(n)]
        for j in range(n):
            if i == 0 and j == 0:
                curr[0] = 1
            if i > 0:
                curr[j] += prev[j]
            if j > 0:
                curr[j] += curr[j-1]
        prev = curr
    return prev[-1]

def count_paths_with_obstacles(matrix, m, n, mod): 
    if m == 1 and n == 1:
        return 1
    prev = [0 for _ in range(n)]
    for i in range(m):
        curr = [0 for _ in range(n)]
        for j in range(n):
            if i == 0 and j == 0:
                curr[0] = 1
            if matrix[i][j] == -1:
                curr[j] = 0
                continue
            if i > 0:
                curr[j] = (curr[j] + prev[j]) % mod
            if j > 0:
                curr[j] = (curr[j] + curr[j-1]) % mod
        prev = curr
    return prev[-1]

def min_path_sum(matrix, m, n):
    if m == 1 and n == 1:
        return matrix[0][0]
    prev = [1e9 for _ in range(n)]
    for i in range(m):
        curr = [1e9 for _ in range(n)]
        for j in range(n):
            if i == 0 and j == 0:
                curr[0] = matrix[0][0]
            if i > 0:
                curr[j] = min(curr[j], matrix[i][j] + prev[j])
            if j > 0:
                curr[j] = min(curr[j], matrix[i][j] + curr[j-1])
        prev = curr
    return prev[-1]