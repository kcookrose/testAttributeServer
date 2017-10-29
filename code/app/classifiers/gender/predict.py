import keras
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.models import Model
from keras.layers import Dropout, Flatten, Dense
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image as kimage
import numpy as np
import os

tuned_model_weights_path = os.path.join(os.path.dirname(__file__), 'tuned_model.h5')

# path to the model weights files.

# build the VGG16 network
base_model = applications.VGG16(weights='imagenet', include_top=False, input_shape=(150,150,3))
print('Model loaded.')

# build a classifier model to put on top of the convolutional model
top_model = Sequential()
top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(1, activation='sigmoid'))

# add the model on top of the convolutional base
# model.add(top_model)
model = Model(inputs=base_model.input, outputs=top_model(base_model.output))
# model = base_model.add(top_model)

model.load_weights(tuned_model_weights_path)

def classify(img_path):

	img = kimage.load_img(img_path, target_size=(150, 150))
	x = kimage.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)

#	print(keras.utils.np_utils.to_categorical(model.predict(x)))
	return model.predict(x)


# Alternativ:

# from keras.models import load_model
# import numpy as np
# import os

# tuned_model_path = os.path.join(os.path.dirname(__file__), 'tuned_model.h5')

# model = model.load_model(tuned_model_path)

# def classify(img_path):

# 	img = kimage.load_img(img_path, target_size=(150, 150))
# 	x = kimage.img_to_array(img)
# 	x = np.expand_dims(x, axis=0)
# 	x = preprocess_input(x)

# 	return model.predict(x)