import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
import numpy as np
import pandas as pd

class_names = ['fine', 'flat', 'agglomeration']

'''view some images'''
import matplotlib.pyplot as plt
import matplotlib.image as mping

'''read in the image and plot it using matplotlib'''
# img = mping.imread('C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\train\\fine\\1.jpg')
# # print(img) #it's ndarray
# plt.imshow(img)
# img.shape

# Preprocess data (get all of the pixel values between 1 and 0, also called scalling/normalization)
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# set up the train and test directories
train_dir = "C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\train\\" 
test_dir = "C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\test\\"

# import data from directories and turn it into batches
train_data = train_datagen.flow_from_directory(train_dir,
                                               batch_size=32, #number of images to process at a time
                                               target_size=(224,224), #convert all images to be 224 x 224
                                               class_mode="categorical") #type of problem we're working on

test_data = train_datagen.flow_from_directory(test_dir,
                                               batch_size=32, 
                                               target_size=(224,224),
                                               class_mode="categorical")

# print(train_data)
# print(len(train_data))
# print(train_data[0])

# Create our model(Tiny VGG)
model1 = Sequential([
    Conv2D(10, 3, activation='relu', input_shape=(224, 224, 3)),
    Conv2D(10, 3, activation='relu'),
    MaxPool2D(),
    Conv2D(10, 3, activation='relu'),
    Conv2D(10, 3, activation='relu'),
    MaxPool2D(),
    Flatten(),
    Dense(3, activation='softmax')
    ])

# Compile the model
model1.compile(loss="categorical_crossentropy",
    optimizer=tf.keras.optimizers.Adam(),
    metrics=['accuracy'])

# Fit the model
history1 = model1.fit(train_data,
                     epochs= 5,
                     steps_per_epoch = len(train_data),
                     validation_data = test_data,
                     validation_steps = len(test_data))

model1.save("C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\model1")

img = tf.io.read_file("C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\valid\\flat\\329.jpg")
img = tf.image.decode_image(img, channels=3)
img = tf.image.resize(img, size=[224, 224])
img = img/225.
# img = "C:\\Users\\Ey\\Desktop\\model_test\\00_tensorflowlite01\\01_model_test\\valid\\flat\\329.jpg"
pred = model1.predict(tf.expand_dims(img, axis=0))

pred.argmax()
pred_class = class_names[pred.argmax()]
print(pred_class)