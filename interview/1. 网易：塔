'''
小易有一些立方体，每个立方体的边长为1，他用这些立方体搭了一些塔。
现在小易定义：这些塔的不稳定值为它们之中最高的塔与最低的塔的高度差。
小易想让这些塔尽量稳定，所以他进行了如下操作：每次从某座塔上取下一块立方体，并把它放到另一座塔上。
注意，小易不会把立方体放到它原本的那座塔上，因为他认为这样毫无意义。
现在小易想要知道，他进行了不超过k次操作之后，不稳定值最小是多少

输入描述：
第一行两个数n,k (1 <= n <= 100, 0 <= k <= 1000)表示塔的数量以及最多操作的次数。
第二行n个数，ai(1 <= ai <= 104)表示第i座塔的初始高度。

输出描述：
第一行两个数s, m，表示最小的不稳定值和操作次数(m <= k)
接下来m行，每行两个数x,y表示从第x座塔上取下一块立方体放到第y座塔上。   

输入例子：
3 2
5 8 5

输出例子：
0 2
2 1
2 3

下面代码通过率为90%。
'''
n, k = raw_input().strip().split()
n, k = int(n), int(k)
tnums = [int(s) for s in raw_input().strip().split()]
op = 0
result = []
maxt, mint = max(tnums), min(tnums)
maxi, mini = tnums.index(maxt), tnums.index(mint)
while maxt > mint + 1:
    while maxt > mint + 1 and op <= k:
        op += 1
        tnums[mini] += 1
        tnums[maxi] -= 1
        result.append([maxi + 1, mini + 1])
        maxt -= 1
        mint += 1
    maxt, mint = max(tnums), min(tnums)
    maxi, mini = tnums.index(maxt), tnums.index(mint)
print maxt - mint, op
for i, j in result:
    print i, j
