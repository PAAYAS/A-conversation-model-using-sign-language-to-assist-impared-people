import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
from PIL import Image, ImageTk
import tkinter as tk

# Preprocess Text
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

nltk.download('stopwords')
nltk.download('punkt')

def preprocess(text):
    stop_words = set(stopwords.words('english'))
    stemmer = SnowballStemmer('english')
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [stemmer.stem(token) for token in tokens]
    processed_text = ' '.join(tokens)
    return processed_text

def func():
    r = sr.Recognizer()
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        i=0
        while True:
            print("I am Listening..")
            audio = r.listen(source)
            # recognize speech using Sphinx
            try:
                a=r.recognize_google(audio)
                a=preprocess(a)
                print('You Said: ' + a.lower())
                if(a.lower()=='goodbye' or a.lower()=='good bye' or a.lower()=='bye'):
                    print("oops!Time To say good bye")
                    break
                else:
                    for i in range(len(a)):
                        if(a[i] in arr):
                            ImageAddress = 'letters/'+a[i]+'.jpg'
                            ImageItself = Image.open(ImageAddress)
                            ImageNumpyFormat = np.asarray(ImageItself)
                            plt.imshow(ImageNumpyFormat)
                            plt.draw()
                            plt.pause(0.8)
                        else:
                            continue
            except:
                print(" ")
            plt.close()

while 1:
  image   = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Convey Message","All Done!"] 
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
