task=door-open
python3 train_metaworld.py --config configs/latent_diff_sr.yaml --task "metaworld_$task"



# echo -e 'export LD_LIBRARY_PATH=/home/Junyu/.mujoco/mujoco210/bin 
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia 
# export PATH="$LD_LIBRARY_PATH:$PATH" 
# export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so' >> ~/.bashrc