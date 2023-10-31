import unittest
import calc

class test_calc(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    

    def test_add(self):
        #result = calc.addition(10,5)
        self.assertEqual(calc.addition(10,5),15)
        self.assertEqual(calc.addition(-1,1),0)
        self.assertEqual(calc.addition(-1,-1),-2)

    def test_sub(self):
        #result = calc.addition(10,5)
        self.assertEqual(calc.substraction(10,5),5)
        self.assertEqual(calc.substraction(-1,1),-2)
        self.assertEqual(calc.substraction(-1,-1),0)

    def test_div(self):
        #result = calc.addition(10,5)
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)

        self.assertRaises(ValueError,calc.divide,10,0)
if __name__ == '__main__':
    unittest.main()
