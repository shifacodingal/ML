import tensorflow as tf
from tensorflow import layers, models
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255.0

model = models.Sequential([layers.Flatten(input_shape=(28, 28)), layers.Dense(128, activation='relu'), layers.Dense(10, activation='softmax')])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

predictions = model.predict(x_test)
num_images = 25
for i in range(num_images):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    predicted_lable = predictions[i].argmax()
    true_lable = y_test[i]
    color = 'blue' if predicted_lable == true_lable else 'red'
    plt.xlabel(f'True: {true_lable}\nPred: {predicted_lable}', color=color)
plt.tight_layout()
plt.show()
