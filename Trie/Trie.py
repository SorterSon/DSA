class Node:

    def __init__(self):
        self.array = [None]*26
        self.flag = False

    def check(self, char):
        return self.array[ord(char) - ord('a')] != None
    
    def put(self, char, new_node):
        self.array[ord(char) - ord('a')] = new_node

    def get(self, char):
        return self.array[ord(char) - ord('a')]
    
    def set_end(self):
        self.flag = True
    
    def is_end(self):
        return self.flag == True

class Trie:
    
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if not node.check(char):
                new_node = Node()
                node.put(char, new_node)

            node = node.get(char)
        
        node.set_end()

    def search(self, word):
        node = self.root
        for char in word:
            if not node.check(char):
                return False
            
            node = node.get(char)

        return node.is_end()
    
    def starts_with(self, word):
        node = self.root
        for char in word:
            if not node.check(char):
                return False
            
            node = node.get(char)

        return True