#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 feng <feng@archlinux>
#
# Distributed under terms of the MIT license.

"""
Figure 10 is from the numerical study in "Time crystals made of electron-positron pairs".
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sympy.abc import t

plt.rcParams.update({
    'axes.titlesize': 28,
    'axes.labelsize': 26,
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    'legend.fontsize': 22
})

def fun_new(y, t, a, b):
    f, df, g, dg = y
    dydt = [ df , (-a+t)*f+b*g , dg, (-a-t)*g+b*f ]
    return dydt

y0=[0,-0.665192338, 1, 0]
t_left=np.arange(0,-2.5,-0.001)
sol_left = odeint(fun_new , y0, t_left, args=(2/(2**(1/3)),2**(2/3)))
t_right=np.arange(0,10,0.001)
sol_right= odeint(fun_new , y0, t_right, args=(2/(2**(1/3)),2**(2/3)))

plt.plot(t_left,sol_left[:,0], color="r", label=r"$\phi_1$")
plt.plot(t_left,sol_left[:,2], color="b", label=r"$\phi_2$")
plt.plot(t_right,sol_right[:,0], color="r")
plt.plot(t_right,sol_right[:,2], color="b")
plt.axhline(0,color="gray") # 画过原点的水平线
plt.axvline(0,color="gray") # 画过原点的竖直线
plt.text(1, 1.3, r"$(-\frac{d^2}{dy^2}-\frac{\epsilon}{2^{1/3}}+y)\phi_1(y)+2^{2/3}\phi_2(y)=0$", fontsize=20)
plt.text(1, 0.9, r"$(-\frac{d^2}{dy^2}-\frac{\epsilon}{2^{1/3}}-y)\phi_2(y)+2^{2/3}\phi_1(y)=0$", fontsize=20)
# plt.title(r"Iwo Bialynicki-Birula FIG.10 $\epsilon=2$ $\phi_1=0$, $\phi_1'=-0.665192338$, $\phi_2=1$, $\phi_2'=0$ ", fontproperties="SimHei", fontsize=20)
plt.xlabel("y")
plt.ylabel(r"$\phi_1$ and $\phi_2$")
plt.legend()
plt.show()
