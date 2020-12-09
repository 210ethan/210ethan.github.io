#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:19:09 2020

@author: EthanMorse
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 50, 100)
y1 = -0.025*x1

x2 = np.linspace(50, 55, 100)
y2 = 15-2*np.log(x2)

x3 = np.linspace(0, 55, 10)
y3 = 0*x3

y4 = np.linspace(-1.25, 7.18, 10)
x4 = 50 + 0*y4

fig = plt.figure(figsize = (10,5))
plt.plot(x1, y1, color = "blue")
plt.plot(x2, y2, color = "blue")
plt.plot(x3, y3, color = "red")
plt.plot(x4, y4, color = "blue")

plt.show()