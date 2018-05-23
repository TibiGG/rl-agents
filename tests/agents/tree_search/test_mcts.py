import gym
import numpy as np
import pytest
from rl_agents.agents.tree_search.mcts import MCTSAgent


def test_cartpole():
    env = gym.make('CartPole-v0')
    agent = MCTSAgent(env, iterations=40, temperature=200, max_depth=10)

    state = env.reset()
    done = False
    steps = 0
    while not done:
        action = agent.act(state)
        assert isinstance(action, (int, np.int32))

        next_state, reward, done, info = env.step(action)
        with pytest.raises(NotImplementedError):
            agent.record(state, action, reward, next_state, done)

        steps += 1

    assert steps == env._max_episode_steps