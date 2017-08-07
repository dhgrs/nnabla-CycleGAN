batch_size = 32
hidden_shape = [32, 1, 1]
input_shape = [3, 128, 128]
hidden_channel = 256
out_channel = 3

learning_rate = 0.0002

max_iter = 100000
monitor_interval = 100
generate_interval = 10000
save_interval = 10000

monitor_path = 'tmp.monitor.dcgan'
model_save_path = 'tmp.monitor.dcgan'
root = 'CelebA/'
