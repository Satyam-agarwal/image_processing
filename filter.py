import numpy as np
import scipy.ndimage as nd
import scipy.misc as mi
import image as im
from scipy.misc.pilutil import Image
from skimage import filters

a = Image.open("justice.jpg").convert('L')
print a
k=np.ones((5,5))/25
print k
b = filters.sobel(a)
b = mi.toimage(b)
b.save('sobel.jpg')
mi.imshow(b)