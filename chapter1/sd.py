# coding: utf-8
"""Sample Variance Example

@author: Liz
@modified: 11-20-2016

"""

import numpy as np

data1 = np.array([1, 5, 18])
data2 = np.array([2, 4, 6, 9, 12, 15, 20])

data1_ssd = sum(i ** 2 for i in (data1 - np.ones_like(data1) * data1.mean()))
data2_ssd = sum(i ** 2 for i in (data2 - np.ones_like(data2) * data2.mean()))

data1_sd = (data1_ssd / (len(data1) - 1)) ** 0.5
data2_sd = (data2_ssd / (len(data2) - 1)) ** 0.5

print("standard deviation 1: {}".format(data1_sd))
print("standard deviation 2: {}".format(data2_sd))
