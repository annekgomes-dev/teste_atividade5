import unittest
from apps.validators import Validators

class MeuTeste(unittest.TestCase):
    def testar_algo(self):

        result0 = Validators.check_valid_identifier(self,"testdev")
        self.assertTrue(result0)
        result1 = Validators.check_valid_identifier(self,"_testdev")
        self.assertTrue(result1)
        result2 = Validators.check_valid_identifier(self,"1testdev")
        self.assertFalse(result2)
        result3 = Validators.check_valid_identifier(self,"@testdev")
        self.assertFalse(result3)
        result4 = Validators.check_valid_identifier(self,"dv")
        self.assertFalse(result4)
        result5 = Validators.check_valid_identifier(self,"testdevelopment")
        self.assertFalse(result5)

if __name__ == '__main__':
    unittest.main()