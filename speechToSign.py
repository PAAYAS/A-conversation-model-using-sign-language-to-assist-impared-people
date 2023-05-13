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
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
    img_dict = {
        'a.jpg': 'A',
        'b.jpg': 'B',
        'c.jpg': 'C',
        'd.jpg': 'D',
        'e.jpg': 'E',
        'f.jpg': 'F',
        'g.jpg': 'G',
        'h.jpg': 'H',
        'i.jpg': 'I',
        'j.jpg': 'J',
        'k.jpg': 'K',
        'l.jpg': 'L',
        'm.jpg': 'M',
        'n.jpg': 'N',
        'o.jpg': 'O',
        'p.jpg': 'P',
        'q.jpg': 'Q',
        'r.jpg': 'R',
        's.jpg': 'S',
        't.jpg': 'T',
        'u.jpg': 'U',
        'v.jpg': 'V',
        'w.jpg': 'W',
        'x.jpg': 'X',
        'y.jpg': 'Y',
        'z.jpg': 'Z',
        '1.jpg': '1',
        '2.jpg': '2',
        '3.jpg': '3',
        '4.jpg': '4',
        '5.jpg': '5',
        '6.jpg': '6',
        '7.jpg': '7',
        '8.jpg': '8',
        '9.jpg': '9'
    }
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        i=0
        while True:
            print("I am Listening..")
            audio = r.listen(source)
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
                            img_name = a[i].lower() + '.jpg'
                            text_rep = img_dict.get(img_name, '')
                            ImageAddress = 'letters/' + img_name
                            ImageItself = Image.open(ImageAddress)
                            ImageNumpyFormat = np.asarray(ImageItself)
                            plt.imshow(ImageNumpyFormat)
                            plt.title(text_rep)
                            plt.draw()
                            plt.pause(0.8)
                        else:
                            continue
            except:
                print(" ")
            plt.close()


while 1:
  image = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Convey Message","All Done!"] 
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
