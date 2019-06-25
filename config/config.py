#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser


class Config:
    config_parser = configparser.ConfigParser()

    def __init__(self, config_path):
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
        return cls.config_parser['ideal_dimensions']['width'], cls.config_parser['ideal_dimensions']['height']
