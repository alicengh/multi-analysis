# coding: utf-8
"""Sum of Squared Deviation Example1

@author: Liz
@modified: 11-20-2016

"""

import numpy as np

data1 = np.array([2, 5, 7, 12, 15])
data2 = np.array([8, 3, 13, 16, 1])

dev1 = data1 - np.ones_like(data1) * data1.mean()
dev2 = data2 - np.ones_like(data2) * data2.mean()

ssd1 = sum(i ** 2 for i in dev1)  # Amount of info. in data1
ssd2 = sum(i ** 2 for i in dev2)  # Amount of info. in data2

print("Amount of info. in data1: {}".format(ssd1))
print("Amount of info. in data2: {}".format(ssd2))
print("Amount of info. in data : {}".format(ssd1 + ssd2))
