from random import randint

numberunknown = randint(0,1000)

def stop():
    print('Você DESISTIU. :(')

def close():
    print('Fim do Jogo')

def option():
    print(' ')
    questionuser = input('Quer tentar mais uma vez? [Sim ou Não] ')
    if questionuser == 'sim':
        again()
    if questionuser == 'não':
        stop()

print('Eu tenho um número secreto. Você consegue descobrir qual é?')
def again():
    tryuser = int(input('Digite um número: '))

    baixo = numberunknown - 10
    alto = numberunknown + 10
    if tryuser < baixo:
        print('Chutou muito baixo.')
        option()

    if tryuser > alto:   
        print('Chutou alto demais.')
        option()
    
    if tryuser == numberunknown:
        print('PARABÉNS! Você acertou!')
        close()
    else:
        option()

again()