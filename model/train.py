import tensorflow as tf
from tensorflow import keras
import numpy as np
import pickle

# Generate dummy data
x_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
x_test = np.random.random((100, 20))
y_test = np.random.randint(2, size=(100, 1))

# Simple binary classifier model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(20,)),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test accuracy: {accuracy:.4f}")

# Save the model
model.save('model/simple_model.h5')  # SavedModel format

# Also save as pickle for compatibility with your original structure
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
