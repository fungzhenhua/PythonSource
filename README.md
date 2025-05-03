# Time Crystals Simulation Code

This code repository contains Python scripts for reproducing the results presented in Figures 9, 10, and 11 of the paper "Comment on 'Time Crystals Made of Electron-Positron Pairs': Parity Considerations and Numerical Validation". Despite using identical initial conditions as reported in the original study, our simulations reveal significant differences.

## Directory Structure

```python
.
├── README.md
├── PythonSource/
│   ├── fig9.py
│   ├── fig10.py
│   └── fig11.py
```


## Usage

To reproduce each figure, run the corresponding script. The scripts are designed to use the same initial conditions specified in the original research article.

### Example Commands

#### Reproducing Figure 9

```bash
python PythonSource/fig9.py
```

#### Reproducing Figure 10

```bash
python PythonSource/fig10.py
```

#### Reproducing Figure 11

```bash
python PythonSource/fig11.py
```

### Initial Conditions

The following initial conditions are used for the calculations:

- For eigenvalue $\varepsilon=2$ corresponding to the quantum Hamiltonian (19), at $y=0:$ $\phi_1=1$,$\phi'_1=0$,$\phi_2=0$ and $\phi_2'=−0.354651985$.
- Also for $\varepsilon=2$ but another set of initial values at $y=0:$ $\phi_1=1$,$\phi'_1=-0.665192338$,$\phi_2=1$ and $\phi_2'=0$
- For eigenvalue $\varepsilon=5$ corresponding to the quantum Hamiltonian (19), at $y=0:$ $\phi_1=0$,$\phi'_1=-0.36012$,$\phi_2=1$ and $\phi_2'=0$.

Despite applying these exact initial conditions, our results show notable discrepancies when compared to Figures 9, 10, and 11 in the original publication. This suggests potential overlooked numerical or theoretical nuances in the original study.

## Contact ##

For any questions or suggestions, please contact Zhen-Hua Feng (fengzhenhua@mail.bnu.edu.cn).


## Acknowledgements ##

We thank Prof. Bialynicki-Birula for his pioneering contributions to quantum theory and Ref.[1] for providing the intellectual foundation.

## References ##

[1] I. Bialynicki-Birula and Z. Bialynicka-Birula, Phys. Rev. A 104, 022203(2021).
[2] G. B. Arfken, Mathematical Methods for Physicists, 3rd ed.(Academic Press, San Diego, USA, 1985).
