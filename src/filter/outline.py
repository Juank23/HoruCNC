import cv2
import numpy as np


class Filter:
    def __init__(self):
        self.config_section = None
        self.conf_file = None

    def meta(self):
        return {
            "filter": self.config_section,
            "name": "Outline",
            "description":"Generates the outline of your black-white image",
            "params": []
        }

    def configure(self, config_section, conf_file):
        self.config_section = config_section
        self.conf_file = conf_file

    def process(self, image, cnt, code):
        kernel = np.ones((3,3),np.uint8)

        # remove white single pixels
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

        # outline
        image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

        return image, cnt, code