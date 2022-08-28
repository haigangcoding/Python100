# -*- coding:UTF-8 -*-
# 有四个数字: 1, 2, 3, 4, 能组成互不相同而且无重复数字的三位数？各是多少？
# 在百位, 十位, 个位的数字都是 1, 2, 3, 4。 组成所有的排列后再去掉不满足的条件的排列

# 解法 1
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != k) and (i != j) and (j != k):
                print(i, j, k)

# 解法 2
for a in [1, 2, 3, 4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            if a != b and b != c and a != c:
                print(a, b, c, sep="")
