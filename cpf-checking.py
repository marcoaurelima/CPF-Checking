# Project: CPF-Checking
# Author:  Marco Aurélio Lima
# Created: 12-02-2021

print('-- Checador de CPF --')
print('Digite o CPF:', end=' ')
cpf = input()

cpf_temp = (cpf.split('-')[0])
cpf_temp = (cpf_temp.split('.'))
cpf_temp = ''.join(cpf_temp)

sum_1 = 0
for i, val in enumerate(cpf_temp):
    sum_1 += (int(val) * (10-i))

# if sum is greater than 9, the digit is 0. If not, continues with the same value.
digit_1 = 11-(sum_1%11)
digit_1 = 0 if digit_1 > 9 else digit_1

print()
print(f'Soma 1: {sum_1}')
print(f'11 - ({sum_1} % 11) = {11-(sum_1%11)}')
print(f'Dígito 1: {digit_1}\n')

# Next step, the first digit will be included in the end of cpf sequence.
cpf_temp += str(digit_1)

sum_2 = 0
for i, val in enumerate(cpf_temp):
    sum_2 += (int(val) * (11-i))

# if sum is greater than 9, the digit is 0. If not, continues with the same value.
digit_2 = 11-(sum_2%11)
digit_2 = 0 if digit_2 > 9 else digit_2

print(f'Soma 2: {sum_2}')
print(f'11 - ({sum_2}) % 11) = {11-(sum_2%11)}')
print(f'Dígito 2: {digit_2}\n')

# Now we have the two digits we need.
# I will append the digit_2 to cpf_temp

cpf_temp += str(digit_2)
cpf_temp = f'{cpf_temp[0:3]}.{cpf_temp[3:6]}.{cpf_temp[6:9]}-{cpf_temp[9:11]}'

print('[CPF válido!]' if (cpf == cpf_temp) else '[CPF INVÁLIDO]')
