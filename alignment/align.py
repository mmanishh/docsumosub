from __future__ import print_function
import os
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import ndimage,stats

def show_img(img,file=True):
    """
    show image by maptlotlib. Accepts matrix image or file_path
    """
    # if filepath read image first
    if file:
        img = cv2.imread(img, cv2.IMREAD_COLOR)
    plt.figure(figsize = (20,15))
    plt.imshow(img,cmap='gray', vmin=0, vmax=255)
    
def concat_image(img1,img2,axis=1):
    """
    concat two image, axis =1 : horizontal , 0:vertical
    """
    return np.concatenate((img1, img2), axis=1)

def get_images_list_path():
    images = []
    for file in glob.glob("./images/*.jpg"):
        images.append(file)
    return images

def get_image_file_names(path='./images'):
    return os.listdir(path)

def mode(array):
    """
    returns mode of array
    """
    return list(stats.mode([1.1,1.2,1.3,1.3]).mode)[0]

def create_dir(dir_name='aligned_images'):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return True

def get_name_only(file_name):
    return file_name.split('.')[0]

def align_img_by_text(img_path):
    image = cv2.imread(img_path)
    # convert the image to grayscale and flip the foreground
    # and background to ensure foreground is now "white" and
    # the background is "black"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
 
    # threshold the image, setting all foreground pixels to
    # 255 and all background pixels to 0
    thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # grab the (x, y) coordinates of all pixel values that
    # are greater than zero, then use these coordinates to
    # compute a rotated bounding box that contains all
    # coordinates
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
     
    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle)
     
    # otherwise, just take the inverse of the angle to make positive
    else:
        angle = -angle
        
    print("[INFO] angle: {:.3f}".format(angle))

    # rotate the image to deskew it
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    return rotated

def align_image_save(img_name,target_dir='./aligned_images2/'):
    path = './images/'+img_name
    print("Procesing image:",path)
    aligned = align_img_by_text(path)
    aligned_path = target_dir+get_name_only(img_name)+'_aligned.jpg'
    cv2.imwrite(aligned_path, aligned)
    print("Aligned image saved at:",aligned_path)
    return aligned_path
  
def process_images(images_path,approach=1):
    for image in images_path:
        if approach == 1:
            pass
           # _ = align_image(image)
        elif approach == 2:
            _ = align_image_save(image)
    return True

if __name__ == '__main__':
  
  process_images(get_image_file_names(),approach=2)
  
