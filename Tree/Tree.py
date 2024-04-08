class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Node2:

    def __init__(self, value, num = 1):
        self.data = value
        self.num = num
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    def add_node(self):
        pass

    def bfs(self, root = None):
        if root == None:
            return 'Empty Tree'
        q = []
        q.append(root)
        while q != []:
            curr = q[0]
            print(f"{curr.data} -> ", end = "")
            q = q[1:]
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)

    def levelorder_bfs(self):
        q = []
        result = ""
        q.append(self.root)
        while q != []:
            curr = q[0]
            q = q[1:]
            result += str(curr.data) + " -> "
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        print(result[:-4])

    def preorder_dfs(self):
        if self.root == None:
            return None
        s = []
        result = ""
        s.append(self.root)
        while s != []:
            curr = s[-1]
            result += str(curr.data) + " -> "
            s = s[:-1]
            if curr.right != None:
                s.append(curr.right)
            if curr.left != None:
                s.append(curr.left)
            
        print(result[:-4])

    def inorder_dfs(self):
        if self.root == None:
            return None
        s = []
        s.append(self.root)
        left = False
        result = ""
        while s != []:
            curr = s[-1]
            if curr.left != None and left == False:
                s.append(curr.left)
            else:
                result += str(curr.data) + " -> "
                s = s[:-1]
                if curr.right != None:
                    s.append(curr.right)
                    left = False
                else:
                    left = True
        return result[:-4]

    def inorder_dfs2(self):
        if self.root == None:
            return None
        s = []
        result = ""
        curr = self.root
        while True:
            if curr != None:
                s.append(curr)
                curr = curr.left
            else:
                if s == []:
                    return result
                curr = s[-1]
                result += str(curr.data) + " -> "
                s = s[:-1]
                curr = curr.right
        return result[:-4]

    def postorder_dfs(self):
        s = []
        curr = self.root
        result = ""
        while curr != None or s != []:
            if curr != None:
                s.append(curr)
                curr = curr.left
            else:
                top = s[-1].right
                if top == None:
                    top = s[-1]
                    result += str(top.data) + " -> "
                    s = s[:-1]
                    while s != [] and top == s[-1].right:
                        top = s[-1]
                        s = s[:-1]
                        result += str(top.data) + " -> "
                else: 
                    curr = top
        print(result[:-4])

    def postorder_dfs2(self):
        s1 = []
        s2 = []
        s1.append(self.root)
        result = ""
        while s1 != []:
            curr = s1[-1]
            s1 = s1[:-1] 
            s2.append(curr)
            if curr.left != None:
                s1.append(curr.left)
            if curr.right != None:
                s1.append(curr.right)

        while s2 != []:
            curr2 = s2[-1]
            s2 = s2[:-1]
            result += str(curr2.data) + " -> "

        print(result[:-4])

    def one_for_all_dfs(self):
        if self.root == None:
            return None
        s = []
        s.append([self.root, 1])
        preorder = ""
        inorder = ""
        postorder = ""
        while s != []:
            curr = s[-1]
            if curr[1] == 1:
                preorder += str(curr[0].data) + " -> "
                if curr[0].left != None:
                    s.append([curr[0].left, 1])
            elif curr[1] == 2:
                inorder += str(curr[0].data) + " -> "
                if curr[0].right != None:
                    s.append([curr[0].right, 1])
            elif curr[1] == 3:
                postorder += str(curr[0].data) + " -> "
                s.pop()
            curr[1] += 1

        return (preorder[:-4], inorder[:-4], postorder[:-4])
    
    def min_depth_1(self):
        if self.root == None:
            return 0
        q = []
        q.append(self.root)
        level = 0
        while q != []:
            size = len(q)
            level += 1
            for _ in range(size):
                curr = q[0]
                q = q[1:]
                if curr.left == None and curr.right == None:
                    return level
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)

    def __helper_min_depth(self, root):
        if root == None:
            return 1e9
        if root.left == None and root.right == None:
            return 1
        lh = self.__helper_min_depth(root.left)
        rh = self.__helper_min_depth(root.right)
        return 1 + min(lh, rh)
    
    def min_depth_2(self):
        if self.root == None:
            return 0
        return self.__helper_min_depth(self.root)

    def max_depth_1(self):
        if self.root == None:
            return 0
        q = []
        q.append(self.root)
        level = 0
        while q != []:
            size = len(q)
            level += 1  
            for _ in range(size):
                curr = q[0]
                q = q[1:]
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
        return level
    
    def max_depth_2(self, root):
        if root == None:
            return 0
        lt = self.max_depth_2(root.left)
        rt = self.max_depth_2(root.right)
        return 1 + max(lt, rt)
    
    def __helper_balanced(self, root):
        if root == None:
            return 0
        lh = self.__helper_balanced(root.left)
        rh = self.__helper_balanced(root.right)
        if lh == -1 or rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)
        
    def check_balanced(self):
        return self.root == None or self.__helper_balanced(self.root) != -1
    
    def diameter(self, root, maxi):
        if root == None:
            return 0
        lh = self.diameter(root.left, maxi)
        rh = self.diameter(root.right, maxi)
        maxi[0] = max(maxi[0], lh + rh)
        return 1 + max(lh, rh)
    
    def max_path_sum(self, root, maxsum):
        if root == None:
            return 0
        lval = max(0, self.max_path_sum(root.left, maxsum))
        rval = max(0, self.max_path_sum(root.right, maxsum))
        maxsum[0] = max(maxsum[0], lval + rval + root.data)
        return root.data + max(lval, rval)

    def zig_zag_bfs(self):
        if self.root == None:
            return None
        dq = []
        result = ""
        level = 1
        dq.append(self.root)
        while dq != []:
            size = len(dq)
            if level % 2:
                for _ in range(size):
                    curr = dq[-1]
                    result += str(curr.data) + " -> "
                    dq.pop()
                    if curr.left != None:
                        # Below operation is costly in case of List
                        dq.insert(0, curr.left)
                    if curr.right != None:
                        # Below operation is costly in case of List
                        dq.insert(0, curr.right)
            else:
                for _ in range(size):
                    curr = dq[0]
                    result += str(curr.data) + " -> "
                    # Below operation is costly in case of List
                    dq.remove(curr)
                    if curr.right != None:
                        dq.append(curr.right)
                    if curr.left != None:
                        dq.append(curr.left)
            level += 1
        return result[:-4]
    
    def zig_zag_bfs2(self):
        if self.root == None:
            return None
        q = []
        result = ""
        flag = 1
        q.append(self.root)
        while q != []:
            size = len(q)
            temp = ""
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if flag:
                    temp += str(curr.data) + " -> "
                else:
                    temp = str(curr.data) + " -> " + temp
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
            result += temp
            flag = 1 - flag
        return result[:-4]
    
    def boundary_traversal(self):
        if self.root == None:
            return None
        curr = self.root
        result = ""
        while curr != None:
            if curr.left == None and curr.right == None:
                break
            result += str(curr.data) + " -> "
            if curr.left != None:
                curr = curr.left
            else:
                curr = curr.right

        def helper_inorder(root):
            if root == None:
                return None
            s = []
            result = ""
            curr = root
            while True:
                if curr != None:
                    s.append(curr)
                    curr = curr.left
                else:
                    if s == []:
                        return result
                    curr = s[-1]
                    if curr.left == None and curr.right == None:
                        result += str(curr.data) + " -> "
                    s = s[:-1]
                    curr = curr.right
            return result[:-4]
        
        result += helper_inorder(self.root)

        s = []
        curr = self.root.right
        temp = ""
        while curr != None:
            if curr.left == None and curr.right == None:
                break
            s.append(curr)
            if curr.right != None:
                curr = curr.right
            else:
                curr = curr.left
            
        while s != []:
            result += str(s[-1].data) + " -> "
            s.pop()

        return result[:-4]
    
    def vertical_order_traversal(self):
        if self.root == None:
            return None
        bar = 0
        level = 0
        result = []
        q = []
        q.append([bar, level, self.root])
        while q != []:
            size = len(q)
            level += 1
            for _ in range(size):
                curr = q[0]
                result.append([curr[0], curr[1], curr[2].data])
                q.remove(curr)
                if curr[-1].left != None:
                    q.append([curr[0]-1, level, curr[-1].left])
                if curr[-1].right != None:
                    q.append([curr[0]+1, level, curr[-1].right])
        result = sorted(result, key = lambda x: (x[0], x[1], x[2]))
        
        output = [[result[0][2]]]
        for i in range(1, len(result)):
            if result[i][0] == result[i-1][0]:
                output[-1].append(result[i][2])
            else:
                output.append([result[i][2]])
        return output
    
    def top_view(self):
        temp = self.vertical_order_traversal()
        return [item[0] for item in temp]

    def top_view2(self):
        if self.root == None:
            return None
        bar = 0
        q = []
        result = []
        list_of_bars = []
        q.append([bar, self.root])
        while q != []:
            size = len(q)
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if curr[0] not in list_of_bars:
                    result.append([curr[0], curr[1].data])
                    list_of_bars.append(curr[0])
                if curr[1].left != None:
                    q.append([curr[0]-1, curr[1].left])
                if curr[1].right != None:
                    q.append([curr[0]+1, curr[1].right])
        result = sorted(result, key = lambda x: (x[0], x[1]))
        return [item[1] for item in result]
    
    def bottom_view(self):
        temp = self.vertical_order_traversal()
        return [item[-1] for item in temp]
    
    # This method fails for collisions along a line
    # def bottom_view2(self):
    #     if self.root == None:
    #         return None
    #     bar = 0
    #     s = []
    #     result = []
    #     list_of_bars = []
    #     bar = 0
    #     node = self.root
    #     while True:
    #         if node != None:
    #             s.append([bar, node])
    #             node = node.left
    #             bar -= 1
    #         else:
    #             if s == []:
    #                 break
    #             bar = s[-1][0]
    #             node = s[-1][1]
    #             s.pop()
    #             if bar not in list_of_bars:
    #                 result.append([bar, node.data])
    #                 list_of_bars.append(bar)
    #             node = node.right
    #             bar += 1
    #     result = sorted(result, key = lambda x: (x[0], x[1]))
    #     return [item[1] for item in result]

    def bottom_view2(self):
        if self.root == None:
            return None
        bar = 0
        level = 0
        q = []
        dix = {}
        list_of_bars = []
        q.append([bar, self.root])
        while q != []:
            size = len(q)
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if curr[0] not in dix.keys() or dix[curr[0]][1] != level or dix[curr[0]][0] < curr[1].data:
                    dix[curr[0]] = [curr[1].data, level]
                if curr[1].left != None:
                    q.append([curr[0]-1, curr[1].left])
                if curr[1].right != None:
                    q.append([curr[0]+1, curr[1].right])
            level += 1
        dix = dict(sorted(dix.items(), key = lambda x: (x[0], x[1][0])))
        return [item[1][0] for item in dix.items()]
    
    def left_view(self):
        if self.root == None:
            return None
        q = []
        result = []
        q.append(self.root)
        while q != []:
            size = len(q)
            count = 1
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if count == 1:
                    result.append(curr.data)
                    count -= 1
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
        return result
    
    def left_view2(self):
        if self.root ==  None:
            return None
        def helper(root, level, output):
            if root == None:
                return 
            if level == len(output):
                output.append(root.data)
            helper(root.left, level+1, output)
            helper(root.right, level+1, output)
        output = []
        helper(self.root, 0, output)
        return output
    
    def right_view(self):
        if self.root == None:
            return None
        q = []
        result = []
        q.append(self.root)
        while q != []:
            size = len(q)
            count = 1
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if count == 1:
                    result.append(curr.data)
                    count -= 1
                if curr.right != None:
                    q.append(curr.right)
                if curr.left != None:
                    q.append(curr.left)
        return result
    
    def right_view2(self):
        if self.root ==  None:
            return None
        def helper(root, level, output):
            if root == None:
                return 
            if level == len(output):
                output.append(root.data)
            helper(root.right, level+1, output)
            helper(root.left, level+1, output)
        output = []
        helper(self.root, 0, output)
        return output
    
    def path_from_root(self, val):
        if self.root == None:
            return
        arr = []
        curr = self.root
        while curr != None or arr != []:
            if curr != None:
                arr.append(curr)
                if curr.data == val:
                    break
                curr = curr.left
            else:
                temp = arr[-1].right
                if temp == None:
                    temp = arr[-1]
                    arr.pop()
                    while arr != [] and temp == arr[-1].right:
                        temp = arr[-1]
                        arr.pop()
                else:
                    curr = temp
        if arr == []:
            return -1
        else:
            return [item.data for item in arr]   

    def path_from_root2(self, val):
        if self.root == None:
            return None
        arr = []
        def helper(root, val):
            if root == None:
                return False
            arr.append(root.data)
            if root.data == val:
                return True
            ls = helper(root.left, val)
            rs = helper(root.right, val)
            if ls or rs:
                return True
            else:
                arr.pop()
                return False
            
        helper(self.root, val)
        if arr == []:
            return -1
        else:
            return arr
        
    def lowest_common_ancestor(self, val1, val2):
        arr1 = self.path_from_root(val1)
        arr2 = self.path_from_root(val2)
        i = 0
        while i < len(arr1) and i < len(arr2) and arr1[i] == arr2[i]:
            i += 1
        return arr1[i-1]
    
    # def lowest_common_ancestor2(self, val1, val2):
    #     if self.root == None:
    #         return None
    #     arr = []
    #     lca = -1
    #     curr = self.root
    #     while curr != None or arr != []:
    #         while lca == -1:
    #             if curr != None:
    #                 arr.append(curr.left)
    #                 if curr.data == val1 or curr.data == val2:
    #                     lca = curr.data
    #                     break
    #                 curr = curr.left
    #             else:
    #                 temp = arr[-1].right
    #                 if temp == None:
    #                     temp = arr[-1]
    #                     arr.pop()
    #                     while arr != [] and temp == arr[-1].right:
    #                         temp = arr[-1]
    #                         arr.pop()
    #                 else:
    #                     curr = temp
    #         else:
    #             if curr != None:
    #                 arr.append(curr.left)

    def lowest_common_ancestor(self, val1, val2):
        if self.root == None:
            return None
        def helper(root, val1, val2):
            if root == None:
                return None
            if root.data == val1 or root.data == val2:
                return root
            ls = helper(root.left, val1, val2)
            rs = helper(root.right, val1, val2)
            if ls != None and rs != None:
                return root
            elif ls != None:
                return ls
            else: 
                return rs
        return helper(self.root, val1, val2).data

    # Fails for 
    '''
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.left.left.left = Node(6)
    tree.root.right.right.right = Node(7)
    '''
    # kind of tree
    # def tree_max_width(self):
    #     if self.root == None:
    #         return None
    #     index = 1
    #     maxi = 1
    #     q = []
    #     q.append([self.root, index])
    #     while q != []:
    #         size = len(q)
    #         maxi = max(maxi, q[-1][-1] - q[0][-1] + 1)
    #         for _ in range(size):
    #             curr = q[0]
    #             q.remove(curr)
    #             index += 1
    #             if curr[0].left != None:
    #                 q.append([curr[0].left, index])
    #             index += 1
    #             if curr[0].right != None:
    #                 q.append([curr[0].right, index])
    #     return maxi
    
    # Can lead to a memory overflow!
    def tree_max_width(self):
        if self.root == None:
            return None
        maxi = 1
        q = []
        q.append([self.root, 1])
        while q != []:
            size = len(q)
            maxi = max(maxi, q[-1][-1] - q[0][-1] + 1)
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if curr[0].left != None:
                    q.append([curr[0].left, 2*curr[1]])
                if curr[0].right != None:
                    q.append([curr[0].right, 2*curr[1] + 1])
        return maxi
    
    def tree_max_width2(self):
        if self.root == None:
            return None
        q = []
        maxi = 1
        q.append([self.root, 0])
        while q != []:
            size = len(q)
            min_index = q[0][-1]
            maxi = max(maxi, q[-1][-1] - q[0][-1] + 1)
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if curr[0].left != None:
                    q.append([curr[0].left, 2*(curr[1] - min_index) + 1])
                if curr[0].right != None:
                    q.append([curr[0].right, 2*(curr[1] - min_index) + 2])

        return maxi
    
    def parent_labeler(self):
        parents = {}
        q = []
        q.append(self.root)
        while q != []:
            size = len(q)
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if curr.left != None:
                    q.append(curr.left)
                    parents[curr.left] = curr
                if curr.right != None:
                    q.append(curr.right)
                    parents[curr.right] = curr
        return parents
    
    def at_distance_k(self, value, k):
        if self.root == None:
            return None
        parents = self.parent_labeler()
        output = []
        
        def node_finder(root, value):
            if root == None:
                return None
            if root.data == value:
                return root
            ls = node_finder(root.left, value)
            if ls != None:
                return ls
            rs = node_finder(root.right, value)
            return rs

        target = node_finder(self.root, value)

        def helper_bfs(root, distance):
            if distance == 0:
                return [root]
            q = []
            result = ""
            q.append(root)
            while q != []:
                size = len(q)
                distance -= 1
                for _ in range(size):
                    curr = q[0]
                    q.remove(curr)
                    if curr.left != None:
                        q.append(curr.left)
                    if curr.right != None:
                        q.append(curr.right)
                if distance == 0:
                    return q

        output.extend(helper_bfs(target, k))
        
        def helper(curr, distance):
            if curr == self.root:
                return
            parent = parents[curr]
            if distance == 1:
                return [parent]
            if parent.left == target:
                output.extend(helper_bfs(parent.right, distance-2))
                temp = helper(parent, distance - 1) 
            else:
                output.extend(helper_bfs(parent.left, distance-2))
                temp = helper(parent, distance - 1) 

        if k > 0:
            helper(target, k)
        
        return [item.data for item in output]
    
    def at_distance_k2(self, value, k):
        if self.root == None:
            return 
        parents = self.parent_labeler()
        visited = {}
        def node_finder(root, value):
            if root == None:
                return None
            if root.data == value:
                return root
            ls = node_finder(root.left, value)
            if ls != None:
                return ls
            rs = node_finder(root.right, value)
            return rs

        target = node_finder(self.root, value)
        q = []
        q.append(target)
        visited[target] = True
        while q != []:
            if k == 0:
                return [item.data for item in q]
            size = len(q)
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if curr.left != None and visited.get(curr.left, False) == False:
                    q.append(curr.left)
                    visited[curr.left] = True
                if curr.right != None and visited.get(curr.right, False) == False:
                    q.append(curr.right)
                    visited[curr.right] = True
            if curr != self.root and visited.get(parents[curr], False) == False:
                q.append(parents[curr])
                visited[parents[curr]] = True 
            k -= 1
    def burn_time(self, value):
        if self.root == None:
            return None
        parents = self.parent_labeler()

        def node_finder(root, value):
            if root == None:
                return None
            if root.data == value:
                return root
            ls = node_finder(root.left, value)
            if ls != None:
                return ls
            rs = node_finder(root.right, value)
            return rs

        target = node_finder(self.root, value)
        time = 0
        visited = {}
        q = []
        q.append(target)
        visited[target] = True
        while q != []:
            size = len(q)
            flag = False
            for _ in range(size):
                curr = q[0]
                q.remove(curr)
                if curr.left != None and visited.get(curr.left, False) == False:
                    q.append(curr.left)
                    visited[curr.left] = True
                    flag = True
                if curr.right != None and visited.get(curr.right, False) == False:
                    q.append(curr.right)
                    visited[curr.right] = True
                    flag = True
            if curr != self.root and visited.get(parents[curr], False) == False:
                q.append(parents[curr])
                visited[parents[curr]] = True 
                flag = True
            if flag:
                time += 1
        
        return time
    
    def count_complete_nodes(self):
        if self.root == None:
            return None
        def helper(root):
            lh = 0
            rh = 0
            curr = root
            while curr != None:
                curr = curr.left
                lh += 1
            while curr != None:
                curr = curr.right
                rh += 1
            if lh == rh:
                return 2**lh - 1
            else:
                return 1 + helper(root.left) + helper(root.right)
        count = helper(self.root)

        return count
    
    def serialize(self):
        string = ""
        if self.root == None:
            return string
        q = []
        q.append(self.root)
        string += str(self.root.data) + " -> "
        while q != []:
            size = len(q)
            for _ in q:
                curr = q[0]
                q.remove(curr)
                if curr.left != None:
                    q.append(curr.left)
                    string += str(curr.left.data) + " -> "
                else: 
                    string += '# -> '
                if curr.right != None:
                    q.append(curr.right)
                    string += str(curr.right.data) + " -> "
                else: 
                    string += '# -> '
        return string[:-4]
    
    def deserialize(self, string):
        if string == "":
            return None
        i = 0
        tree = Tree()
        tree.root = Node(int(string[0]))
        i += 5
        q = []
        q.append(tree.root)
        while q != []:
            size = len(q)
            for _ in range(size):
                curr = q[0]
                lval = int(string[i])
                if lval != "#":
                    curr.left = Node(lval)
                    q.append(curr.left)
                i += 5
                rval = int(string[i])
                if rval != "#":
                    curr.right = Node(rval)
                    q.append(curr.right)
                i += 5
            return tree.root
    
