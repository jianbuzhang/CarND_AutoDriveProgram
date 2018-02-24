# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 21:43:10 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(-1, 1, 0.01), np.arange(-1, 1, 0.01))

contor = np.sqrt(x ** 2 + y ** 2)
plt.imshow(contor)
plt.colorbar()
plt.show()