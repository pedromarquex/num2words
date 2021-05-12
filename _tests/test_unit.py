import unittest
from num2words.num2words import NumToWords


class TestNum2Words(unittest.TestCase):
    def test_convert(self):
        converter = NumToWords()
        self.assertEqual(
            converter.perform_convert('99,00'),
            'noventa e nove reais'
        )
        self.assertEqual(
            converter.perform_convert('90,00'),
            'noventa reais'
        )
        self.assertEqual(converter.perform_convert(
            '22,00'), 'vinte e dois reais')
        self.assertEqual(converter.perform_convert('15,00'), 'quinze reais')
        self.assertEqual(converter.perform_convert('2,00'), 'dois reais')
        self.assertEqual(converter.perform_convert('2,99'),
                         'dois reais e noventa e nove centavos')
        self.assertEqual(converter.perform_convert(
            '2,90'), 'dois reais e noventa centavos')
        self.assertEqual(converter.perform_convert(
            '2,20'), 'dois reais e vinte centavos')
        self.assertEqual(converter.perform_convert(
            '2,15'), 'dois reais e quinze centavos')
        self.assertEqual(converter.perform_convert(
            '2,02'), 'dois reais e dois centavos')
        self.assertEqual(converter.perform_convert('200,02'),
                         'duzentos reais e dois centavos')
        self.assertEqual(converter.perform_convert(
            '100,02'), 'cem reais e dois centavos')
        self.assertEqual(converter.perform_convert('120,02'),
                         'cento e vinte reais e dois centavos')
        self.assertEqual(converter.perform_convert('121,02'),
                         'cento e vinte e um reais e dois centavos')
        self.assertEqual(converter.perform_convert('999,99'),
                         'novecentos e noventa e nove reais e noventa e nove centavos')
        self.assertEqual(converter.perform_convert('9999,99'),
                         'nove mil novecentos e noventa e nove reais e noventa e nove centavos')
        self.assertEqual(converter.perform_convert('1999,99'),
                         'mil novecentos e noventa e nove reais e noventa e nove centavos')
        self.assertEqual(converter.perform_convert('9999,99'),
                         'nove mil novecentos e noventa e nove reais e noventa e nove centavos')
        self.assertEqual(converter.perform_convert('99999,99'),
                         'noventa e nove mil novecentos e noventa e nove reais e noventa e nove centavos')
        self.assertEqual(converter.perform_convert('999999,99'),
                         'novecentos e noventa e nove mil novecentos e noventa e nove reais e noventa e nove centavos')


if __name__ == '__main__':
    unittest.main()
