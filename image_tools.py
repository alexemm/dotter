from PIL import Image
import numpy as np
from stippler import  choose_k_points, get_probability_matrix,tractor_beam


def load_image(file: str):
    im = Image.open(file).convert('L')
    return im


def image_to_array(img):
    return np.asarray(img)


def array_to_image(arr):
    return Image.fromarray(np.uint8(arr))


input_folder = 'images/input/'
output_folder = 'images/output/'
name = 'fine_art.jpg'
k = 200
iterations = 10000
im_arr = image_to_array(load_image(input_folder + name))
#output_img = array_to_image(im_arr)
output_img = array_to_image(tractor_beam(im_arr, k=k, iterations=iterations))
output_img.save(output_folder+name)
