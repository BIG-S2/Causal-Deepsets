# Causal PIE: Permutation Invariant Estimator for Off-policy Evaluation under Spatial or Spatial-temporal Interferences

This repository contains the implementation for the paper "Causal PIE: Permutation Invariant Estimator for Off-policy Evaluation under Spatial or Spatial-temporal Interferences" in Python.

The code consists of two parts. The code for Nondynamic Simulation, as described in Section 5.1 of the paper, is located in the `sec5.1` folder. Conversely, the code for Dynamic Simulation, outlined in Section 5.2, is housed in the `sec5.2` folder. To replicate the results presented in our manuscript, please follow the instructions provided below.

## Installation

* First use `git clone` command to clone our repository to your local machine.
* Then, you should enter the directory and install the required packages by running the following commands in your terminal:

```
cd Causal-Deepsets
conda create -n PIE python=3.9
conda activate PIE
pip install -r requirements.txt
```

## Nondynamic Simulation

Firstly enter the folder `sec5.1` by running the following command in your terminal:

```
cd sec5.1
```

### Reproducing Figure 4
![visual](/image/fig4.png)

**Figure 4 in the paper**

To derive Figure 4, we first should run `run_newcar.py` using the following parameter combination:

```
python run_newcar.py --fmod 1 --bmod 1 --deepset 1 --parm 0.2 --l 5
```

where `fmod=1` represents the linear setting while `fmode=0` represents the nonlinear setting. `bmod=1` represents permutation invariant case while `bmod=0` break the permutation invariant assumption. Specifically, `fmod = 1` and `bmod = 1` represents the linear setting in Figure 4, while `fmod = 0` and `bmod = 1` represents the nonlinear 1 , `fmod = 0` and `bmod = 0` represents the nonlinear 2.

`deepset=1` means a PIE structure is applied, otherwise, a mean-field technique is used. `parm` specifies $\kappa$ in policy definition. `l` denote the grid number of each dimension in spatial space.

Figure 4 follows the following parameter combination :

| parm | deepset=1                                                      | deepset=0 |
| ---- | -------------------------------------------------------------- | --------- |
| 0.2  | (fmod=1,bmod=1,l=5),(fmod=0,bmod=1,l=5),(fmod=0,bmod=0,l=5)    | ...       |
| 0.4  | (fmod=1,bmod=1,l=5),(fmod=0,bmod=1,l=5),(fmod=0,bmod=0,l=5)    | ...       |
| 0.6  | (fmod=1,bmod=1,l=5),(fmod=0,bmod=1,l=5),(fmod=0,bmod=0,l=5)    | ...       |
| 0.8  | (fmod=1,bmod=1,l=5),(fmod=0,bmod=1,l=5),(fmod=0,bmod=0,l=5)    | ...       |
| 0.2  | (fmod=1,bmod=1,l=10),(fmod=0,bmod=1,l=10),(fmod=0,bmod=0,l=10) | ...       |
| 0.4  | (fmod=1,bmod=1,l=10),(fmod=0,bmod=1,l=10),(fmod=0,bmod=0,l=10) | ...       |
| 0.6  | (fmod=1,bmod=1,l=10),(fmod=0,bmod=1,l=10),(fmod=0,bmod=0,l=10) | ...       |
| 0.8  | (fmod=1,bmod=1,l=10),(fmod=0,bmod=1,l=10),(fmod=0,bmod=0,l=10) | ...       |

The result will be saved in `/results`. To generate the figure 4, the specific procedure is displayed in `plot.py `.

### File overview

* `new_car.py` This script implement the simulation environment and generates data.
* `run_newcar.py` This script import new_car.py to generate offline data then train policy evaluation models and evaluate their performance.

## Dynamic Simulation

Firstly enter the folder `sec5.2` by running the following command in your terminal:

```
cd sec5.2
```

### Ride-sharing simulation environment

One of the contribution of the paper is developing an easy-to-use ride-sharing simulation environment to simulate the ride-sharing process under top-k subsidy policies.

The ride-sharing simulation environment is implemented in `ride_sharing_simu.py`. To visualize the simulation environment, you can run `visuallize_policy.py` by running the following command in your terminal:

```bash
python visualize_policy.py
```

by changing the parameter `l` to visualize the ride-sharing process with different number of grids. To visualize different policies, you can modify TOP in `visuallize_policy.py`.
![visual](/image/policy.png)


### Reproducing Figure 5
![visual](/image/fig5.png)
**Figure 5 in the paper**

To derive Figure 5, we first should run `run_arg.py` using the following parameter combination:

```
python -u run_arg.py --deepset 1 --top 10 --l 5
```

where `top=k` denotes top-k subsidize policy is applied, subsidizing the k spatial units with highest average number of orders. `deepset=1` means a PIE structure is applied, otherwise, a mean-field technique is used. `l` denotes the simulation environment adopts a map of size $l × l$.

The 
The result will be saved in `/results`. And the plot `results.png` will be automatically generated by function draw_results in `utils.py`.
