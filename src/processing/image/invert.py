
class Filter:
    def __init__(self):
        self.conf_section = None
        self.conf_file = None
        self.icon = None

    def meta(self):
        return {
            "filter": self.conf_section,
            "name":"Invers Black&White",
            "description":"The filter inverts a Black&White image",
            "parameters": [],
            "input": "image",
            "output": "image",
            "icon": self.icon
        }

    def configure(self, global_conf, conf_section, conf_file):
        self.conf_section = conf_section
        self.conf_file = conf_file

    def process(self, image, cnt):
        return (255-image), cnt


    def stop(self):
        pass

