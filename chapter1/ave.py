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

fig, ax = plt.subplots()
data_line = ax.plot(x, data, label='Data', marker='o')
mean_line = ax.plot(x, mean, label='Mean', linestyle='-')
legend = ax.legend(loc='upper left')

plt.show()
