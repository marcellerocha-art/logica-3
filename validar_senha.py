senha = input("Digite uma senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

caracteres_especiais = "!@#$%&*()-_=+/?"

for caractere in senha:

    if caractere.isupper():
        tem_maiuscula = True

    elif caractere.islower():
        tem_minuscula = True

    elif caractere.isdigit():
        tem_numero = True

    elif caractere in caracteres_especiais:
        tem_especial = True

erros = []

if len(senha) < 8:
    erros.append("Mínimo de 8 caracteres")

if not tem_maiuscula:
    erros.append("Falta letra maiúscula")

if not tem_minuscula:
    erros.append("Falta letra minúscula")

if not tem_numero:
    erros.append("Falta número")

if not tem_especial:
    erros.append("Falta caractere especial")

if len(erros) == 0:
    print("Senha forte")
else:
    print("A senha não atende aos seguintes requisitos:")

    for erro in erros:
        print("-", erro)