from stable_baselines3.common.env_checker import check_env
from game.dinogame import DinoGame

env = DinoGame()
check_env(env)