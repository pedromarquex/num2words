class NumToWords:
    def __init__(self):
        self.low_numwords = ['', 'um', 'dois', 'tres', 'quatro', 'cinco',
                             'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
                             'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
        self.dozens = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta',
                       'sessenta', 'setenta', 'oitenta', 'noventa']
        self.hundreds = ['0', 'cento', 'duzentos', 'trezentos', 'quatrocentos',
                         'quinhentos', 'seissentos', 'setecentos', 'oitocentos',
                         'novecentos']

    def __get_parts(self, num):
        integer_part, decimal_part = map(
            lambda part: part.strip(),
            num.split(','))
        return integer_part, decimal_part

    def __convert(self, number):
        words = []
        num = int(number)
        if num == 0:
            return
        if num < 1000000 and num > 100000:
            n = num // 100000
            words.append(self.hundreds[n])
            num = num % 100000
        if num < 100000 and num > 10000:
            n = num // 10000
            words.append('e') if len(words) > 0 else None
            words.append(self.dozens[n])
            num = num % 10000
        if num < 10000 and num > 999:
            if num // 1000 == 1:
                words.append('mil')
                num = num % 1000
            else:
                n = num // 1000
                words.append('e') if len(words) > 0 else None
                words.append(self.low_numwords[n])
                words.append('mil')
                num = num % 1000
        if num < 1000 and num > 99:
            if num / 100 == 1 and num % 100 == 0:
                words.append('cem')
            else:
                n = num // 100
                words.append(self.hundreds[n])
                num = num % 100
        if num < 100 and num > 19:
            n = num // 10
            words.append('e') if len(words) > 0 else None
            words.append(self.dozens[n])
            num = num % 10
        if num > 0 and num <= 19:
            words.append('e') if len(words) > 0 else None
            words.append(self.low_numwords[num])

        return ' '.join(words)

    def perform_convert(self, num):
        final_words = []
        integer_part, decimal_part = map(
            lambda part: int(part),
            self.__get_parts(num)
        )
        integer_returned = self.__convert(integer_part)
        final_words.append(integer_returned +
                           ' reais') if integer_returned is not None else None
        decimal_returned = self.__convert(decimal_part)
        final_words.append('e ' + decimal_returned +
                           ' centavos') if decimal_returned is not None else None

        return ' '.join(final_words)
