# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:17:20 2021

@author: Md. Ishrak Ahsan
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 12, 0.5)
y = x**3 - 18*x**2 + 475.2 

plt.plot(x, y)
plt.show()


