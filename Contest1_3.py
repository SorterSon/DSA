def pathfinder(a, n):
    i = 0
    j = 0
    path = ""
    count = 1
    while True:
        path += a[i][j]
        if i == 1 and j == n-1:
            break
        if i < 2 and j < n-1 and a[i][j+1] == "0": 
            j = j + 1
        elif i < 1 and j < n and a[i+1][j] == "0": 
            i = i + 1
        else:
            if j < n-1:
                j = j + 1
            else:
                i = i + 1

    i = 0 
    j = 0
    while True:
        if i == 1 and j == n-1:
            break
        if i < 2 and j < n-1 and a[i][j+1] == "0": 
            if a[i+1][j] == "0" and path[j+2:] == a[i+1][j+1:]:
                count += 1
            j = j + 1
        elif i < 1 and j < n and a[i+1][j] == "0": 
            i = i + 1
            break
        else:
            if j < n-1:
                if a[i+1][j] == "1" and path[j+2:] == a[i+1][j+1:]:
                    count += 1
                j = j + 1
            else:
                i = i + 1
        
    return path, count

def num_moves(g, n):

    
if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        a = []
        for i in range(2):
            a.append(input())
        result = pathfinder(a, n)
        print(result[0], result[1], sep = "\n")
        t -= 1