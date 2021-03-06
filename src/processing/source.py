import os
import sys
import cv2
from scanner_camera import Camera as Scanner
import base64
import numpy as np

CWD_PATH = os.path.dirname(os.path.realpath(__file__))


class ImageSource:
    def __init__(self):
        self.conf_section = None
        self.conf_file = None
        self.icon = None
        self.capture = None
        self.factor = 1
        self.width=320
        self.camera = None
        self.uploaded_image = None

    def meta(self):
        return {
            "filter": self.conf_section,
            "name":"Camera",
            "description":"Place the image in front of your camera and zoom in to focus",
            "parameters": [],
            "icon": self.icon
        }

    def configure(self, global_conf, conf_section, conf_file):
        self.conf_section = conf_section
        self.conf_file = conf_file

        self.factor = self.conf_file.get_int("zoom", self.conf_section)
        self.width = self.conf_file.get_int("width", self.conf_section)
        print("CREATE CAMERA")
        self.camera = Scanner()
        print(self.camera)


    def set_image(self, val):
        if val == None:
            self.uploaded_image = None
        else:
            bytearray = base64.b64decode(val)
            png_as_np = np.frombuffer(bytearray, dtype=np.uint8)
            self.uploaded_image = self.__resize(cv2.imdecode(png_as_np, flags=cv2.IMREAD_COLOR), width=self.width)


    def get_image(self):
        try:
            if self.uploaded_image is None :
                readed = self.camera.capture.read()
                if readed is None:
                    return None
                return  self.__resize(readed, width=self.width)
            else:
                return self.uploaded_image
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(self.conf_section, exc)
        return None


    def __resize(self, image, width = None, height = None, inter = cv2.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation = inter)

        # return the resized image
        return resized


    def __zoom(self, image, zoom_size):
        height, width, channels = image.shape
        new_dim = (int(zoom_size * width), int(zoom_size * height))
        image = cv2.resize(image, new_dim, interpolation = cv2.INTER_AREA)
        from_width = int(new_dim[0]/2)- int(width/2)
        to_width =from_width+width

        from_height = int(new_dim[1]/2)- int(height/2)
        to_height =from_height+height

        return image[from_height:to_height,from_width:to_width]


    def stop(self):
        Scanner.stop()
        pass