class BST():

    def __init__(self):
        self.root = None

    def bfs(self, root = None):
        if root == None:
            return 'Empty Tree'
        q = []
        q.append(root)
        while q != []:
            curr = q[0]
            print(f"{curr.data} -> ", end = "")
            q = q[1:]
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)

    def search(self, val):
        curr = self.root
        
        while True:
            if curr == None:
                return None
            if curr.data == val:
                return curr
            elif curr.data < val:
                curr = curr.right
            else:
                curr = curr.left

    def ceiling(self, val):
        curr = self.root
        ceil = None
        while True:
            if curr == None:
                return ceil
            if curr.data == val:
                ceil = curr
                return ceil
            elif curr.data < val:
                curr = curr.right
            else:
                ceil = curr
                curr = curr.left

    def floor(self, val):
        curr = self.root
        floor = None
        while True:
            if curr == None:
                return floor
            if curr.data == val:
                floor = curr
                return floor
            elif curr.data > val:
                curr = curr.left
            else:
                floor = curr
                curr = curr.right
        
    def insert_node(self, val):
        curr = self.root
        node = Node(val)
        while True:
            if curr == None:
                curr = node
                return
            if curr.data < val:
                if curr.right == None:
                    curr.right = node
                    return 
                curr = curr.right
            else:
                if curr.left == None:
                    curr.left = node
                    return 
                curr = curr.left
                
if __name__ == "__main__":
    tree = BST()
    # tree.root = Node(1)
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)
    # tree.root.left.left = Node(4)
    # tree.root.left.right = Node(5)
    # tree.root.left.right.left = Node(6)
    # tree.root.left.right.right = Node(7)

    # ans = tree.one_for_all_dfs()
    # print(f"preorder: {ans[0]}\ninorder: {ans[1]}\npostorder: {ans[2]}")
    # print(tree.max_depth_1())
    # maxi = [0]
    # tree.max_path_sum(tree.root, maxi)
    # print(maxi[0])
   
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(13)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(6)
    tree.root.right.left = Node(11)
    tree.root.right.right = Node(14)
    tree.root.left.right.right = Node(9)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.right = Node(4)
    tree.root.left.right.right.left = Node(7)
 
    tree.insert_node(8)
    tree.bfs(tree.root)
             
        

