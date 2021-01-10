import gym

env = gym.make('Alien-v0')

for i_episode in range(10):
    env.reset()
    total_reward = 0
    for t in range(10000):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break

