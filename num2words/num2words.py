class NumToWords:
	def __init__(self):
		self.low_numwords = ['', 'um', 'dois', 'três', 'quatro', 'cinco',
			'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
			'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
		self.dozens = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta',
			'sessenta', 'setenta', 'oitenta', 'noventa']
		self.hundreds = ['0', 'cem', 'duzentos', 'trezentos', 'quatrocentos',
			'quinhentos', 'seissentos', 'setecentos', 'oitocentos',
			'novecentos']

	def __get_parts(self, num):
		integer_part, decimal_part = map(
			  lambda part : part.strip(),
			   num.split(','))
		return integer_part, decimal_part

	def __convert(self, number):
		words = []
		num = int(number)
		if num == 0:
			return
		if num < 1000 and num > 99:
			pass
		if num < 100 and num > 19:
			n = num // 10
			words.append(self.dozens[n])
			num = num % 10
		if num > 0 and num <= 19:
			words.append('e') if len(words) > 0 else None
			words.append(self.low_numwords[num])

		return ' '.join(words)

	def perform_convert(self, num):
		final_words = []
		integer_part, decimal_part = map(
			lambda part : int(part),
			self.__get_parts(num)
			)
		integer_returned = self.__convert(integer_part)
		final_words.append(integer_returned + ' reais') if integer_returned is not None else None
		decimal_returned = self.__convert(decimal_part)
		final_words.append('e ' + decimal_returned + ' centavos') if decimal_returned is not None else None

		return ' '.join(final_words)

