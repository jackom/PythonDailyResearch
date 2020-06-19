
import numpy as np

b1 = np.arange(36).reshape(2, 3, 6)
print('b1:\n', b1)

b02 = np.all(b1, axis=0, keepdims=True)      # 判断矩阵中 某个轴向上 所有元素是否都为True
print("np.all(b1, axis=0):\n", b02)

b03 = np.any(b1, axis=0, keepdims=True)      # 判断矩阵中 某个轴向上 是否有一个元素为True
# print("np.any(b1, axis=0):\n", b03)


a1 = np.arange(10).reshape(2, 5)
print('a1:\n', a1)

a02 = np.all(a1, axis=0)      # 判断矩阵中 某个轴向上 所有元素是否都为True
print("np.all(a1, axis=0):\n", a02)

print(np.reshape(b02, [18]))

import itertools as it

for i in it.combinations(range(4), 3):
    print(i)

print("\n")

expL = np.exp([0, 1])
print(expL, type(expL))

print("\n")

l = [1, 2, 3, 4]
print(np.array(l).sum())


