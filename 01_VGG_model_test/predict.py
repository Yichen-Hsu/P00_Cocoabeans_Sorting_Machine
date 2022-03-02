import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
import numpy as np
import pandas as pd

class_names = ['agglomeration', 'fine', 'flat']

# model = "C:\\Users\Ey\Desktop\model_test\00_tensorflowlite01\01_model_test\model1\\saved_model.pb"

img = tf.io.read_file("C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\valid\\fine\\151.jpg")
img = tf.image.decode_image(img, channels=3)
img = tf.image.resize(img, size=[224, 224])
img = img/225.
# img = "C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\valid\\flat\\329.jpg"

model1 = tf.keras.models.load_model('C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\model1')

pred = model1.predict(tf.expand_dims(img, axis=0))

print(pred)
print(pred.argmax())
pred_class = class_names[pred.argmax()]
print(pred_class)