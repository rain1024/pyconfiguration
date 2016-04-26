# -*- coding: utf-8 -*-

__author__ = 'Brother Rain'
__email__ = 'brother.rain.1024@gmail.com'
__version__ = '0.1.0'
import json


class Configuration:
    def __init__(self):
        pass

    @staticmethod
    def load_config(file_name):
        with open(file_name) as data_file:
            data = json.load(data_file)
            Configuration.__dict__.update(data)
