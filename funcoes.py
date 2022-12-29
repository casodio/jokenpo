from random import choice
from rich import print
import os

var = ['1', '2', '3']
bot = choice(var)
seunome = ['Que nome feio.', '  kkkk. é oque?', 'Que nome hein, rsrsrs.', '... O escrivão errou ou seu nome ta correto?', 
'Só tinha esse nome quando você nasceu?', 'Pensei que era ENZO']
empate = ['Hum.. você parece ser bom.', 'Você quase ganhou de mim', 'Você quase conseguiu.', 'Eu quase ganhei.', 'Na proxima eu ganho.',
'você teve sorte de eu não ganhar de você!!']
ganhou = ['É... você parece bom.', 'Foi sorte.', 'Meu programador é muito burro rsrsrs.', 'Estou com azar hoje!!', 
'Você deixou eu jogar primeiro e viu minha jogada.','Meu programador não entende de lógica.', 'Meus algoritmos estão loucos.',
 'Meu programador não previu isso!!', 'Quem me programou não sabe jogar isso, por isso você ganhou!']
perdeu = ['Você foi bom garoto... mas enquantou eu exixtir você será sempre o segundo melhor', 
'Haha.. eu sou o melhor', 'Tente de novo, quem sabe na proxima', 'Você não é pareo para mim!', 'Admita, eu sou o melhor...',
 'Não vai chorar hein', 'Hann, o nenenzinho perdeu...', 'Treine bastante garoto, quem sabe um dia você ganhe de mim.', 'Quem é o melho???']
cont = ['Ei, presta atenção no que você está digitando!', 'É "s" ou "n". parece dificil?', 'Você não sabe o que está digitando?', 
'OMG... você não sabe o que está acontecendo.', 'Você não sabe ler, só pode!!!', '"s" ou "n"... quer q eu desenhe?']
saida = '''Gostou de jogar??
entra em contato:
###########################################################

|---------------------------------------------------------|
|          Autor - [bold][underline]Marcio Maia[/][/]                            |
|***********************[bold]Contatos[/]**************************|
| [bold magenta]E-mail:[/] marciojesusmaia@hotmail.com                     |
| [bold cyan]Linkedin:[/] https://www.linkedin.com/in/marciojesusmaia/  |
| [bold green]Telefone/Whatsapp:[/] 55 85 98614-9863                     |
|---------------------------------------------------------|

############################################################'''

opcaoerrada = ['Opção errada.', 'Não está vendo as opções: 1, 2 ou 3!', 'Você sabe ler??', 
'Tá de brincadeira comigo?', 'Seu teclado não tem as teclas solicitadas?']


def linha():
    print('\n')

def menu():
    print('*'*34)
    print('|','ESCOLHA UMA DAS OPÇÕES'.center(30),'|')
    print('*'*34)
    print('|',' [1] - PEDRA'.ljust(30),'|')
    print('|',' [2] - PAPEL'.ljust(30),'|')
    print('|',' [3] - TESOURA'.ljust(30),'|')
    print('*'*34)


def escolha():
    escolha = input('Escolha a jogada: ')
    bot = choice(var)

    while escolha not in ['1','2','3']:
        os.system('clear')
        print('[red][bold]'+choice(opcaoerrada))
        menu()
        escolha = input('Escolha a jogada: ')
        
    # EMPATE
    if escolha == '1' and bot == '1':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[purple]Empatamos')
        print('[yellow]'+choice(empate))

    elif escolha == '2' and bot == '2':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[purple]Empatamos')
        print('[yellow]'+choice(empate))

    elif escolha == '3' and bot == '3':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[purple]Empatamos')
        print('[yellow]'+choice(empate))

    # JOGADOR VENCE
    elif escolha == '1' and bot == '3':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[green]Você ganhou')
        print('[red]'+choice(ganhou))

    elif escolha == '2' and bot == '1':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[green]Você ganhou')
        print('[red]'+choice(ganhou))
        
    elif escolha == '3' and bot == '2':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[green]Você ganhou')
        print('[red]'+choice(ganhou))

    # JOGADOR PERDE

    elif escolha == '1' and bot == '2':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[red]Você perdeu hehe')
        print('[green]'+ choice(perdeu))

    elif escolha == '2' and bot == '3':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[red]Você perdeu hehe')
        print('[green]'+choice(perdeu))

    elif escolha == '3' and bot == '1':
        print(f'você jogou {escolha} e eu joguei {bot}')
        print('[red]Você perdeu hehe')
        print('[green]'+choice(perdeu))


def sair():
    exit()
