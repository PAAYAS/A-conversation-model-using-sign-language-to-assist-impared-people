import tensorflow as tf
import numpy as np
from PIL import Image
from gtts import gTTS
import os 
from tensorflow.keras.optimizers import Adam

# Load the trained model
model = tf.keras.models.load_model("model/ISLResNet50V2.h5", compile=False)
learning_rate = 0.0001
adam = Adam(lr=learning_rate)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

# Class Labels
class_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']

# Load and preprocess the image
image = Image.open('Indian/1/8.jpg')
image = image.resize((64, 64)) # ResNet50v2 expects input shape (224, 224, 3)
image_array = np.asarray(image)
image_array = np.expand_dims(image_array, axis=0) # Reshape to (1, 224, 224, 3)
image_array = tf.keras.applications.resnet_v2.preprocess_input(image_array)

# Make predictions
prediction = model.predict(image_array)
label = np.argmax(prediction, axis=-1)[0]

# Convert the predicted index back to its original label
predicted_label = class_labels[label]
print('Predicted label:', predicted_label)

# Get speech
language = 'en'
myobj = gTTS(text=predicted_label, lang=language, slow=False)
myobj.save("speech.mp3")
os.system("start speech.mp3")