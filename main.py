#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.config import Config
from image.util import ImageUtil
from PIL import Image

import os

execution_path = os.getcwd()
SOURCE_DIR = os.path.join(execution_path, "images", "flowers")
TARGET_DIR = os.path.join(execution_path, "images", "target")


def main():
    image_util = ImageUtil()

    config_parser = Config()

    ideal_image_dimensions = config_parser.get_config_dimensions()

    images_dict = image_util.get_images_list(config_parser.get_images_directory_path())

    os.makedirs(TARGET_DIR, exist_ok=True)

    # Iterate over the dictionary of images
    for flower_category, images in images_dict.items():
        # Fetch each sub directory (named category of flower)
        os.makedirs(os.path.join(TARGET_DIR, flower_category), exist_ok=True)

        # Iterate over image list
        for image_name in images:
            # Get Source Image
            source_image = Image.open(os.path.join(SOURCE_DIR, flower_category, image_name))

            resize_tuple = image_util.create_resize_tuple(ideal_image_dimensions[0]/float(ideal_image_dimensions[1]),
                                                          source_image.size[0], source_image.size[1])

            target_image = image_util.resize_image(source_image, resize_tuple, ideal_image_dimensions)

            target_image.save(os.path.join(TARGET_DIR, flower_category, image_name))


if __name__ == "__main__":
    main()
