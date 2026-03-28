# # Basic triangle
# n = 4

# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()
    
# # Reverse triangle
# n = 4

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()
    
# # Number triangle
# n = 4

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()
    
# Right aligned triangle
n = 4

for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)