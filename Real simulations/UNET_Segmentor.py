from patchify import patchify, unpatchify
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
from tensorflow.keras.utils import normalize

from keras.models import load_model

class UNET_Segmentor:
    def __init__(self):
            print("in init")

    def predict(self):  
    # *************** Prediction on a given image ****************


        model = load_model('V8.hdf5')
        train_image = []

        #You can change the image file with whatever algorithm output you want to test 
        #(return back to image reconstruction algorithms for output images names)
        large_image = cv2.imread('demo_static.png', 0)
        large_image = cv2.resize(large_image, (128, 128))

        train_image.append(large_image)
        train_image = np.array(train_image)


        train_image = np.expand_dims(train_image, axis=3)
        train_image = normalize(train_image, axis=1)


        test_img = train_image[0]
        test_img_norm=test_img[:,:,0][:,:,None]
        test_img_input=np.expand_dims(test_img_norm, 0)
        prediction = (model.predict(test_img_input))
        predicted_img=np.argmax(prediction, axis=3)[0,:,:]

        plt.figure(2)
        plt.title('Prediction on test image')
        plt.imshow(predicted_img, cmap='nipy_spectral')


        #show both images
        plt.show()