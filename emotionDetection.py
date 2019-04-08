import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
from keras.utils import np_utils
from sklearn.model_selection import train_test_split

from keras.models import Sequential #Initialise our neural network model as a sequential network
from keras.layers import Conv2D #Convolution operation
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
from keras.layers import Activation#Applies activation function
from keras.layers import Dropout#Prevents overfitting by randomly converting few outputs to zero
from keras.layers import MaxPooling2D # Maxpooling function
from keras.layers import Flatten # Converting 2D arrays into a 1D linear vector
from keras.layers import Dense # Regular fully connected neural network
from keras import optimizers
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, TensorBoard, ModelCheckpoint
from sklearn.metrics import accuracy_score, classification_report
from keras import models
from keras import layers
from keras.applications import VGG16
from keras.applications import resnet50



TRAIN_END=28708
TEST_START=TRAIN_END+1
IMG_SIZE=48
NUM_CLASSES=7
def duplicate_input_layer(array_input, size):

	vg_input = np.empty([size, 48, 48, 3])
	for index, item in enumerate(vg_input):
		item[:, :, 0] = array_input[index]
		item[:, :, 1] = array_input[index]
		item[:, :, 2] = array_input[index]

	return vg_input


def process_emotion(emotion):
    """
    Takes in a vector of emotions and outputs a list of emotions as one-hot vectors.
    :param emotion: vector of ints (0-7)
    :return: list of one-hot vectors (array of 7)
    """
    emotion_as_list = pandas_vector_to_list(emotion)
    y_data = []
    for index in range(len(emotion_as_list)):
        y_data.append(emotion_as_list[index])

    # Y data
    y_data_categorical = np_utils.to_categorical(y_data, NUM_CLASSES)
    return y_data_categorical


def process_pixels(pixels, img_size=IMG_SIZE):
    """
    Takes in a string (pixels) that has space separated ints. Will transform the ints
    to a 48x48 matrix of floats(/255).
    :param pixels: string with space separated ints
    :param img_size: image size
    :return: array of 48x48 matrices
    """
    pixels_as_list = pandas_vector_to_list(pixels)

    np_image_array = []
    for index, item in enumerate(pixels_as_list):
        # 48x48
        data = np.zeros((img_size, img_size), dtype=np.uint8)
        # split space separated ints
        pixel_data = item.split()

        # 0 -> 47, loop through the rows
        for i in range(0, img_size):
            # (0 = 0), (1 = 47), (2 = 94), ...
            pixel_index = i * img_size
            # (0 = [0:47]), (1 = [47: 94]), (2 = [94, 141]), ...
            data[i] = pixel_data[pixel_index:pixel_index + img_size]

        np_image_array.append(np.array(data))

    np_image_array = np.array(np_image_array)
    # convert to float and divide by 255
    np_image_array = np_image_array.astype('float32') / 255.0
    return np_image_array



def split_for_test(list):
    train = list[0:20000]
    test = list[20001:28720]
    return train, test


def pandas_vector_to_list(pandas_df):
    py_list = [item[0] for item in pandas_df.values.tolist()]
    return py_list





raw_data = pd.read_csv('fer2013.csv')

# convert to one hot vectors
emotion_array = process_emotion(raw_data[['emotion']])

# convert to a 48x48 float matrix
pixel_array = process_pixels(raw_data[['pixels']])

# split for test/train
y_train, y_test = split_for_test(emotion_array)
x_train_matrix, x_test_matrix = split_for_test(pixel_array)

n_train = int(len(x_train_matrix))
n_test = int(len(x_test_matrix))

x_train_input = duplicate_input_layer(x_train_matrix, n_train)
x_test_input = duplicate_input_layer(x_test_matrix, n_test)






'''
conv_base = VGG16(weights='imagenet',\
		  include_top=False,\
		  input_shape=(48, 48, 3))
'''

conv_base =resnet50.ResNet50(weights= 'imagenet', include_top=False, input_shape=(48, 48, 3))
#conv_base.trainable = False

#conv_base.trainable = False
model = models.Sequential()
model.add(conv_base)
'''
model=Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(48, 48, 3), kernel_regularizer=l2(0.01)))
model.add(Conv2D(64, (3, 3), padding='same',activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(128, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(Conv2D(128, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(Conv2D(128, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))

model.add(Conv2D(256, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(Conv2D(256, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(Conv2D(256, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))

model.add(Conv2D(512, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(Conv2D(512, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(Conv2D(512, (3, 3), padding='same', activation='relu',kernel_regularizer=l2(0.01)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))
'''

model.add(Flatten())
'''
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
'''
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))

lr_reducer = ReduceLROnPlateau(monitor='val_loss', factor=0.9, patience=3)
early_stopper = EarlyStopping(monitor='val_acc', min_delta=0, patience=6, mode='auto')
'''
model.compile(optimizer=optimizers.RMSprop(lr=2e-5),
loss='categorical_crossentropy',
metrics=['acc'])
'''
'''
set_trainable = False
for layer in conv_base.layers:
    if layer.name == 'block5_conv1':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False
'''
adam = optimizers.Adam(lr = 0.001)
#gen = ImageDataGenerator()
#train_generator = gen.flow(x_train, y_train, batch_size=32)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])

history = model.fit(x_train_input, y_train,
epochs=30,callbacks=[lr_reducer,early_stopper], batch_size=64, validation_data=(x_test_input, y_test))


model.save_weights('model_weights.h5')
with open('model_architecture.json', 'w') as f:
    f.write(model.to_json())
model.save('my_model.h5')

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()

