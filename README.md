# Time Crystals Simulation Code

This code repository contains Python scripts for reproducing the results presented in Figures 9, 10, and 11 of the paper "Divergent Solutions and Enforced Symmetry in Bialynicki-Birula’s Time Crystal Quantum Model: A Numerical-Theoretical Exposé". Despite using identical initial conditions as reported in the original study, our simulations reveal significant differences.

## Directory Structure

```python
.
├── README.md
├── PythonSource/
│   ├── fig9.py
│   ├── fig9_x.py
│   ├── fig10.py
│   ├── fig10_x.py
│   ├── fig11.py
│   └── fig11_x.py
└── Figures/
├── Figure_9.png
├── Figure_9o.png
├── Figure_9x.png
├── Figure_10.png
├── Figure_10o.png
├── Figure_10x.png
├── Figure_11.png
├── Figure_11o.png
└── Figure_11x.png
```


## Usage

To reproduce each figure, run the corresponding script. The scripts are designed to use the same initial conditions specified in the original research article.

### Example Commands

#### Reproducing Figure 9

```bash
python PythonSource/fig9.py   #  y ranging from −2 to 10
python PythonSource/fig9_x.py #  y ranging from −10 to 10
```

#### Reproducing Figure 10

```bash
python PythonSource/fig10.py  #  y ranging from −2 to 10
python PythonSource/fig10_x.py #  y ranging from −10 to 10
```

#### Reproducing Figure 11

```bash
python PythonSource/fig11.py   #  y ranging from −4 to 10
python PythonSource/fig11_x.py #  y ranging from −10 to 10
```

### Initial Conditions

The following initial conditions are used for the calculations:

- For eigenvalue $\varepsilon=2$ corresponding to the quantum Hamiltonian (19), at $y=0:$ $\phi_1=1$, $\phi_1'=0$, $\phi_2=0$ and $\phi_2'=−0.354651985$.
- Also for $\varepsilon=2$ but another set of initial values at $y=0:$ $\phi_1=1$, $\phi_1'=-0.665192338$, $\phi_2=1$ and $\phi_2'=0$
- For eigenvalue $\varepsilon=5$ corresponding to the quantum Hamiltonian (19), at $y=0:$ $\phi_1=0$, $\phi_1'=-0.36012$, $\phi_2=1$ and $\phi_2'=0$.

Despite applying these exact initial conditions, our results show notable discrepancies when compared to Figures 9, 10, and 11 in the original publication. This suggests potential overlooked numerical or theoretical nuances in the original study.

## Contact ##

For any questions or suggestions, please contact Zhen-Hua Feng (fengzhenhua@mail.bnu.edu.cn).


## Acknowledgements ##

We thank Prof. Bialynicki-Birula for his pioneering contributions to quantum theory and Ref.[1] for providing the intellectual foundation.

## References ##

- [1] I. Bialynicki-Birula and Z. Bialynicka-Birula, Phys. Rev. A 104, 022203(2021).
- [2] G. B. Arfken, Mathematical Methods for Physicists, 3rd ed.(Academic Press, San Diego, USA, 1985).
