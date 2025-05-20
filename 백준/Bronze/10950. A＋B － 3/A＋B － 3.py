num = int(input())
for i in range(num):
    q = input().split(" ")
    q[0] = int(q[0])
    q[1] = int(q[1])

    print(q[0]+q[1])