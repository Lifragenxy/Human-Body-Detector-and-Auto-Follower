# -*- encoding:utf-8 -*-
# this file contains two parts:
# 1.process the images of human body in BS
# 2.labelling
# 3.training done by tensorflow
import keras
import tensorflow as tf
import keras as kr
import numpy as np
import matplotlib.pyplot as plt
import glob, os
import PIL
from PIL import Image, ImageOps


def convert_to_grey_gradient(image_path: str):
    # Open the input image
    original_image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = ImageOps.grayscale(original_image)

    # Resize the image to 100x100 pixels
    resized_image = grayscale_image.resize((100, 100))

    # return it
    return np.asarray(resized_image)


def load_from_directory(path, label_list: str):
    images = []
    labels = [int(i) for i in label_list.split()]

    os.chdir(path)
    for file_path in glob.glob("*.png"):
        img = convert_to_grey_gradient(file_path)
        images.append(img)
        labels.append(0)

    return (np.asarray(images), np.asarray(labels))


def model_processing(train_domain, lbl):
    train_images, train_labels = load_from_directory(train_domain, lbl)
    class_names = ['human', 'not_human']

    # train_images.shape(26, 100, 100)

    train_images /= 255.0

    # layer processing
    model = keras.Sequential([keras.layers.Flatten(input_shape=(100, 100)),
                              keras.layers.Dense(128, activation=tf.nn.sigmoid),
                              keras.layers.Dense(16, activation=tf.nn.sigmoid),
                              keras.layers.Dense(2, activation=tf.nn.softmax)])

    sgd = keras.optimizers.SGD(lr=0.01, decay=1e-5, momentum=0.7, nesterov=True)

    model.compile(optimizer=sgd,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=100)
