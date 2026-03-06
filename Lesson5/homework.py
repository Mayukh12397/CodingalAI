import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()



x_train, x_test = x_train / 255.0, x_test / 255.0



model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(138, activation='relu'), 
    layers.Dense(15, activation='softmax') 
])



model.compile(optimizer='RMSprop',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])



model.fit(x_train, y_train, epochs=5) 


test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}") 


predictions = model.predict(x_test)



plt.imshow(x_test[3], cmap=plt.cm.binary) 
plt.title(f"Predicted: {predictions[3].argmax()}")
plt.show()


