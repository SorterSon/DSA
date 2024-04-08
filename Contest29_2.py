# def optimal_r(a, n, l, u):
#     maxi  = -1e9
#     r = -1
#     check = 0
#     prev_sum = 0
#     sum = 0
#     for i in range(l, n+1):
#         sum = sum + a[i-1]
#         check  = check + sum*(u + 1) - prev_sum*(u + 1) - sum*(sum + 1)/2 + prev_sum*(prev_sum + 1)/2
#         prev_sum = sum
#         if maxi < check:
#             r = i + 1
#             maxi = check
#     return r-1
    

if __name__ == "__main__":
    t = int(input())
    while t:
        pass
        # n = int(input())
        # a = [int(i) for i in input().split()]
        # q = int(input())
        # for _ in range(q):
        #     l_and_u = input().split()
        #     l = int(l_and_u[0])
        #     u = int(l_and_u[1])
        #     print(optimal_r(a, n, l, u), end = " ")
        # print()
        # t -= 1
    