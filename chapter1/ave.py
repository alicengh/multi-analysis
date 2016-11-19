# coding: utf-8
"""Average Example

@author: Liz
@modified: 11-20-2016

"""

import numpy as np
import matplotlib.pyplot as plt

data = np.array([2, 5, 7, 12, 15])

print("data: {}".format(data))
print("ave : {}".format(data.mean()))


# Graph
x = np.arange(data.size)
mean = np.ones_like(data) * data.mean()

fig = plt.figure()
plt.scatter(x, data, s=60, label='Data', marker='o')
plt.plot(x, mean, c='g', label='Mean', linestyle='-')
plt.xlim(x.min(), x.max())
plt.legend(loc='upper left')

plt.show()
