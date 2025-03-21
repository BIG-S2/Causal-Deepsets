import pickle
import tqdm
import numpy as np
import os
from utils import *

from one_stage_simu import DeepDR
from new_car import Simulator
from policy import PCarPolicy
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--fmod', type=int, default = 1) 
parser.add_argument('--bmod', type=int, default = 1)
parser.add_argument('--deepset', type = int, default = 0) # 0 for Order policy
parser.add_argument('--parm', type=float, default = 1, help = 'kappa')
parser.add_argument('--l',type=int,default = 5)

args = parser.parse_args()

REPLICATES = 40
# print(data[0][:10])
top_k = 6
beh_pi = 0.5
deep_dim =2

deepset = bool(args.deepset)
normalize = False

max_iters = int(10000)
hidden_dim = 16
print_freq = 500
batch_size = 32
lr = 1e-4

device = "cpu"
rep = 10
thresh = 1e-4
eql_thresh = 1e-1

noise = True
std = 1

rho_u = 0.9
rho_v = 0.99
phi = 1.75
fmod = args.fmod # 1 ->' linear',0->'nonlinear'
bmod = args.bmod # 1 ->' pert',0->'nonpert'
th = 0.3
l=args.l #5,10,15
T = 100
sigma = 2

tgt_beta = np.array([args.parm,1-args.parm])
tgt_th = 0.5

DR, IS, PLG = [],[],[]
STAT_VALUE = []
counter = 0

os.makedirs("results/", exist_ok=True)
f_pth = 'results/l{}_fmod{}_bmod{}_kappa{}deepset_{}.pkl'.format(l,fmod,bmod,args.parm, deepset)


for i in range(REPLICATES):
    print('Now proc iter {}'.format(counter+1))
    counter += 1

    simulator = Simulator(l,  fmod, bmod, phi, rho_u, rho_v, sigma, th)
    # u_0 = np.arange(25)

    data, adj_mat, raw_data = simulator.simu_trajs(T)

    tgt_pi = PCarPolicy(tgt_beta,tgt_th)
    state_value, state_std = simulator.get_real_value(100000, tgt_pi)

    states = np.array([[item[0] for item in x] for x in data])
    a_tgt = tgt_pi.get_action(states)

    dr =DeepDR(42, data, adj_mat, normalize, deepset, tgt_pi, deep_dim)

    dr.est_reward(batch_size,max_iters, hidden_dim, print_freq,  lr, device)
    mod = 'TR' # choose mode for calculating the propensity score, 'TR' (traversal) or 'MC'
    dr.est_prop_score(rep, beh_pi, mod, thresh, eql_thresh, noise, std)
    dr_est = dr.construct_dr_est(dr.batch_idx,dr.prob,dr.a_tgt)
    is_est = dr.construct_is_est(dr.batch_idx,dr.prob)
    plg_est = dr.construct_plg_est(dr.a_tgt)
    DR.append(dr_est)
    IS.append(is_est)
    PLG.append(plg_est)
    STAT_VALUE.append(state_value)
    ########################################

    print('real_value is {:.1f},while standard error is {:.2f}'.format(state_value,state_std))
    print("MSE of this round is {}".format(mse(dr_est, state_value)))
    dump = [args.parm, mse(DR, STAT_VALUE), mse(PLG, STAT_VALUE), ci(DR, STAT_VALUE), ci(PLG, STAT_VALUE), counter]
    print("MSE of DR is {}".format(dump[1]))
    print("MSE of PLG is {:.1f}".format(dump[2]))

    ########################################
    with open(f_pth, 'wb') as f:
        pickle.dump(dump,f)
        f.close()


 