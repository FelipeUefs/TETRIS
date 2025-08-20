#/*******************************************************************************
#Autor: Felipe Gomes da Silva
#Componente Curricular: Algoritmos I
#Concluido em: 29/10/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/
#SISTEMA OPERACIONAL: WINDOWS 10
#VERSÃO DO PYTHON: 3.12.7

#BLOCO 1 - DEFINIÇÃO e CRIAÇÃO

import curses #necessario pip install windows-curses
import random #necessario para peças e posições aleatorias
import time #importa o tempo de caida da peça

#Gerar tabuleiro
#Cria uma matriz de 20x10
def criar_tabuleiro():
    tabuleiro_1 = []
    for y in range(20):
        linha = []
        for x in range(10):
            linha.append('⬜')
        tabuleiro_1.append(linha)
    return tabuleiro_1

#Peças do tetris
I = [['🟦', '🟦', '🟦', '🟦']]
O = [['🟦', '🟦'],
     ['🟦', '🟦']]
T = [['🟦', '🟦', '🟦'],
     ['⬜', '🟦', '⬜']]
S = [['⬜', '🟦', '🟦'],
     ['🟦', '🟦', '⬜']]
Z = [['🟦', '🟦', '⬜'],
     ['⬜', '🟦', '🟦']]
J = [['🟦', '⬜', '⬜'],
     ['🟦', '🟦', '🟦']]
L = [['⬜', '⬜', '🟦'],
     ['🟦', '🟦', '🟦']]
B = [['🧨']]
# Lista de peças
pedras = [I, O, T, S, Z, J, L, B]

#Escolher uma peça aleatória
def pedra_aleatoria():
    return random.choice(pedras)

#definição da bombinha
def bomba(tabuleiro):
    #cria a matriz 3x3 para a bombinha
    for i in range(len(tabuleiro)): 
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == '🧨' and j != 0:
                for h in range (-1, 2):
                    for m in range (-1, 2):
                        try: #verifica os blocos dentro do alcance
                            if tabuleiro[i+h][j+m] != '⬜':
                                tabuleiro[i+h][j+m] = '⬜'
                        except IndexError:
                            pass
            elif tabuleiro[i][j] == '🧨' and j == 0:
                for h in range (-1, 2):
                    for m in range (0, 2):
                        try: #verifica os blocos dentro do alcance
                            if tabuleiro[i+h][j+m] != '⬜':
                                tabuleiro[i+h][j+m] = '⬜'
                        except IndexError: 
                            pass

#FIM DO BLOCO 1 --

#BLOCO 2 - EXIBIÇÃO    

#Exibir o tabuleiro e limpar
def aparecer_tab(telinha, tabuleiro, total_pontos):
    telinha.clear()  #Limpa a tela
    for linha in tabuleiro:
        telinha.addstr (''.join(linha) + '\n')  #Deixa os blocos organizados e bonitos
    telinha.addstr (f'Pontuação: {total_pontos}\n'
                    'CLIQUE [W] PARA GIRAR\n'
                    'CLIQUE [A] PARA MOVER PARA ESQUERDA\n'
                    'CLIQUE [D] PARA MOVER PARA DIREITA\n'
                    'CLIQUE [S] PARA DESCER MAIS RÁPIDO\n\n'
                    'NÃO PRESSIONE A TECLA, ISSO PODE CAUSAR PROBLEMAS\n'
                    'DESATIVE O CAPSLOCK')
    telinha.refresh()  #Atualiza a tela

# Colocar peça no tabuleiro e verifica se está nos limites
def colocar_pedra(peca, inicio_x, inicio_y, tabuleiro):
    for y, linha_1 in enumerate(peca):
        for x, bloco in enumerate(linha_1):
            if bloco != '⬜' and (inicio_x + x) < 10: #limite de tela
                tabuleiro[inicio_y + y][inicio_x + x] = bloco

