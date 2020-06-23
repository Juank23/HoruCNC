import cv2
import numpy as np


class Filter:
    def __init__(self):
        self.slider_max = 255
        self.threshold = 75
        self.config_section = None
        self.conf_file = None

    def meta(self):
        return {
            "filter": self.config_section,
            "name":"Black & White",
            "description":"Adjust the threshold until you see only your parts",
            "params": ["threshold"]
        }

    def configure(self, config_section, conf_file):
        self.config_section = config_section
        self.conf_file = conf_file
        self.threshold = self.conf_file.get_int("threshold", self.config_section)

    def process(self, image, cnt, code):
        (thresh, blackAndWhiteImage) = cv2.threshold(image, self.threshold, 255, cv2.THRESH_BINARY)

        thumb = cv2.resize(blackAndWhiteImage, (0, 0), None, .3, .3)

        return blackAndWhiteImage, cnt, code

    def set_threshold(self, val):
        self.threshold = val
        self.conf_file.set("threshold", self.config_section, str(val))

