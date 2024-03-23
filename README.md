# Curriculum-Learning

I used gym  (https://github.com/openai/gym) with box2d (https://github.com/openai/gym/blob/master/gym/envs/box2d/bipedal_walker.py).The bipedal_walker.py environment file had to be modified to fit to our requirements for Curriculum Learning. 

The main.py files contain the minimal code required to get the experiments up and running. However, it's incredibly tricky to get gym to perform the "registration" of custom environment, which has still been included as part of the code to try out if needed; in fact, they had a bug that prevents proper functioning of this registration function for the purposes of the experiment themselves. Therefore, it is important to copy this "bipedal_walker.py" and "__init__" files to the "gym/gym/envs/box2d/" path of your gym installation, and run the main.py as provided. 

I also use the DDPG algorithm (pytorch) and ExperimentGrid API from them.

Direct packages that need to be installed:

macOS Mojave 10.14.6
gym 0.15.7
spinup 0.2.0 
Python 3.7.12
torch 1.3.1

Unfortunately, the setting up of these environments worked on only one computer, with one or more problem with each of the packages creating extremely constraint conditions for startup. Please let us know if you would like to re-create them.

Finally, I tried out additional simulation environments in PyBullet and Mujoco. This included creating the appropriate environment features in addition to slight modifications to the code provided by them, one of which have been included in the "other" and "environments" folder as examples.