#Limpar peça do tabuleiro
def limpar_pedra(peca, inicio_x, inicio_y, tabuleiro):
    for y, linha_1 in enumerate(peca):
        for x, bloco in enumerate(linha_1):
            if bloco != '⬜' and (inicio_x + x) < 10: #limite de tela
                tabuleiro [inicio_y + y][inicio_x + x] = '⬜'

#FIM DO BLOCO 2 --

#BLOCO 3 - MOVIMENTAÇÃO E FIXAÇÃO

#Mover peça para baixo
def descer(peca, inicio_x, inicio_y, tabuleiro):
    if colisao(peca, inicio_x, inicio_y + 1, tabuleiro):
        return inicio_y
    else:
        limpar_pedra(peca, inicio_x, inicio_y, tabuleiro) #Limpar peça
        inicio_y += 1  #Move a peça para baixo
        colocar_pedra(peca, inicio_x, inicio_y, tabuleiro)  #Coloca a peça na nova posição
        return inicio_y  #Retorna a nova posição

#mover peça para esquerda e direita
def mover(peca, inicio_x, inicio_y, tabuleiro, direcionar):
    nova_posicao_x = inicio_x + direcionar
    #Verifica se pode mover ou não
    if not colisao(peca, nova_posicao_x, inicio_y, tabuleiro):
        limpar_pedra(peca, inicio_x, inicio_y, tabuleiro)
        inicio_x = nova_posicao_x
        colocar_pedra(peca, inicio_x, inicio_y, tabuleiro)
    return inicio_x

#rotacionar a peça no tabuleiro
def rotacionar(pedra_vindo):
    rotacionar = [list(linha) for linha in zip(*reversed(pedra_vindo))]
    return rotacionar

#Verificar colisão
def colisao(peca, inicio_x, inicio_y, tabuleiro):
    for y, linha_1 in enumerate(peca):
        for x, bloco in enumerate(linha_1):
            if bloco != '⬜' :
                #Fixa as peças uma na outra, sem isso elas atravessam umas as outras
                fixa_x = inicio_x + x
                fixa_y = inicio_y + y
                if fixa_x < 0 or fixa_x >= len(tabuleiro[0]) or fixa_y >= len(tabuleiro):
                    return True
                if fixa_y < len(tabuleiro) and tabuleiro[fixa_y][fixa_x] != '⬜':
                    return True
    return False

#FIM DO BLOCO 3 --

#BLOCO 4 - PONTUAÇÃO E DIFICULDADE

#Função para eliminar linhas e contabilizar pontos
def eliminar_linhas(tabuleiro):
    #define as variaveis para contabilizar os pontos e linhas eliminadas
    eliminar = 0
    pontos = 0
    peso = 100
    for i, linha in enumerate(tabuleiro): #Verifica as linhas completas para eliminação
        if linha == ['🟦' for _ in range(10)]:
            tabuleiro.pop(i) #Retira as linhas completas
            tabuleiro.insert(0 , ['⬜' for _ in range(10)]) #Insere uma linha branca no topo 
            eliminar += 1 #contagem de linhas eliminadas
            pontos += 1 #pontos
    if eliminar > 0: #eliminação simultanea/multiplicador de pontos
        if eliminar == 1:
            pontos = peso * 1
        elif eliminar == 2:
            pontos = peso * 4
        elif eliminar == 3: 
            pontos = peso * 6
        elif eliminar == 4:
            pontos = peso * 8
    return pontos

#atualiza a velocidade quando chegar a determinada pontuação
def nova_vel(pontos, velocidade):
    if pontos >= 800:
        return 0.1
    else:
        return velocidade

#FIM DO BLOCO 4 --   

