# Importing necessary modules
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from gtts import gTTS
import os
from visualize import visualize
from convert_mp3_wav import convert

# Create a new window
window = tk.Tk()
window.title("ISL Classifier")
window.geometry("800x600")
window.configure(bg="#F0E68C")

# Load the trained model
model = tf.keras.models.load_model("model/VGG16ISL.h5", compile=False)
learning_rate = 0.0001
adam = Adam(lr=learning_rate)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

# Class Labels
class_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']

# Create a label for the input image
image_label = tk.Label(window, bg="white")

# Function to load and preprocess the image
def load_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load and preprocess the image
        image = Image.open(file_path)
        image = image.resize((64, 64))
        image_array = np.asarray(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = tf.keras.applications.resnet_v2.preprocess_input(image_array)

        # Make prediction
        prediction = model.predict(image_array)
        label = np.argmax(prediction, axis=-1)[0]
        predicted_label = class_labels[label]

        # Display the image and predicted label
        image_tk = ImageTk.PhotoImage(image)
        image_label.configure(image=image_tk, width=300, height=300)
        image_label.image = image_tk
        predicted_label_text.set(f"Predicted label: {predicted_label}")

        # Generate speech
        language = 'en'
        if predicted_label.isdigit():
            message = f"{predicted_label}."
        else:
            message = f"{predicted_label.upper()}."
        
        myobj = gTTS(text=message, lang=language, slow=False)
        myobj.save("speech.mp3")
        os.system("start speech.mp3")
        
        # converting mp3 to wav file
        convert("speech.mp3")
        # Visualization
        visualize("file.wav")

# Create a button to load the image
load_button = tk.Button(window, text="Load Image", font=("Arial", 14), bg="white", fg="black", bd=2, relief="raised", command=load_image)

# Create a label to display the predicted label
predicted_label_text = tk.StringVar()
predicted_label_text.set("Predicted label: ")
predicted_label_label = tk.Label(window, textvariable=predicted_label_text, font=("Arial", 14), bg="white", fg="black")

# Create a label for the title
title_label = tk.Label(window, text="Indian Sign Language Classifier", font=("Arial", 24), bg="white", fg="black")

# Create a label for the instructions
instructions_label = tk.Label(window, text="Please select an image to classify.", font=("Arial", 14), bg="white", fg="black")

# Create a label for the credits
credits_label = tk.Label(window, text="Developed by Team-2 Here", font=("Arial", 10), bg="white", fg="black")

# Pack the GUI widgets into the window
title_label.pack()
instructions_label.pack()
load_button.pack()
image_label.pack()
predicted_label_label.pack()
credits_label.pack()

# Start the GUI loop
window.mainloop()