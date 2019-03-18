from random import randint

def jogar():
    
    imprimir_abertura() 
    palavra = palavra_secreta() 
    letras = iniciar_letras(palavra)
    print(' '.join(letras)) 
    
    enforcou = False
    acertou = False
    erros = 0
   
    while(not acertou and not enforcou):
        index = 0
        chute = input('Qual letra? ').strip().upper()
        if(chute in palavra):
            verificar_letra(palavra, chute, letras, index)
            print(' '.join(letras),'\n')
        else:
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = '_' not in letras
        
    if(acertou):
        imprimir_msg_ganhador()
    else:
        imprimir_msg_perdedor(palavra)
        
       
def imprimir_abertura():
    print('*'*30)
    print('Jogo da Forca'.center(30))
    print('*'*30)
    
def palavra_secreta():
    arquivo = open('palavras.txt','r')
    lista = [] 
    for nome in arquivo:
        lista.append(nome)
    num = randint(0,len(lista))
    palavra = lista[num].strip().upper()
    arquivo.close()
    return palavra

def iniciar_letras(palavra):
    return ['_' for letra in palavra]
    
def verificar_letra(palavra, chute, letras, index):
    for letra in palavra:
                if(chute == letra):
                    letras[index] = letra
                index = index + 1
           
def imprimir_msg_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
 
def imprimir_msg_perdedor(palavra):
    print("Poxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar()

