import tensorflow as tf

import  keras as kr

mnist_v = kr.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist_v.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = kr.models.Sequential([
  kr.layers.Flatten(),
  kr.layers.Dense(512, activation=tf.nn.relu),
  kr.layers.Dropout(0.2),
  kr.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)