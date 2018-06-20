from test import numerals
import unittest


class TestNumeralConverter(unittest.TestCase):
    numeral_engine = None

    numeral_dict = {
        1:"I", 2:"II", 3:"III", 4:'IV', 5:'V', 6:'VI', 8:'VIII', 9:'IX', 10:'X',
        11:'XI', 13:'XIII', 14:'XIV', 15:'XV', 16:'XVI', 18:'XVIII', 19:'XIX', 20:'XX',
        30:'XXX', 40:'XL', 49:'XLIX', 50:'L', 80:'LXXX', 90:'XC', 99:'XCIX', 100:'C',
        149:'CXLIX', 349:'CCCXLIX', 449:'CDXLIX', 849:'DCCCXLIX', 999:'CMXCIX', 1000:'M',
        1499:'MCDXCIX', 1999:'MCMXCIX', 2000:'MM', 0:"Invalid number for conversion", "A":"Invalid number for conversion"
    }

    def setUp(self):
        self.numeral_engine = numerals.NumeralConverter()

    def test_all(self):
        for number in self.numeral_dict.keys():
            self.assertEqual(self.numeral_dict[number], self.numeral_engine.convert(number), "testing: %s" %(number))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
