from gym.envs.registration import register
import numpy as np
import pandas as pd
import gym
import argparse
from spinup import ddpg_pytorch
from spinup.utils.run_utils import ExperimentGrid
import importlib
# import registration
from spinup.utils.test_policy import load_policy_and_env, run_policy
from spinup.utils.test_policy import load_policy_and_env, run_policy

path_to_env="" # current directory

# Method to regiser environment in gym
def register_env(args=None):
    gym.envs.register(
        id='Walker-v1',
        entry_point='bipedalWalker:BipedalWalker',
        max_episode_steps=150,
        kwargs={},
    )

# Helper method to simulate the environment, given a path
def simulate():
    _, get_action = load_policy_and_env(path_to_env)
    env_model = gym.make('hum-v0')
    run_policy(env_model, get_action)

# Running ddpg without the use of experiment grid
def run_ddpg(env):
    print("Environment name: {0}".format(env))
    env_fn = lambda : gym.make(env)
    ddpg_pytorch(env_fn=env_fn, steps_per_epoch=4000, epochs=1)


def experiment_grid(env):
     eg = ExperimentGrid(name='ddpg_20')
     eg.add('env_name', env)
     eg.add('epochs', 20) # epochs used to get to be successful at the target required height
     eg.add('steps_per_epoch', 4000) # 4000

    # Parameters that were adjusted during the training process; we recommend commenting out and use default values
     eg.add('start_steps', 200) # 2000
     eg.add('max_ep_len', 1000) 
     eg.add('pi_lr', 0.01)
     eg.add('replay_size', 10000)
     eg.add('batch_size', 32)
     eg.add('update_after', 0)
     eg.add('update_every', 2)
     eg.add('act_noise', 1)
     eg.run(ddpg_pytorch)

# Can be used to receive arguments for the program – ultimately not used in training either.
# def pass_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--cpu', type=int, default=2)
#     parser.add_argument('--num_runs', type=int, default=1)
#     args = parser.parse_args()
#     return args

# We ended up using just the experiment grid to make tweaks to the runs to find the optimal balance
if __name__ == '__main__':
    name_of_model = 'BipedalWalker-v3'
    # register_env(args)
    # run_ddpg(env)
    experiment_grid(name_of_model)
