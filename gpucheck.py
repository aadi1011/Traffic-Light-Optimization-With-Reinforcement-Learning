from tensorflow.python.client import device_lib
# import tensorflow as tf
print(device_lib.list_local_devices())
# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))