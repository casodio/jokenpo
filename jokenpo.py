# JOGO PEDRA PAPEL TESOURA EM MODO CONSOLE PARA DIVERSÃO
from time import sleep
from funções import *
import os
from rich import print


print('*'*80)
linha()
print('Este é o [yellow][bold]PEDRA, PAPEL, TESOURA[/][/] mais divertido que você ja jogou!!'.center(80))
linha()
print('*'*80)
sleep(5)
os.system('clear')

print('\n','Olá, bem vindo ao jogo Pedra, Papel, Tesoura.')
sleep(0)
linha()
print('Meu nome é [bold][underline][purple]M4X[/][/][/] e eu serei seu adversario!!')
sleep(0)
print('Vamos jogar?')
input('Pressione < Enter > para prosseguir ')
os.system('clear')

n = input('Digite seu nome jogador: ')

if n in 'M4Xm4x':
    linha()

    print('Humm, meu chara. Vamos ver se você é tão bom quanto eu!!')
else:
    linha()
    print(f'{n}?, {choice(seunome)}')


while True:
    menu()
    linha()
    escolha()
    

    continuar = input('Deseja continuar jogando(s/n)? ').lower()
    while continuar not in ['s','n']:
        os.system('clear')
        print(choice(cont), '\n')
        continuar = input('Deseja continuar jogando(s/n)? ').lower()
  
    if continuar == 's':
        os.system('clear')

    elif continuar == 'n':
        os.system('clear')
        print(saida)
        sleep(3)
        sair()

        

