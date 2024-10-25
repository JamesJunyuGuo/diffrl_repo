import os
os.environ["DISPLAY"] = ":0"  # Set display to Xvfb

import metaworld
import random
import matplotlib.pyplot as plt

# Initialize MetaWorld and setup the task
ml1 = metaworld.ML1('door-open-v2')
env = ml1.train_classes['door-open-v2']()

task = random.choice(ml1.train_tasks)
env.set_task(task)

env.render_mode = 'rgb_array'

obs = env.reset()
if obs is None:
    print("Environment reset failed! Check initialization.")
else:
    print("Environment reset successfully.")
print(obs.shape)
# # Display the initial pixel observation
# plt.imshow(pixel_obs)
# plt.title("Initial RGB Observation of Door-Open Task")
# plt.axis('off')
# plt.show()
