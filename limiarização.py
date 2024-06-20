# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WKueOHFTF-rw8rO_RUfkEhrFioVJ5YFs
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/content/1097069.jpg')
plt.imshow(img);

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb); #imagem convertida(original)

gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray');

limiar = 180

val, thresh = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY)

plt.imshow(thresh, cmap='gray');

limiar = 100
val, thresh = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY);
plt.imshow(thresh, cmap = 'gray');

fig = plt.gcf()
fig.set_size_inches(18,6)
plt.imshow(thresh, cmap='gray')
plt.axis('off')
plt.show()

cv2.imwrite('resultado.jpg', thresh)