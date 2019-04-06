from mixins import JSONable, XMLable
import unittest
class TestMixins(unittest.TestCase):

    #test class
    class Panda(JSONable, XMLable):
        def __init__(self, **kwargs):
            for kwarg, vl in kwargs.items():
                setattr(self, kwarg, vl)

        def __eq__(self, other):
            for k in self.__dict__.keys():
                if self.__dict__[k] != other.__dict__[k]:
                    return False
            return True

    #create test object
    unittest.TestCase.p = Panda(name='Ivo')

    def test_from_xml(self):
        obj = unittest.TestCase.p.from_xml("<Panda><name>Ivo</name></Panda>")
        self.assertEqual(unittest.TestCase.p, obj)

    def test_to_xml(self):
        xml_ivo = unittest.TestCase.p.to_xml()
        #b is for bytes literal
        expected_result = b"<Panda><name>Ivo</name></Panda>"
        self.assertEqual(xml_ivo, expected_result)

    def test_from_json(self):
        obj=unittest.TestCase.p.from_json('{"dict": {"name": "Ivo"}, "type": "Panda"}')
        self.assertEqual(unittest.TestCase.p, obj)

    def test_to_json(self):
        json_ivo = unittest.TestCase.p.to_json()
        expected_result = """{
    "dict": {
        "name": "Ivo"
    },
    "type": "Panda"
}"""
        self.assertEqual(json_ivo, expected_result)


if __name__ =='__main__':
    unittest.main()
