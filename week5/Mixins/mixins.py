from xml.etree import ElementTree as ET
import json
class JSONable:

    def to_json(self, indent=4):
        my_dict = {}
        my_dict['dict'] = self.__dict__
        my_dict['type'] = type(self).__name__
        return json.dumps(my_dict, indent = indent)

    @classmethod
    def from_json(cls, json_string):
        json_repr = json.loads(json_string)
        if cls.__name__!=json_repr['type']:
            raise ValueError()
        return cls(**json_repr['dict'])


class XMLable:
    def to_xml(self):
        class_name = ET.Element(type(self).__name__)
        for attr_name, val in self.__dict__.items():
            attr = ET.Element(str(attr_name))
            attr.text = val
            class_name.append(attr)

        tree = ET.ElementTree(class_name).getroot()
        return ET.tostring(tree) #bytes literal

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)
        if cls.__name__!=root.tag:
            raise ValueError()

        my_dict = {}
        for child in root:
            my_dict[child.tag] = child.text

        return cls(**my_dict)