#!/usr/bin/python

# -*- coding:UTF-8 -*-  
from os import path  
from scipy.misc import imread  
import matplotlib.pyplot as plt  
from matplotlib.font_manager import FontProperties  
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  
  
import sys  
import importlib
importlib.reload(sys)  
  
  
d = path.dirname(__file__)  
  
# Read the wholedd text.  
text = open(path.join(d, 'alice_result.txt')).read()  
  
# read the mask / color image  
# taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010  
alice_coloring = imread(path.join(d, "alice_color.png"))  
  
wc = WordCloud(background_color="white", max_words=100, mask=alice_coloring,  
               font_path='/Library/Fonts/HYLiangPinXianJ.ttf',stopwords=STOPWORDS.add("said"),  
               max_font_size=50, random_state=42)  
# generate word cloud  
wc.generate(text)  
  
# create coloring from image  
image_colors = ImageColorGenerator(alice_coloring)  
  
# show  
plt.imshow(wc)  
plt.axis("off")  
plt.figure()  
# recolor wordcloud and show  
# we could also give color_func=image_colors directly in the constructor  
plt.imshow(wc.recolor(color_func=image_colors))  
plt.axis("off")  
plt.figure()  
plt.imshow(alice_coloring, cmap=plt.cm.gray)  
plt.axis("off")  
plt.show()  
#save img  
wc.to_file(path.join(d, "cloudimg.png"))  
