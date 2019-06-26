#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser


class Config:
    config_parser = configparser.ConfigParser()

    default_config_path = 'config/config.ini'

    def __init__(self, config_path = default_config_path):
        """
        Constructor for Config

        :param config_path:
            Configuration File Path
        """
        self.config_parser.read(config_path)

    @classmethod
    def get_config_dimensions(cls):
        """
        Return Tuple for Width and Height of ideal dimensions

        :return: (x1,x2) tuple for ideal dimensions
        """
        return int(cls.config_parser['ideal_image_dimensions']['width']), int(cls.config_parser['ideal_image_dimensions']['height'])

    @classmethod
    def get_images_directory_path(cls):
        """
        Return directory path where all the images are present

        :return: images' directory path
        """
        return str(cls.config_parser['directory_path']['path'])

