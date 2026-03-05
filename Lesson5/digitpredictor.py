# check collab for the activity
# Tensorflow is already installed in collab, making it easier to conduct the following activity.
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt


# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# Mnist dataset is a dataset which contains digits from 0-9, images in 28*28 pixels. It contain training and testing data.
# x_train is the training image
# x_test is the testing image
# y_train is the label for training image corresponding to x_train
# y_test is the label for testing image corresponding to x_test


# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0
# In normalization, its scaling input data to range[0,1], by dividing it by 255 in this case. Normalization is done to improve the performance of the model during training and testing.

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'), # it helps the model to learn complex patterns in data.
    # Its connecting 128 neurons.
    layers.Dense(10, activation='softmax') # converts the output to probability distribution over the ten digits.
    # its conncecting 10 neurons into a layer.
])


# Compile the model
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])


# Train the model
model.fit(x_train, y_train, epochs=5) # training model for 5 epochs.


# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}") # evaluate the trained model on the test data set.


# Make predictions
predictions = model.predict(x_test)


# Display the first image and prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()



