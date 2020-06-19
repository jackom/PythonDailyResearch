import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

arr1 = np.ones((3, 3))
print("arr1>>>", arr1)

import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(a[0:1])  # 截取第一行,返回 [[1 2 3 4 5]]
print(a[1, 2:5])  # 截取第二行，第三、四、五列，返回 [8 9 10]

print(a[1, :])  # 截取第二行,返回 [ 6  7  8  9 10]

print("\n测试 X, y\n")
X = a[:, 0:2]
y = a[:, 2]
print(X)
print(y)

array = [[0.33986, 0.71199, 0],
         [0.34447, 0.81433, 0],
         [0.28226, 0.82602, 0],
         [0.26613, 0.75, 1],
         [0.26613, 0.63596, 0],
         [0.32604, 0.54825, 1],
         [0.28917, 0.65643, 0]]
a = np.asarray(array)
print("a>>>", a)
print("\n打印 X, y\n")
X = a[:, 0:2]
y = a[:, 2]
print(X)
print(y)

print('\n')
l = [2, 3, 1, 4, 7]
for index, item in enumerate(l):
    print('index: ', index)
    print('item: ', item)

x = np.arange(6).reshape(2, 3)
print('test: ', x)
print('test1: ', np.nonzero(x))
print('test2: ', np.transpose(np.nonzero(x)))
print('argwhere: ', np.argwhere(x > 1))
print('flatten: ', np.argwhere(x > 1).flatten())

print('eye: ', np.eye(4, dtype=int))
print('eye2: ', np.eye(3, 4, k=2, dtype=int))
print('eye3: ', np.eye(3, 4, k=-1, dtype=int))

import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

a = [(1, 'a'), (2, 5)]
print('zip* ', list(zip(*a)))

a = [1, 2, 3]
b = [5, 4, 6]
zipped = list(zip(a, b))
print('zip ', zipped)
print('zip* ', list(zip(*zipped)))
# l = [(1, 5), (2, 4), (3, 6)]
# print('zip* ', list(zip(*l)))


a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5])
print('a + b: ', a * b)
print('sum: ', sum(a * b))

# np.arange(5) 中产生一个size为3的随机采样:
print('choice: ', np.random.choice(5, 3))
# 从 np.arange(5) 中产生一个非标准的 size为 3的随机采样: 其中，由于下标index为3时概率为0.6，所以相对来说3出现的几率最大
print('choice2: ', np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]))
print('choice3: ', np.random.choice(np.arange(2), p=[0.8, 0.2]))
print('choice4: ', np.random.choice(np.arange(2), p=[0.2, 0.8]))

from collections import defaultdict

dict1 = defaultdict(list)
a = lambda: np.zeros(2)
dict2 = defaultdict(a)
print('defaultDict:  ', len(dict1))
print('defaultDict a:  ', a)
print('defaultDict2:  ', len(dict2))

Q = {'a': 1, 'b': 5, '4': 'c'}
policy = dict((k, v) for k, v in Q.items())
print('policy: ', policy)

x = np.hstack((np.ones(10), 10 * np.ones(10)))
print('x: ', x)

a = np.ones(10)
print('a: ', a)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.vstack((arr1, arr2)))

print(np.hstack((arr1, arr2)))

a1 = np.array([[1, 2], [3, 4], [5, 6]])
a2 = np.array([[7, 8], [9, 10], [11, 12]])
print(a1)
print(a2)
print(np.hstack((a1, a2)))

print(np.arange(0, .3, .01))

print(np.round(12.01, 4))

print("\n")

V_opt = np.zeros((4, 12))
temp = np.arange(3, 15)
print("V_opt_first", temp)

print("\n")

V_opt[0:13][0] = -temp[::-1]
print(V_opt)

V_opt[0:13][1] = -temp[::-1] + 1
V_opt[0:13][2] = -temp[::-1] + 2
V_opt[3][0] = -13

print("\n")

print(V_opt)

import random

l1 = [1, 2, 3, 4, 10]
print("random: ", random.choice(l))

qline = {'u': 1.2, 'l': 27, 'r': -2.1, 'd': -24.5}
value_max = qline.get("u")
key_max = None
for k, v in qline.items():
    if value_max < v:
        value_max = v
        key_max = k
action = key_max
print("action: ", action)

qline = {'u': 1.2, 'r': -2.1, 'd': -24.5, 'l': 27}

action = max(qline, key=qline.get)
print("max action: ", action)
print("\n")

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

print(df)

print("随机数", random.Random().randint(1, 10))

import seaborn as sns

df2 = pd.DataFrame({'A': [1., 2.0, 3.0, 2.0],
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)

df2.isnull().any(axis=0)

fruits = pd.Series(data=[10, 6, 3, 5], index=['apples', 'oranges', 'bananas', 'oranges'])
print(fruits)

fruits.replace()

# print(fruits.groupby(''))

print(df2)
df2['A'].loc[df2['A'] == 2] = 5
print(df2)

print("\n分割线\n")

df2.loc[df2.A == 5.0, 'A'] = ''
print(df2)

print("\n分割线\n")

df = pd.date_range('2020-1-21', periods=15)
print(df)

aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)

cList = [123, 'xyz', 'zara', 'abc', 123, bList]

print(aList)
print("\n")
print(cList)
print("\n")

df3 = pd.DataFrame({'A': [1., 2.0, 3.0, 2.0],
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

new_df = pd.concat([df2, df3], axis=0, ignore_index=True)
print(new_df)
print("\n")

print(new_df.B.dt.year)

df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})

print(pd.get_dummies(df, prefix=['col1', 'col2']))

print('\n')

import pickle

for index, row in df.iterrows():
    print(index)
    print('\n')
    print(row)
    print('\n')

print('\n')

for row in df.iterrows():
    print(row)

print('\n')

print(df[['A', 'B']])
print('\n')

x = np.arange(6)
arg_where = np.argwhere(x > 1)
print(arg_where)
print('\n')
print(arg_where.flatten())
print('\n')

print(int(False) == False)

print(np.random.rand(1))

print("\n")

series = pd.Series([0, 1, 1, 0, 1, 1, 0])

print(len(series))

print("\n")


def iq_test(numbers):
    even_map = {}
    odd_map = {}
    data = numbers.split(" ")
    for index, value in enumerate(data):
        if int(value) % 2 == 0:
            even_map[index + 1] = int(value)
        else:
            odd_map[index + 1] = int(value)
    if len(even_map) > len(odd_map):
        # return odd_map.keys()[0]
        return list(odd_map.keys())[0]
    else:
        # return even_map.keys()[0]
        return list(even_map.keys())[0]


print(iq_test("2 4 7 8 10"))

print("\n")

stop_words_1 = ['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑', '助理',
                'Assistants',
                'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced', 'and', 'distributed']
s = '  作曲  毛不易\n 作词  毛不易\n编曲Arranger ：赵兆 宋涛\n\n借一盏午夜街头 昏黄'


# 去掉停用词
def remove_stop_words(f, stop_words):
    for word in stop_words:
        f = f.replace(word, '')
    print(f)
    return f


remove_stop_words(s, stop_words_1)

