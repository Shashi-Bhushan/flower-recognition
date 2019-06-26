#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.config import Config
from image.util import ImageUtil
from image.util import FileUtil
from PIL import Image

import os


def main():
    image_util = ImageUtil()
    file_util = FileUtil()

    config_parser = Config()

    ideal_image_dimensions = config_parser.get_config_dimensions()

    images_dict = image_util.get_images_list(config_parser.get_images_directory_path())

    os.makedirs(file_util.get_dir_path("images", "target"), exist_ok=True)

    for dir_name, images in images_dict.items():
        os.makedirs(file_util.get_dir_path("images", "target", dir_name), exist_ok=True)

        for image_str in images:
            image = Image.open(file_util.get_dir_path("images/flowers", dir_name, image_str))

            resize_tuple = image_util.create_resize_tuple(ideal_image_dimensions[0]/float(ideal_image_dimensions[1]),
                                                          image.size[0], image.size[1])

            new_image = image_util.resize_image(image, resize_tuple, ideal_image_dimensions)

            new_image.save(file_util.get_dir_path("images/target", dir_name, image_str))
            break


if __name__ == "__main__":
    main()
