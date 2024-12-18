"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Função replace para remover caracteres especificos -  texto.replace('.', '')  # Remove pontos  
                                                      texto.replace('-', '')  # Remove hífens

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0  

expressão regular, para remover caracteres especiais de numero entre o intervalo q eu determinar
re.sub(r"^[intervalo de verificação do que vai ser removido e mantido]", "aqui vai pelo oq vai ser substituido", "aqui é a string que vai ser verificada")
"""

import re

def cpf_treaty():
    cpf = input("Digite um CPF (com ou sem caracteres especiais): ")
    correct_cpf = re.sub(r'[^0-9]', '', cpf)
    return correct_cpf


def calc_first_digit(cpf_user_recept):
    cpf_first_digit = cpf_user_recept[:9]
    counter_first_digit = 10
    first_digit_result = 0
    first_digit = 0

    for digit in cpf_first_digit:
        first_digit_result += int(digit) * counter_first_digit
        counter_first_digit -= 1

    first_digit_result_final = (first_digit_result * 10) % 11

    if first_digit_result_final > 9:
        first_digit = 0
    else:
        first_digit = first_digit_result_final

    return first_digit

def calc_second_digit(cpf_user_recept):
    cpf_second_digit = cpf_user_recept[:10]
    counter_second_digit = 11
    second_digit_result = 0
    second_digit = 0

    for digit in cpf_second_digit:
        second_digit_result += int(digit) * counter_second_digit
        counter_second_digit -= 1

    second_digit_result_final = (second_digit_result * 10) % 11

    if second_digit_result_final > 9:
        second_digit = 0
    else:
        second_digit = second_digit_result_final

    return second_digit

while True:
    cpf_user = cpf_treaty()
    if len(cpf_user) != 11:
        print("Quantidade de digitos invalidos, favor inserir novamente: ")
        continue
    elif cpf_user == cpf_user[0] * len(cpf_user):
        print("CPF com todos os valores iguais, favor inserir um CPF Válido")
        continue

    try:
        int(cpf_user)
    except ValueError:
        print("Digite apenas números e às acentuações")
        continue

    validation_first_digit = calc_first_digit(cpf_user)
    validation_second_digit = calc_second_digit(cpf_user)

    if str(validation_first_digit) == cpf_user[-1] and str(validation_second_digit) == cpf_user[-2]:
        print(f"CPF digitado é Valido, {cpf_user}")
    else:
        print(f"CPF Digitado é Invalido: {cpf_user}")
