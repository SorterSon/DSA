''' The function (climbing_stairs) takes the number of stairs, n 
as input and returns the number of ways in which 
one can climb from the nth stair to the 1st stair
given that either 1 or 2 steps can be climbed at once.
'''
def climbing_stairs(n):
    if n == 1 | n == 2:
    # If the number of stairs is 1 or 2, then
    # there is only 1 way.
        return 1
    prev2 = 1
    prev = 1
    for i in range(2, n+1):
    # For all other cases, the total number of ways 
    # can be calculated as the sum of number of 
    # ways till both 1 step down and 2 steps down.
        curr = prev2 + prev
        prev2 = prev
        prev = curr
    return prev

''' The function (frog_jump) takes the number of pillars, n
and a height array having the heights of each pillar, as 
input and returns the minimum energy using which the frog can 
jump from the 1st pillar to the nth pillar given that the frog 
can jump either 1 or 2 pillars at once and the amount of energy
consumed in a jump is equal to abs(height diff. b/w the pillars).
''' 
def frog_jump(n, height):
    if n == 1:
    # If there is only 1 pillar, no energy is consumed.
        return 0
    if n == 2:
    # If there are two pillars, then the energy consumed  
    # is the abs(height diff. b/w the two pillars).
        return abs(height[1] - height[0])
    prev2 = 0
    prev = height[1] - height[0]
    for i in range(2, n):
    # For all other cases, the minimum energy spent for 
    # the overall jump is calculated by considering the 
    # energy spent in the jumps till one pillar before as
    # well as in the jumps till two pillars before, along 
    # with the energy spent in the jump from those pillars 
    # to the current pillar and then taking the minimum of both.
        curr = min(abs(height[i] - height[i-1]) + prev, abs(height[i] - height[i-2]) + prev2)
        prev2 = prev
        prev = curr
    return prev

''' The function (frog_jump_k_distance) takes the number of 
pillars, n, the number of pillars the frog can jump at once, k 
and a height array having the heights of each pillar, as input 
and returns the minimum energy using which the frog can jump 
from the 1st pillar to the nth pillar given that the amount of 
energy consumed in a jump is equal to abs(height diff. b/w the pillars).
''' 
def frog_jump_k_distance(n, k, height):
    if n == 1:
    # If there is only 1 pillar, no energy is consumed.
        return 0
    prev = [0 for _ in range(k)]
    for i in range(1, n):
        curr = 1e9
        for step in range(1, k+1):
        # The nested loop takes care of all back steps 
        # (1 to k) from the current pillar...
            if i >= step:
        # ...and if it is possible to make that step from the 
        # current pillar, then the energy consumed in making that step
        # along with the energy consumed till reaching the previous 
        # pillar is calculated and the minimum of all is taken for 
        # reaching the current pillar.
                curr = min(curr, abs(height[i] - height[i-step]) + prev[step*(-1)])
        # Finally, the calculated minimum energy required to reach the last pillar
        # is stored in the prev arr for the calculation of energy consumed 
        # in reaching the next pillars.

        # Note that only the minimum energy required to reach the last k pillars
        # are required at once.
        prev = prev[1:].append(curr)
    return prev[-1]

''' The function (house_robber) takes the number of houses, n 
and an array listing the money present in each house, as input 
and returns the maximum money which the robber can steal from 
these houses given that no two consecutive houses can be robbed.
''' 
def house_robber(arr, n):
    if n == 1:
    # If there is only 1 house, only the money present
    # in that house can be robbed.
        return arr[0]
    prev2 = 0
    prev = arr[0]
    for i in range(1, n):
    # For all other cases, the maximum money that the 
    # robber can rob is calculated by considering the 
    # money that can stole by robbing the current house
    # along with robbing the previous houses leaving the 
    # last house a
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

def triangle(matrix, m):
    front = [1e9 for _ in range(m)]
    for j in range(m):
        front[j] = matrix[m-1][j]
    for i in range(m-2, -1, -1):
        curr = [1e9 for _ in range(m)]
        for j in range(i):
            curr[j] = matrix[i][j] + min(front[j], front[j+1])
        front = curr
    return front[0]

def min_falling_sum(matrix, m):
    front = [1e9 for _ in range(m)]
    for j in range(m):
        front[j] = matrix[m-1][j]
    for i in range(m-2, -1, -1):
        curr = [1e9 for _ in range(m)]
        for j in range(i):
            left = matrix[i][j]
            if j > 0:
                left += front[j-1]
            else:
                left += 1e9
            right = matrix[i][j]
            if j < m-1:
                right += front[j+1]
            else:
                right += 1e9
            down = matrix[i][j] + front[j]
            curr[j] = min(min(left, down), right)
        front = curr
    return min(front)

def cherry_pickup(matrix, m, n):
    front = [-1e9 for _ in range(n)]
    for j1 in range(n):
        for j2 in range(n):
            if j1 == j2:
                front[j1][j2] = matrix[m-1][j1]
            else:
                front[j1][j2] = matrix[m-1][j1] + matrix[m-1][j2]
    for i in range(m-2, -1, -1):
        curr = [-1e9 for _ in range(n)]
        for j1 in range(n):
            for j2 in range(n):
                if j1 == j2:
                    left = matrix[i][j2]
                    if j1 > 0:
                        left += front[j1-1]
                       
