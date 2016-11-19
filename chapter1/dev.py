# coding: utf-8
"""Deviation Example

@author: Liz
@modified: 11-20-2016

"""

import numpy as np

data = np.array([2, 5, 7, 12, 15])
dev = data - np.ones_like(data) * data.mean()

print("data: {}".format(data))
print("ave : {}".format(data.mean()))
print("dev : {}".format(dev))
print("sum of dev: {}".format(sum(dev)))
