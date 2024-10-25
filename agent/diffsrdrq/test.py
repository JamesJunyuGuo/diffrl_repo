# import gym

# env = gym.make("Swimmer-v3")
# obs = env.reset()

# for _ in range(100):
#     action = env.action_space.sample()  # Sample a random action
#     obs, reward, done, info = env.step(action)
#     print(obs)
#     if done:
#         env.reset()

# env.close()
import metaworld
import random

ml45 = metaworld.ML45() # Construct the benchmark, sampling tasks

training_envs = []
for name, env_cls in ml45.train_classes.items():
  env = env_cls()
  task = random.choice([task for task in ml45.train_tasks
                        if task.env_name == name])
  print(task.env_name)
  env.set_task(task)
  training_envs.append(env)


for env in training_envs:
  obs = env.reset()  # Reset environment
  a = env.action_space.sample()  # Sample an action
  obs, reward, done, info = env.step(a)  # Step the environment with the sampled random action
  print(obs.shape)
  print(a.shape,a)


# import env.metaworld_env as metaworld_env

# task = "metaworld_door-open"
# domain, task = task.split("_")
# train_env = metaworld_env.make(task, 3, 2, 0)


# state = train_env.observation_spec()

# print(state.shape)