"""
Exercício 2
Peça ao usuario para digitar seu nome
Peça ao usúario para digitar seua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {}
        Seu nome invertido é {nome invertido}
        Se nome contém ( ou não ) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
exiba "Desculpas, você deixou campos vazios"
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    
    if " " in nome:
        print("Seu nome contem espaços")
    else:
        print("Seu nome não contém espaços")
        
    print(f"Seu nome tem {len(nome)} letras ")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A primeira letra do seu nome é {nome[-1]}")
else:
    print("Desculpas, você deixou campos vazios.")