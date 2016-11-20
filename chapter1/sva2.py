# coding: utf-8
"""Sample Variance Example

@author: Liz
@modified: 11-20-2016

"""

import numpy as np
import matplotlib.pyplot as plt

data1 = np.array([1, 5, 18])
data2 = np.array([2, 4, 6, 9, 12, 15, 20])

data1_ssd = sum(i ** 2 for i in (data1 - np.ones_like(data1) * data1.mean()))
data2_ssd = sum(i ** 2 for i in (data2 - np.ones_like(data2) * data2.mean()))

data1_s = data1_ssd / (len(data1) - 1)
data2_s = data2_ssd / (len(data2) - 1)

print("sum of sqd dev 1: {}".format(data1_ssd))
print("sum of sqd dev 2: {}".format(data2_ssd))
print("sample variance 1: {}".format(data1_s))
print("sample variance 2: {}".format(data2_s))


# Graph
x1, x2 = [np.arange(d.size) for d in [data1, data2]]
m1, m2 = [np.ones_like(d) * d.mean() for d in [data1, data2]]

graph = zip([x1, x2],
            [m1, m2],
            [data1, data2],
            [121, 122],
            ["Data1", "Data2"])

for x, m, d, p, t in graph:
    plt.subplot(p)
    plt.scatter(x, d, s=60, label='Data', marker='o')
    plt.plot(x, m, c='g', label='Mean', linestyle='-')
    plt.xlim(x.min(), x.max())

    plt.title(t)
    plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
