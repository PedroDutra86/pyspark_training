"""
Formatação básia de strings
s- string
d - int
f - float
<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
< - Esquerda
> - Direita
^ - Centro
Sinal - + ou -
Ex: 0>-100,.1f
conversion flags - !r !s !a
"""

variable = 'ABC'
print(f'{variable}')
print(f'{variable::>10}')
print(f'{variable:u<10}.')
print(f'.{variable:-^10}.')
print(f'{1000.14184120971:+,.2f}')
print(f'{1000.14184120971:0>+11,.2f}')
print(f'{1000.14184120971:0=+11,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variable!r}') #__repr__ que retorna uma string com a representação oficial do objeto.
print(f'{variable!s}') #__str__ que retorna a representação em string "legível" do objeto.
print(f'{variable!a}') #__ascii__ que retorna uma string escapando caracteres não-ASCII.