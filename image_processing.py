# load and display an image with Matplotlib
from PIL import Image
from matplotlib import image
import numpy as np
from numpy import asarray
from matplotlib import image
from matplotlib import pyplot
# load the image
# convert image to gray scale
image = Image.open("./image/MCZ7o.jpg")
im = image.convert('L')
print(type(im))   # pil.IMAGE
# convert image to numpy array
im_map = im.load()
data = asarray(im)
# print(type(data))  # numpy.array
# print(data)
# print(data.size)
# print(data.shape)
i = 0
j = 0
lst = []
x = data.shape
# tabdile matrixe pixelha be binary
for i in range(x[0]):
    for j in range(x[1]):
        lst.append((np.binary_repr(im_map[i, j], width=8)))
data = np.array(lst).reshape(data.shape)
data = np.transpose(data)
print(type(data))
print(data)
i = 0
j = 0
pixel = []
page = 0
# sakhte 2D array
data_plane = np.arange(data.size).reshape(x[0], x[1])
# joda sazie har laye va tabdil be int(dar in ghesmat 0 o 1 har yeki az indexhaye 0 ta 7 tamame pixelhara joda mikonim)
for page in range(8):
    for i in range(x[0]):
        for j in range(x[1]):
            pixel = data[i][j]
            data_plane[i][j] = np.uint8(pixel[page], base=2)
    print(type(data_plane))
    print("dsfdd")
    # dar in ghesmat har yek az khaanehaye matrix be andazeye int ast vali bayad yek bit bashad
    print(data_plane)
    pyplot.imshow(data_plane, cmap="gray")
    pyplot.savefig(str(page)+'.jpg', bbox_inches='tight', dpi=150)
    pyplot.show()
