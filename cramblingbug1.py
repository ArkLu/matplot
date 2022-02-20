import time

import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate
import os

os.environ['NO_PROXY'] = 'https://www.ip138.com/post'


class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


def get_provinces(url):
    content = requests.get(url).content
    time.sleep(5)
    start = content.find('<map name=\"map_86" id=\"map_86\">')
    end = content.find('</map>')
    content = content[start:end + len('</map>')].strip()
    print(content)
    provinces1 = []
    handler = DefaultSaxHandler(provinces1)
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parser(content)
    return provinces1


provinces2 = get_provinces('http://www.yb21.cn')
print(provinces2)




