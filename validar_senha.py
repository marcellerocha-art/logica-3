def validar_senha(senha):
    requisitos_ausentes = []
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
    
    if len(senha) < 8:
        requisitos_ausentes.append("Comprimento mínimo de 8 caracteres")
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_especial = True
    
    if not tem_maiuscula:
        requisitos_ausentes.append("Um caracter maiúsculo")
    
    if not tem_minuscula:
        requisitos_ausentes.append("Um caracter minúsculo")
    
    if not tem_numero:
        requisitos_ausentes.append("Um número")
    
    if not tem_especial:
        requisitos_ausentes.append("Um caracter especial")
    
    if not requisitos_ausentes:
        return "Senha forte"
    else:
        return f"Requisitos ausentes: {', '.join(requisitos_ausentes)}"


if __name__ == "__main__":
    print("=" * 60)
    print("VALIDADOR DE COMPLEXIDADE DE SENHA")
    print("=" * 60)
    
    while True:
        senha = input("\nDigite uma senha (ou 'sair' para encerrar): ")
        
        if senha.lower() == 'sair':
            print("Programa encerrado!")
            break
        
        resultado = validar_senha(senha)
        print(f"Resultado: {resultado}")