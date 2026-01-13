from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import rotate


image_path = 'venv/Flower Color Images Dataset/flowers/flowers/09_010.png'
original_image = Image.open(image_path)

# Display the original image using matplotlib
plt.imshow(original_image)

from scipy.ndimage import rotate
def rotate_image_30_degrees(image):
    return rotate(image, 30, reshape=False, mode='nearest') 

rotated_image = rotate_image_30_degrees(np.array(original_image))
plt.imshow(rotated_image)
plt.show()

from PIL import ImageOps

flipped_h = ImageOps.mirror(original_image)

plt.imshow(flipped_h)
plt.axis("off")
plt.title("Flip horizontal")
plt.show()
flipped_v = ImageOps.flip(original_image)

plt.imshow(flipped_v)
plt.axis("off")
plt.title("Flip vertical")
plt.show()

w, h = original_image.size
res = original_image.resize((int(w*1.2), int(h*1.2)))
res.show()