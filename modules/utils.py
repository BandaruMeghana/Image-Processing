import numpy as np
import cv2
from PIL import Image


def cv2_to_PIL(image):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(image)
    return pil_img

def translate(image, tx, ty):
    trans_matrix = np.float32([
        [1,0,tx],
        [0,1,ty]
    ])

    shifted = cv2.warpAffine(image,trans_matrix,(image.shape[1],image.shape[0]))
    return shifted

def rotate(image, theta, center = None, scale=1.0):
    (h,w) = image.shape[:2]
    if center is None:
        center = (w//2,h//2)
    rotate_matrix = cv2.getRotationMatrix2D(center, theta, scale)
    rotated = cv2.warpAffine(image, rotate_matrix,(w,h))
    return rotated

def resize(image, new_width=None, new_height=None, inter=cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    if new_width is None and new_height is None:
        return image
    if new_width is None:
        ratio = new_height/float(h)
        dim = (int(w*ratio), new_height)
    else:
        ratio = new_width / float(w)
        dim = (new_width, int(h*ratio))
    resized = cv2.resize(image,dim,interpolation=inter)
    return resized