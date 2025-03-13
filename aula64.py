import random

for cpf in range(100):
	cpf_first_nine_digits = ''
	for index in range(9):
		cpf_first_nine_digits += str(random.randint(0, 9))

	countdown = 10
	first_digit_accumulator = 0

	for digit in cpf_first_nine_digits:
		first_digit_accumulator += int(digit) * countdown
		countdown -= 1

	first_digit = (first_digit_accumulator * 10) % 11
	first_digit = first_digit if first_digit <= 9 else 0

	cpf_first_ten_digits = cpf_first_nine_digits + str(first_digit)
	countdown = 11

	second_digit_accumulator = 0
	for digit in cpf_first_ten_digits:
		second_digit_accumulator += int(digit) * countdown
		countdown -= 1

	second_digit = (second_digit_accumulator * 10) % 11

	second_digit = second_digit if second_digit <= 9 else 0

	formatted_cpf_first_nine_digits = f'{cpf_first_nine_digits[:3]}.{cpf_first_nine_digits[3:6]}.{cpf_first_nine_digits[6:]}'

	generated_cpf = f'{formatted_cpf_first_nine_digits}-{first_digit}{second_digit}'

	print(f'CPF Gerado: {generated_cpf}')
