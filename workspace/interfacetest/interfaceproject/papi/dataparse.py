__author__ = 'Administrator'

# -*-coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'dongjie'
__data__ = '2015-05-21'
import json
import xmltodict
from interfaceproject.pyapilog import pyapilog

# 解析json字符串
class jsonprase(object):
    def __init__(self, json_value):
        try:
            self.json_value = json.loads(json_value)
        except ValueError as e:
            pyapilog().error(e)

    def find_json_node_by_xpath(self, xpath):
        elem = self.json_value
        nodes = xpath.strip("\"").split("\"")
        for x in range(len(nodes)):
            try:
                elem = elem.get(nodes[x])
            except AttributeError:
                elem = [y.get(nodes[x]) for y in elem]
        return elem

    def json_exit(self):
        try:
            falag = self.json_value["success"]
        except KeyError as e:
            falag = pyapilog().error(e)
        return falag

    def datalength(self, xpath="/"):
        return len(self.find_json_node_by_xpath(xpath))

    @property
    def json_to_xml(self):
        try:
            root = {"root": self.json_value}
            xml = xmltodict.unparse(root, pretty=True)
        except ArithmeticError as e:
            pyapilog().error(e)
        return xml


# 解析xml字符串
class xmlprase(object):
    def __init__(self, xml_value):
        self.xml_str = xml_value

    @property
    def xml_to_json(self):
        try:
            xml_dic = xmltodict.parse(self.xml_str,
                                      encoding="utf-8",
                                      process_namespaces=True,
                                      )
            json_str = json.dumps(xml_dic)
        except Exception as e:
            print(e)
        return json_str