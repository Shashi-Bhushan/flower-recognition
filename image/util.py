#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os import path

from PIL import Image


class ImageUtil:

    @staticmethod
    def create_resize_tuple(ideal_aspect_ratio, image_width, image_height):
        """
        Get a Resize Tuple based on current aspect ratio of the image

        The Resize tuple will be in square dimensions and the image will be cropped equally from either left and
        right side or top and bottom side. It compares the aspect ratios - depending on whether width or height is
        larger, that will decide whether to chop off the sides or the top and bottom.


        :param ideal_aspect_ratio:
            ideal aspect ratio of the image
        :param image_width:
            width of the image
        :param image_height:
            height of the image
        :return: tuple:
            tuple with 4 entries in form of (x1, x2, y1, y2)
        """

        image_aspect_ratio = image_width/float(image_height)

        # If width is greater than height
        if image_aspect_ratio > ideal_aspect_ratio :
            # Then crop the left and right side edges

            # New Width will be equal to Height
            new_width = image_height

            # Distribute this width equally between both right and left sides
            offset = (image_width - new_width) / 2

            # Create Resize Tuple (x1, x2, y1, y2)
            return offset, 0, image_width - offset, image_height
        else :
            # Then crop the top and bottom side edges

            # New Height will be width
            new_height = image_width

            # Distribute this new height equally between both top and bottom sides
            offset = (image_height - new_height) / 2

            # Create Resize Tuple (x1, x2, y1, y2)
            return 0, offset, image_width, image_height - offset

    @staticmethod
    def get_images_list(directory_path):
        """
        Get a dictionary of images keyed by directories

        :param directory_path:
            directory which has images by types
        :return:
            the dictionary with images list keyed by directories
        """
        if path.exists(directory_path):

            # Create dictionary if path exists
            images_dict = {}

            # Crawl over each flower type directory
            for dir_name in listdir(directory_path):
                # get images list from directory
                images_list = [file_name for file_name in listdir("/".join([directory_path, dir_name]))]

                images_dict[dir_name] = images_list
                break

            return images_dict

    @staticmethod
    def resize_image(image, resize_tuple, ideal_image_dimensions):
        """
        Resize the image to ideal image's dimensions

        :param image:
            the original image to resize
        :param resize_tuple:
            tuple with coordinates for square image in form (x1, x2, y1 ,y2)
        :param ideal_image_dimensions:
            tuple with coordinates for the ideal image in form of (width, height)
        :return:
            cropped image for ideal dimensions
        """
        return image.crop(resize_tuple).resize(ideal_image_dimensions, Image.ANTIALIAS)


class FileUtil:
    @staticmethod
    def get_dir_path(*intermittent_path):
        """
        Append the entries of the list to create a full directory path by joining with '/' character

        :param intermittent_path:
            the entries comprising of the intermediate directories
        :return:
            full path of file or directory
        """
        return "/".join(intermittent_path)
