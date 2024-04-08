import queue

class Graph:
    
    def __init__(self, num_nodes, directed = False, weighted = False):
        # 1-based indexing
        if not weighted:
            if not directed:
                self.adj_list = []
                self.size = num_nodes + 1
                self.visited = [False]*self.size
                for i in range(num_nodes+1):
                    self.adj_list.append([])
                self.num_edges = int(input())
                for _ in range(self.num_edges):
                    node_1_2 = input().split()
                    node_1 = int(node_1_2[0])
                    node_2 = int(node_1_2[1])
                    self.adj_list[node_1].append(node_2)
                    self.adj_list[node_2].append(node_1)
            else:
                self.adj_list = []
                self.size = num_nodes + 1
                self.visited = [False]*self.size
                for i in range(num_nodes+1):
                    self.adj_list.append([])
                self.num_edges = int(input())
                for _ in range(self.num_edges):
                    node_1_2 = input().split()
                    node_1 = int(node_1_2[0])
                    node_2 = int(node_1_2[1])
                    self.adj_list[node_1].append(node_2)
        else:
            if not directed:
                self.adj_list = []
                self.size = num_nodes + 1
                self.visited = [False]*self.size
                for i in range(num_nodes+1):
                    self.adj_list.append([])
                self.num_edges = int(input())
                for _ in range(self.num_edges):
                    node_1_2_and_weight = input().split()
                    node_1 = int(node_1_2_and_weight[0])
                    node_2 = int(node_1_2_and_weight[1])
                    wgt = int(node_1_2_and_weight[2])
                    self.adj_list[node_1].append([node_2, wgt]) 
                    self.adj_list[node_2].append([node_1, wgt])
            else:
                self.adj_list = []
                self.size = num_nodes + 1
                self.visited = [False]*self.size
                for i in range(num_nodes+1):
                    self.adj_list.append([])
                self.num_edges = int(input())
                for _ in range(self.num_edges):
                    node_1_2_and_weight = input().split()
                    node_1 = int(node_1_2_and_weight[0])
                    node_2 = int(node_1_2_and_weight[1])
                    wgt = int(node_1_2_and_weight[2])
                    self.adj_list[node_1].append([node_2, wgt])    

        print(self.adj_list)

    def bfs(self, start_node):
        q = []
        result = ""
        q.append(start_node)
        self.visited[start_node] = True
        while q != []:
            curr = q[0]
            q.remove(curr)
            result += str(curr) + " -> "
            for i in self.adj_list[curr]:
                if not self.visited[i]:
                    q.append(i)
                    self.visited[i] = True
        return result[:-4]
    
    def dfs(self, start_node):
        result = [""]
        def helper(node, result):
            if self.visited[node]:
                return 
            result[0] += str(node) + " -> "
            self.visited[node] = True
            for i in self.adj_list[node]:
                if not self.visited[i]:
                    helper(i, result)
        helper(start_node, result)
        return result[0][:-4]
    
    def provinces(self):
        traversals = []
        for i in range(1, len(self.adj_list)):
            if not self.visited[i]:
                output = self.dfs(i)
                traversals.append(output)
        return len(traversals), traversals
    
    def detect_UCG_dfs(self):
        def helper(node, parent):
            self.visited[node] = True
            for i in self.adj_list[node]:
                if self.visited[i] and i != parent and parent != -1:
                    return True
                if not self.visited[i]:
                    return helper(i, node)
            return False
        
        ans = False
        for i in range(1, len(self.adj_list)):
            if not self.visited[i]:
                is_cycle = helper(i, -1)
                ans |= is_cycle
                 
        return ans
    
    def detect_UCG_bfs(self):
        def helper(node):
            queue = []
            queue.append([node, -1])
            while queue != []:
                curr = queue[0]
                queue.remove(curr)
                for i in self.adj_list[curr[0]]:
                    if self.visited[i] and curr[1] != i and curr[1] != -1:
                        return True
                    if not self.visited[i]:
                        queue.append([i, curr[0]])
                        self.visited[i] = True
            return False

        for i in range(1, len(self.adj_list)):
            if helper(i):
                return True
        return False
    
    def bipartite_check_bfs(self):
        color = [-1 for _ in range(len(self.adj_list))]
        def helper(node, color):
            clr = 0
            queue = []
            queue.append(node)
            color[node] = clr
            while queue != []:
                size = len(queue)
                clr = 1 - clr
                for _ in range(size):
                    curr = queue[0]
                    queue.remove(curr)
                    for i in self.adj_list[curr]:
                        if color[i] == -1:
                            color[i] = clr
                            queue.append(i)
                        elif color[i] == 1 - clr:
                            return False
            return True
        
        for i in range(1, len(self.adj_list)):
            if color[i] == -1:
                if not helper(i, color):
                    return False
        return True

    def bipartite_check_dfs(self):
        color = [-1 for _ in range(len(self.adj_list))]
        def helper(node, color, clr):
            color[node] = 1 - clr
            for i in self.adj_list[node]:
                if color[i] == -1:
                    color[i] = clr
                    return helper(i, color, 1 - clr)
                elif color[i] == 1 - clr:
                    return False
            return True
        
        for i in range(1, len(self.adj_list)):
            if color[i] == -1:
                if not helper(i, color, 1):
                    return False
        return True

    def detect_DCG_dfs(self):
        # Can be done using a single array by marking visited as 1 and path_visited as 2.
        path_visited = [False for _ in range(len(self.adj_list))]
        def helper(node, path_visited):
            self.visited[node] = True
            path_visited[node] = True
            for i in self.adj_list[node]:
                if self.visited[i] == False:
                    if helper(i, path_visited):
                        return True
                elif path_visited[i] == True:
                    return True
            path_visited[node] = False
            return False
        
        for i in range(1, len(self.adj_list)):
            if helper(i, path_visited):
                return True
        return False        
    
    def check_safe_states1(self):
        def helper(node):
            self.visited[node] = 2
            for i in self.adj_list[node]:
                if self.visited[i] == False:
                    if helper(i):
                        return True
                elif self.visited[i] == 2:
                    return True
            self.visited[node] = 1
            return False

        for i in range(1, len(self.adj_list)):
            helper(i)
        
        res = [i for i in range(1, len(self.visited)) if self.visited[i] == 1]
        return res
    
    def check_safe_states2(self):
        adj_list = [[] for _ in range(len(self.adj_list))]
        indegree = [0 for _ in range(len(self.adj_list))]
        # Graph is reversed
        for i in range(1, len(self.adj_list)):
            for nd in self.adj_list[i]:
                adj_list[nd].append(i)
                indegree[i] += 1

        queue = []
        for i in range(1, len(adj_list)):
            if indegree[i] == 0:
                queue.append(i)

        stack = []
        while queue != []:
            curr = queue[0]
            queue.remove(curr)
            for i in adj_list[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            stack.append(curr)

        return sorted(stack)
    
    def topological_sort_dfs(self):
        stack = []
        def helper(node, stack):
            self.visited[node] = True
            for i, weight in self.adj_list[node]:
                if not self.visited[i]:
                    helper(i, stack)
            stack.append(node)
        
        for i in range(1, len(self.adj_list)):
            if not self.visited[i]:
                helper(i, stack)

        return stack
    
    def topological_sort_bfs1(self):
        stack1 = []
        stack2 = []
        def helper(node, stack1, stack2):
            queue = []
            queue.append(node)
            self.visited[node] = True
            while queue != []:
                curr = queue[0]
                queue.remove(curr)
                not_yet = False
                for i in self.adj_list[curr]:
                    if not self.visited[i]:
                        queue.append(i)
                        self.visited[i] = True                     
                        not_yet = True
                if not not_yet:
                    stack1.append(curr)
                else:
                    stack2.append(curr)
            while stack2 != []:
                stack1.append(stack2.pop())
        
        for i in range(1, len(self.adj_list)):
            if not self.visited[i]:
                helper(i, stack1, stack2)

        out = ""
        for i in stack1:
            out = str(i) + " " + out

        return out[:-1]
    
    def topological_sort_bfs2(self):
        indegree = [0 for _ in range(len(self.adj_list))]
        for i in range(1, len(self.adj_list)):
            for nd in self.adj_list[i]:
                indegree[nd] += 1
        
        queue = []
        for i in range(1, len(self.adj_list)):
            if indegree[i] == 0:
                queue.append(i)

        stack = []
        while queue != []:
            curr = queue[0]
            queue.remove(curr)
            for i in self.adj_list[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            stack.append(curr)

        out = ""
        for i in stack:
            out = out + ' ' + str(i)

        return out[1:] 
    
    def shortest_distance_bfs(self, src):
        self.visited = [-1 for _ in range(len(self.adj_list))]
        self.visited[src] = 0
        queue = []
        queue.append(src)
        while queue != []:
            curr = queue[0]
            queue.remove(curr)
            for nd, weight in self.adj_list[curr]:
                val = self.visited[curr] + weight
                if self.visited[nd] == -1:
                    self.visited[nd] = val
                    queue.append(nd)
                elif self.visited[nd] > val:
                    self.visited[nd] = val
                    queue.append(nd)
        return self.visited
    
    # This is to prevent repeated insertions of subsequent elements in the queue (in the prev. method)
    def shortest_distance_after_toposort(self, src):
        dist = [1e9 for _ in range(len(self.adj_list))]
        dist[src] = 0
        topo_sort = self.topological_sort_dfs()[::-1]
        for nd in topo_sort:
           for neighbour_nd, weight in self.adj_list[nd]: 
               dist[neighbour_nd] = min(dist[neighbour_nd], dist[nd] + weight)
        return dist
    
    def shortest_distance_undirected(self, src):
        dist = [1e9 for _ in range(len(self.adj_list))]
        dist[src] = 0
        queue = []
        queue.append(src)
        while queue != []:
            curr = queue[0]
            queue.remove(curr)
            for i, weight in self.adj_list[curr]:
                if dist[i] > dist[curr] + weight:
                    dist[i] = dist[curr] + weight
                    queue.append(i)
        return dist 
    # The property of Priority Queue prevents repeated insertions of subsequent elements in the queue (in the prev. method) 
    def shortest_distance_Dijkstra(self, src):
    # With negative weights, the program runs into an infinite loop
        dist = [1e9 for _ in range(len(self.adj_list))]
        dist[src] = 0
        que = queue.PriorityQueue()

        def remove_from_priority_queue(pq, item_to_remove):
            temp_list = []

            # Remove all items from the priority queue, excluding the item to remove
            while not pq.empty():
                item = pq.get()
                if item != item_to_remove:
                    temp_list.append(item)

            # Reinsert items from the temporary list back into the priority queue
            for item in temp_list:
                pq.put(item)

        que.put([0, src])
        while not que.empty():
            curr = que.get()
            nd = curr[1]
            distance = curr[0]
            remove_from_priority_queue(que, curr)
            for neighbor_nd, weight in self.adj_list[nd]:
                if dist[neighbor_nd] == 1e9:
                    dist[neighbor_nd] = dist[nd] + weight
                    que.put([dist[neighbor_nd], neighbor_nd])
                elif dist[neighbor_nd] > dist[nd] + weight:
                    remove_from_priority_queue(que, [dist[neighbor_nd], neighbor_nd])
                    dist[neighbor_nd] = dist[nd] + weight
                    que.put([dist[neighbor_nd], neighbor_nd])
        return dist
    
    def shortest_path(self, src, dest):
        parent = [i for i in range(len(self.adj_list))]
        dist = [1e9 for _ in range(len(self.adj_list))]
        dist[src] = 0
        que = queue.PriorityQueue()
        que.put([0, src])
        while not que.empty():
            curr = que.get()
            nd = curr[1]
            distance = curr[0]
            for neighbor_nd, weight in self.adj_list[nd]:
                if dist[neighbor_nd] > dist[nd] + weight:
                    dist[neighbor_nd] = dist[nd] + weight
                    que.put([dist[neighbor_nd], neighbor_nd])
                    parent[neighbor_nd] = nd   

        ans = []
        node = dest
        while node != parent[node]:
            ans.append(node)
            node = parent[node]
        ans.append(src)
        if node == src:
            return ans[::-1]
        else:
            return [-1]
        
    def cheapest_flights(self, src, dest, k_stops): 
        cost = [1e9 for _ in range(len(self.adj_list))]
        cost[src] = 0
        que = []
        que.append([0, [src, 0]])
        while que != []:
            curr = que[0]
            stops = curr[0]
            nd = curr[1][0]
            cst = curr[1][1]
            que.remove(curr)
            if stops > k_stops:
                continue
            for neighbor_nd, cst_ in self.adj_list[nd]:
                if cost[neighbor_nd] > cst + cst_ and stops <= k_stops:
                    cost[neighbor_nd] = cst + cst_
                    que.append([1 + stops, [neighbor_nd, cost[neighbor_nd]]])
        
        if cost[dest] == 1e9:
            return -1
        else:
            return cost[dest]

def num_islands_bfs(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = 0
    visited = [[False]*n for _ in range(m)]
    queue = []
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == '1' and visited[row][col] == False:
                result += 1
                visited[row][col] = True
                queue.append([row, col])
            delta = [-1, 0, 1]
            while queue != []:
                curr = queue[0]
                queue.remove(curr)
                for delta_row in delta:
                    for delta_col in delta:
                        new_row = curr[0] + delta_row
                        new_col = curr[1] + delta_col
                        if new_row >= 0 and new_col >= 0 and new_row < m and new_col < n and matrix[new_row][new_col] == '1' and visited[new_row][new_col] == False:
                            visited[new_row][new_col] = True
                            queue.append([new_row, new_col])
    return result

def num_islands_dfs(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[False]*n for _ in range(m)]
    def helper_dfs(matrix, row, col, visited):
        visited[row][col] = True
        delta = [-1, 0, 1]
        for del_row in delta:
            for del_col in delta:
                new_row = row + del_row
                new_col = col + del_col
                if  new_row >= 0 and new_col >= 0 and new_row < m and new_col < n and matrix[new_row][new_col] == '1' and visited[new_row][new_col] == False:
                    helper_dfs(matrix, new_row, new_col, visited)
    
    result = 0
    for row in range(m):
        for col in range(n):
            if visited[row][col] == False and matrix[row][col] == '1':
                helper_dfs(matrix, row, col, visited)
                result += 1
    return result

def flood_fill_bfs(matrix, sr, sc, nwcolor):
    ini_color = matrix[sr][sc]
    ans = [submatrix[:] for submatrix in matrix]
    ans[sr][sc] = str(nwcolor)
    m = len(ans)
    n = len(ans[0])
    queue = []
    queue.append([sr, sc])
    
    while queue != []:
        curr = queue[0]
        queue.remove(curr)
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, -1, 0, 1]
        for i in range(4):
            new_row = curr[0] + delta_row[i]
            new_col = curr[1] + delta_col[i]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and ans[new_row][new_col] == ini_color:
                ans[new_row][new_col] = str(nwcolor)
                queue.append([new_row, new_col])
    return ans

def flood_fill_dfs(matrix, sr, sc, nwcolor):
    ini_color = matrix[sr][sc]
    ans = [submatrix[:] for submatrix in matrix]
    ans[sr][sc] = str(nwcolor)
    m = len(ans)
    n = len(ans[0])

    def helper_dfs(ans, matrix, row, col, nwcolor):
        ans[row][col] = str(nwcolor)
        delta_row = [0, -1, 0, 1]
        delta_col = [-1, 0, 1, 0]
        for i in range(4):
            new_row = row + delta_row[i]
            new_col = col + delta_col[i]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and ans[new_row][new_col] == ini_color:
                helper_dfs(ans, matrix, new_row, new_col, nwcolor)

    helper_dfs(ans, matrix, sr, sc, nwcolor)
    return ans  

def rotten_oranges(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = [submatrix[:] for submatrix in matrix]
    queue = []
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == '2':
                queue.append([row, col, 0])
    
    min_time = 0
    delta_row = [0, -1, 0, 1]
    delta_col = [-1, 0, 1, 0]
    while queue != []:
        curr = queue[0]
        queue.remove(curr)
        for i in range(4):
            new_row = curr[0] + delta_row[i]
            new_col = curr[1] + delta_col[i]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and ans[new_row][new_col] == '1':
                ans[new_row][new_col] = '2'
                queue.append([new_row, new_col, curr[2] + 1])
                min_time = max(min_time, curr[2] + 1)
    
    for row in range(m):
        for col in range(n):
            if ans[row][col] == '1':
                return -1
            
    return min_time     

def nrst_cell_with1_m1(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = [submatrix[:] for submatrix in matrix]
    def helper(row, col, matrix, m, n):
        queue = []
        queue.append([row, col])
        dist = 0
        delta_row = [0, -1, 0, 1]
        delta_col = [-1, 0, 1, 0]
        while queue != []:
            size = len(queue)
            dist += 1
            for i in range(size):
                curr = queue[0]
                queue.remove(curr)
                for i in range(4):
                    new_row = curr[0] + delta_row[i]
                    new_col = curr[1] + delta_col[i]
                    if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n:
                        if matrix[new_row][new_col] == '1':
                            return dist
                        else:
                            queue.append([new_row, new_col])
                    
    
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == '1':
                ans[row][col] = 0
            else:
                ans[row][col] = helper(row, col, matrix, m, n)
    return ans

def nrst_cell_with1_m2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = [[-1 for _ in range(len(submatrix))] for submatrix in matrix]
    queue = [] 
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == '1':
                queue.append([row, col, 0])
    
    delta_row = [0, -1, 0, 1]
    delta_col = [-1, 0, 1, 0]
    while queue != []:
        curr = queue[0]
        queue.remove(curr)
        ans[curr[0]][curr[1]] = curr[2]
        for i in range(4):
            new_row = curr[0] + delta_row[i]
            new_col = curr[1] + delta_col[i]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and ans[new_row][new_col] == -1 and matrix[new_row][new_col] == '0':
                queue.append([new_row, new_col, curr[2] + 1])
                ans[new_row][new_col] = 1
    return ans

def replaceO_with_X(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = [submatrix[:] for submatrix in matrix]
    visited = [[False]*n for _ in range(m)]
    queue = []
    for row in range(m):
        if matrix[row][0] == 'O' and not visited[row][0]:
            queue.append([row, 0])
            visited[row][0] = True
        if matrix[row][n-1] == 'O' and not visited[row][n-1]:
            queue.append([row, n-1])
            visited[row][n-1] = True

    for col in range(n):
        if matrix[0][col] == 'O' and not visited[0][col]:
            queue.append([0, col])
            visited[0][col] = True
        if matrix[m-1][col] == 'O' and not visited[m-1][col]:
            queue.append([m-1, col])
            visited[m-1][col] = True

    delta_row = [0, -1, 0, 1]
    delta_col = [-1, 0, 1, 0]
    while queue != []:
        curr = queue[0]
        queue.remove(curr)
        for i in range(4):
            new_row = curr[0] + delta_row[i]
            new_col = curr[1] + delta_col[i]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and not visited[new_row][new_col] and matrix[new_row][new_col] == 'O':
                queue.append([new_row, new_col])
                visited[new_row][new_col] = True
            
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 'O' and not visited[row][col]:
                ans[row][col] = 'X'
    
    return ans

def distinct_islands(matrix):
    m = len(matrix)
    n = len(matrix[0])
    shapes = []
    visited = [[False]*n for _ in range(m)]
    queue = []
    for row in range(m):
        for col in range(n):
            if not visited[row][col] and matrix[row][col] == "1":
                queue.append([row, col])
                visited[row][col] = True
            
            delta_row = [0, -1, 0, 1]
            delta_col = [-1, 0, 1, 0]
            level = 0
            shape = []
            while queue != []:
                size = len(queue)
                for _ in range(size):
                    level += 1
                    curr = queue[0]
                    queue.remove(curr)
                    if level == 1:
                        ini_row = curr[0]
                        ini_col = curr[1]
                    shape.append([curr[0]-ini_row, curr[1]-ini_col])
                    for i in range(4):
                        new_row = curr[0] + delta_row[i]
                        new_col = curr[1] + delta_col[i]
                        if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and not visited[new_row][new_col] and matrix[new_row][new_col] == '1':
                            queue.append([new_row, new_col])
                            visited[new_row][new_col] = True
            if shape not in shapes and shape != []:
                shapes.append(shape)
    return len(shapes)    

def alien_dict(dix, n, k):
    map = {}
    for i in range(k):
        map[chr(ord('a') + i)] = i
    for i in range(n - 1):
        first = dix[i]
        second = dix[i + 1]
        head1 = 0
        head2 = 0
        while head1 < len(first) and head2 < len(second) and first[head1] == second[head2]:
            head1 += 1
            head2 += 1
        if head1 < len(first) and head2 < len(second):
            if map[first[head1]] > map[second[head2]]:
                temp = map[second[head2]]
                map[second[head2]] = map[first[head1]]
                map[first[head1]] = temp
        elif head1 < len(first):
            return "No order Possible"
    return [key for key, value in sorted(map.items(), key = lambda x: x[1])]

def alien_dict_graph(dix, n, k):
    adj_list = [[] for _ in range(k)]
    for i in range(n - 1):
        first = dix[i]
        second = dix[i + 1]
        head1 = 0
        head2 = 0
        while head1 < len(first) and head2 < len(second) and first[head1] == second[head2]:
            head1 += 1
            head2 += 1
        if head1 < len(first) and head2 < len(second):
            adj_list[ord(first[head1]) - ord('a')].append(ord(second[head2]) - ord('a'))
        elif head1 < len(first):
            return "No order Possible"

    stack = []
    visited = [False for _ in range(k)]
    def helper(node, stack):
        visited[node] = True
        for i in adj_list[node]:
            if not visited[i]:
                helper(i, stack)
        stack.append(node)
        
    for i in range(k):
        if not visited[i]:
            helper(i, stack)
    
    return [chr(i + ord('a')) for i in stack[::-1]]

def word_ladder_count1(sw, ew, list_of_words):
    lnth = len(sw)
    queue = []
    queue.append([sw, 0])
    if sw in list_of_words:
        list_of_words.remove(sw)
    chars = [chr(ord('a') + i) for i in range(26)]
    while queue != []:
        curr = queue[0]
        word = curr[0]
        steps = curr[1]
        queue.remove(curr)
        if word == ew:
            return steps
        for i in range(lnth):
            original = word
            for char in chars:
                word = word[:i] + char + word[i+1:]
                if word in list_of_words:
                    queue.append([word, steps + 1])
                    list_of_words.remove(word)
            word = original
    return 0   

def word_ladder_count2(sw, ew, list_of_words):
    lnth = len(sw)
    queue = []
    queue.append([sw, 0])
    if sw in list_of_words:
        list_of_words.remove(sw)
    while queue != []:
        curr = queue[0]
        word = curr[0]
        steps = curr[1]
        queue.remove(curr)
        if word == ew:
            return steps
        i = 0
        while i < len(list_of_words):
            head1 = 0
            head2 = 0
            cnt = 0
            while head1 < lnth:
                if word[head1] != list_of_words[i][head2]:
                    cnt += 1
                head1 += 1
                head2 += 1
            if cnt == 1:
                queue.append([list_of_words[i], steps + 1])
                list_of_words.remove(list_of_words[i]) 
                i -= 1
            i += 1
    return 0

def word_ladder_count_graph(sw, ew, list_of_words):
    # How do I represent a word as node value in a graph?
    # adj_list = [[] for _ in range(len(list))]
    lnth = len(sw)
    queue = []
    queue.append([sw, ''])
    while queue != []:
        curr = queue[0]
        curr_word = curr[0]
        prev_word = curr[1]
        queue.remove(curr)
        if curr_word == ew:
            break
        i = 0
        while i < len(list_of_words):
            head1 = 0
            head2 = 0
            cnt = 0
            while head1 < lnth:
                if curr_word[head1] != list_of_words[i][head2]:
                    cnt += 1
                head1 += 1
                head2 += 1
            if cnt == 1:
                pass
    
def word_ladder_seq(sw, ew, list_of_words):
    lnth = len(sw)
    queue = []
    queue.append([sw])
    if sw in list_of_words:
        list_of_words.remove(sw)
    chars = [chr(ord('a') + i) for i in range(26)]
    ans = []
    while queue != []:
        size = len(queue)
        for _ in range(size):
            seq = queue[0]
            if seq[-1] == ew:
                while queue != []:
                    ans.append(queue[0])
                    queue.remove(queue[0])
                break
            queue.remove(seq)
            for i in range(lnth):
                for char in chars:
                    word = seq[-1][:i] + char + seq[-1][i+1:]
                    if word in list_of_words and word != seq[-1]:
                        temp = [word for word in seq]
                        temp.append(word)
                        queue.append(temp)
        for seq in queue:
            try:
                list_of_words.remove(seq[-1])
            except ValueError:
                pass
    if ans != []:
        out = ""
        for index, seq in enumerate(ans, start = 1):
            result = str(seq[0])
            for word in seq[1:]:
                result += " -> " + word
            out = out + "\n" + str(index) + ". " + result
        return out
    else:
        return -1
    
def word_ladder_seq2(sw, ew, list_of_words):
    lngth = len(sw)
    chars = [chr(ord('a') + i) for i in range(26)]
    queue = []
    queue.append(sw)
    dix = {sw: 0}
    if sw in list_of_words:
        list_of_words.remove(sw)
    while queue != []:
        word = queue[0]
        queue.remove(word)
        if word == ew:
            break
        for i in range(lngth):
            original = word
            for char in chars:
                word = word[:i] + char + word[i+1:]
                if word in list_of_words:
                    dix[word] = dix[original] + 1
                    list_of_words.remove(word)
                    queue.append(word)
            word = original 

    def helper_dfs(word, sw, lngth, chars, dix, seq, ans):
        if word == sw:
            ans.append(seq[::-1])
            return
        for i in range(lngth):
            original = word
            for char in chars:
                word = word[:i] + char + word[i+1:]
                if word in dix and dix[word] < dix[original]:
                    temp = [wrd for wrd in seq]
                    temp.append(word)
                    helper_dfs(word, sw, lngth, chars, dix, temp, ans)
            word = original

    ans = []
    helper_dfs(ew, sw, lngth, chars, dix, [ew], ans)
    if ans != []:
        out = ""
        for index, seq in enumerate(ans, start = 1):
            result = str(seq[0])
            for word in seq[1:]:
                result += " -> " + word
            out = out + "\n" + str(index) + ". " + result
        return out
    else:
        return -1
    
def shortest_distance_in_binary_maze(matrix, src, dest):
    src_rn = src[0]
    src_cn = src[1]
    m = len(matrix)
    n = len(matrix[0])
    dist = [[1e9 for _ in range(n)] for _ in range(m)]
    dist[src_rn][src_rn] = 0
    que = queue.PriorityQueue()
    que.put([0, [src_rn, src_cn]])

    def remove_from_priority_queue(pq, item_to_remove):
            temp_list = []

            # Remove all items from the priority queue, excluding the item to remove
            while not pq.empty():
                item = pq.get()
                if item != item_to_remove:
                    temp_list.append(item)

            # Reinsert items from the temporary list back into the priority queue
            for item in temp_list:
                pq.put(item)

    while not que.empty():
        curr = que.get()
        distance = curr[0]
        rn = curr[1][0]
        cn = curr[1][1]
        delta_row = [0, -1, 0, 1]
        delta_col = [-1, 0, 1, 0]
        remove_from_priority_queue(que, curr)
        for i in range(4):
            new_rn = rn + delta_row[i]
            new_cn = cn + delta_col[i]
            if new_rn >= 0 and new_rn < m and new_cn >= 0 and new_cn < n and matrix[new_rn][new_cn] == '1' and dist[new_rn][new_cn] > 1 + distance:
                if new_rn == dest[0] and new_cn == dest[1]:
                    return 1 + distance
                dist[new_rn][new_cn] = 1 + distance
                que.put([1 + distance, [new_rn, new_cn]])
    return -1

def min_effort_path(matrix):
    m = len(matrix)
    n = len(matrix[0])
    diff = [[1e9 for _ in range(n)] for _ in range(m)]
    diff[0][0] = 0
    que = queue.PriorityQueue()
    que.put([0, [0, 0]])
    delta_row = [0, -1, 0, 1]
    delta_col = [-1, 0, 1, 0]

    def remove_from_priority_queue(pq, item_to_remove):
            temp_list = []

            # Remove all items from the priority queue, excluding the item to remove
            while not pq.empty():
                item = pq.get()
                if item != item_to_remove:
                    temp_list.append(item)

            # Reinsert items from the temporary list back into the priority queue
            for item in temp_list:
                pq.put(item)

    ans = 1e9
    while not que.empty():
        curr = que.get()
        dfrnce = curr[0]
        rn = curr[1][0]
        cn = curr[1][1]
        if rn == m-1 and cn == n-1:
            ans = dfrnce
            return ans
        remove_from_priority_queue(que, curr)
        for i in range(4):
            new_rn = rn + delta_row[i]
            new_cn = cn + delta_col[i]
            if new_rn >= 0 and new_rn < m and new_cn >= 0 and new_cn < n:
                difference = abs(int(matrix[new_rn][new_cn]) - int(matrix[rn][cn]))
                maxi = max(difference, dfrnce)
                if diff[new_rn][new_cn] > maxi:
                    diff[new_rn][new_cn] = maxi
                    que.put([maxi, [new_rn, new_cn]])
    return ans

def min_multiply_to_reach_end(start, end, arr, mod):
    pass
    
if __name__ == "__main__":
    graph = Graph(5, True, True)
    print(f"Cheapest Flights' cost: {graph.cheapest_flights(1, 3, 2)}")
    # num_provinces, provinces = graph.provinces()
    # print(num_provinces, provinces, sep = "\n")

    # num_rows = int(input())
    # matrix = []
    # for i in range(num_rows):
    #     columns = input().split()
    #     matrix.append(columns)

    # print(f"The path has the min. effort equals to = {min_effort_path(matrix)}")

    # print(f"The number of distinct islands: {distinct_islands(matrix)}")

    # print(f"The Transformations required are: {word_ladder_seq2('hit', 'cog', ['hit', 'hot', 'dot', 'lot', 'dog', 'log', 'cog'])}")




    