import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        image = image_left.copy()

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if j > column:
                    image[i][j][0] = image_right[i][j][0]
                    image[i][j][1] = image_right[i][j][1]
                    image[i][j][2] = image_right[i][j][2]
        return image

    def color_slicing(self, color_image, blackwhite_image, target_color, threshold):
        """
        Perform color slicing to create an image where only the targeted color is preserved and the rest
        is black and white

        color_image: the input color image
        blackwhite_image: the input black and white image
        target_color: the target color to be extracted
        threshold: the threshold to determine the pixel to determine the prximity to the target color

        return: output_image
        """

        image = color_image.copy()
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                dis = (image[i][j][0]-target_color[0])**2 + (image[i][j][1]-target_color[1])**2 + (image[i][j][2]-target_color[2])**2
                dis = math.sqrt(dis)
                # print(dis, threshold)
                if dis > threshold:
                    image[i][j][0] = blackwhite_image[i][j][0]
                    image[i][j][1] = blackwhite_image[i][j][1]
                    image[i][j][2] = blackwhite_image[i][j][2]

        # final = gray_image * mask_in


        return image

   