# forca.py

def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra_secreta = "banana"
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    letras_faltando = str(letras_acertadas.count('_'))
    print('Ainda faltam acertar {} letras'.format(letras_faltando))

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")


if(__name__ == '__main__'):
    jogar()
