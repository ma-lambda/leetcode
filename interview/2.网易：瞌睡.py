'''
时间限制：1秒
空间限制：262144K
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知道了小易对一堂课每分钟知识点
的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易
这堂课听到的知识点分值。 

输入描述：
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。

输出描述：
小易这堂课听到的知识点的最大兴趣值。

输入例子：
6 3
1 3 5 2 5 4
1 1 0 1 0 0

输出例子：16

下面的代码通过率为20，需进行优化。
'''
import sys
n, k = raw_input().strip().split()
n, k = int(n), int(k)
score = [int(s) for s in raw_input().strip().split()]
isawake = [int(a) for a in raw_input().strip().strip().split()]
score_awake = []
for i in range(n):
    score_awake.append(score[i] if isawake[i] else 0)
score_cumsum = [0] * n
score_cumsum[-1] = score_awake[-1]
for i in range(n - 2, -1, -1):
    score_cumsum[i] = score_cumsum[i + 1] + score_awake[i]
value = 0
i = 0
maxvalue = 0
while i < n:
    value += score_awake[i]
    if not isawake[i]:
        right = i + k if i + k <= n else n
        if i + k > n:
            curvalue = value + sum(score[i:n])
        else:
            curvalue = value + sum(score[i:right])
            if right != n:
                curvalue += score_cumsum[right]
        if curvalue > maxvalue:
            maxvalue = curvalue
    i += 1
print maxvalue