#BLOCO 5 - CODIGO PRINCIPAL
#menu do jogo 
menu = 0
print('TETRIS THE NEW GAME\n')
while menu != 2:
    print('MENU PRINCIPAL\n')
    menu = int(input('[1] NOVO JOGO\n'
                    '[2] FECHAR\n'))
    #verificação de erro de digitação
    while menu not in (1, 2): 
        print('MENU PRINCIPAL\n')
        menu = int(input('OPÇÃO INVALIDA, DIGITE:\n'
                    '[1] PARA NOVO JOGO\n'
                    '[2] PARA FECHAR\n'))
    #Inicialização do tabuleiro do TETRIS
    if menu == 1:
        def play_nojogo(telinha):
            tabuleiro = criar_tabuleiro() #Usa o tabuleiro gerado
            telinha.nodelay(2) #ter melhor tempo de resposta nos clicks
            fim = False
            total_pontos = 0 
            velocidade = 0.4 #velocidade atual
            #Looping das peças
            while not fim:
                pedra_vindo = pedra_aleatoria()  #Escolhe a peça que vai cair
                tamanho_tabuleiro = len(tabuleiro[0])  #Tamanho do tabuleiro
                tamanho_pedra = len(pedra_vindo[0])  #Tamanho da peça
                #Posicionamento inicial aleatório
                posicionamento_x = random.randint(0, tamanho_tabuleiro - tamanho_pedra)
                posicionamento_y = 0 #Começa do topo
                for i in range(len(tabuleiro)): #Explosão da da bomba
                    for j in range(len(tabuleiro[i])):
                        if tabuleiro[i][j] == '🧨':
                            tabuleiro[i][j] = '⬜'
                #Caso as peças ultrapassem o limite o jogo finaliza e exibe a mensagem
                if colisao(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro):
                    telinha.clear()
                    telinha.addstr(f'GAME OVER! VOCÊ TEVE {total_pontos} PONTOS! ')
                    telinha.refresh()
                    time.sleep(5) #tempo de exibição da mensagem final
                    fim = True
                colocar_pedra(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro)
                posicionamento_y = 0  #Começa do topo
                aparecer_tab(telinha, tabuleiro, total_pontos) #Mostra o tabuleiro
                parar = False
                #looping de funções
                while not parar:
                    #velocidade do jogo atualizada
                    velocidade = nova_vel(total_pontos, velocidade)
                    time.sleep(velocidade) 
                    limpar_pedra(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro)
                    movi = telinha.getch() #captura de tecla
                    if movi == ord('w'): #girar a peça
                        if not colisao(rotacionar(pedra_vindo),posicionamento_x, posicionamento_y, tabuleiro):
                            pedra_vindo = rotacionar(pedra_vindo)
                    elif movi == ord('a'): #Mover para esquerda
                        posicionamento_x = mover(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro, -1)
                    elif movi == ord('d'): #Mover para direita
                        posicionamento_x = mover(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro, 1)
                    elif movi == ord('s'): #Mover para baixo mais rapido
                        if not colisao(pedra_vindo, posicionamento_x, posicionamento_y + 4, tabuleiro):
                            posicionamento_y += 4 #Desce 4 posiçoes a baixo 
                            colocar_pedra(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro)
                            aparecer_tab(telinha, tabuleiro, total_pontos) #Mostra a peça no novo local 
                    #Colisão, coloca as peças no fundo ou sobre as outras
                    elif colisao(pedra_vindo, posicionamento_x, posicionamento_y + 1, tabuleiro): 
                        colocar_pedra(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro)
                        pontos = eliminar_linhas(tabuleiro)
                        total_pontos += pontos
                        #Chama a função da bomba
                        if pedra_vindo == B:
                            bomba(tabuleiro)
                        parar = True
                    #Senão colidir, a peça continua descendo
                    else:
                        posicionamento_y += 1
                    colocar_pedra(pedra_vindo, posicionamento_x, posicionamento_y, tabuleiro)
                    aparecer_tab(telinha, tabuleiro, total_pontos) #Mostra o tabuleiro
        #Puxa todas as funções, inicializando o jogo corretamente
        if __name__ == '__main__':
            curses.wrapper(play_nojogo)
    #Caso o usuario clique 2 ele encerra o programa
    elif menu == 2:
        print(f'ATÉ A PRÓXIMA, OBRIGADO POR JOGAR!')

#FIM DO BLOCO 5 --