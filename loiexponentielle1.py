# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:31:50 2020

@author: Fatou Badji
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
abs=np.linspace(0,8,200)
plt.plot(abs,expon.cdf(abs,scale=1))
plt.plot(abs,expon.cdf(abs,scale=1/3))
plt.grid()
plt.show()