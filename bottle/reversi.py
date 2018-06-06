#Game
#Author: Thiago
import os
import sys
import random
import math
import time
import re
from enum import Enum

regra = 'Reversi é um jogo de tabuleiro para dois jogadores, disputado em um tabuleiro 8x8 com 64 discos que possui uma cor escura em um dos lados da face e no outro uma cor clara,cujo o objetivo é ficar com mais peças da sua cor no tabuleiro ao final do jogo. A partida começa com 4 peças no centro do tabuleiro, duas brancas e duas pretas, sendo sempre as brancas na grande diagonal a1-h8. O jogador com as pretas começa a partida colocando uma peça em uma das quatro opções possíveis.'

class color(Enum):
    NENHUM = 0
    BRANCO = 1
    PRETO = 2

# class configuracao():
    
class partida():
    def __init__(self):
        self.jogadores = []
        self.tabuleiro = tabuleiro()
        self.jogadorVez = None
        self.cores = [color.BRANCO, color.PRETO]

    def adicionarJogador(self, jogador):
        if len(self.jogadores) == 2:
            return False
        jogador.cor = self.cores.pop()
        self.jogadores.append(jogador)
    
    def removerJogador(self, nome):
        for j in self.jogadores:
            if j.nome == nome:
                self.cores.append(j.cor)
                self.jogadores.remove(j)
                break
        print('Jogador não encontrado')

    def buscaJogador(self, cor):
        for j in self.jogadores:
            if j.cor == cor:
                return j
        return None

    def defineVez(self):
        if(self.jogadorVez == None):
            for j in self.jogadores:
                if j.cor == color.PRETO:
                    self.jogadorVez = j
                    return self.jogadorVez
        
        for j in self.jogadores:
            if j.cor != self.jogadorVez.cor:
                self.jogadorVez = j
                return self.jogadorVez

    def fim(self):
        pecas = [p for l in list(self.tabuleiro.matris) for p in list(l) if isinstance(p, peca)]
        if pecas.count == 64: 
            return True

        if len(pecas) == 1: 
            return True

        return False
    
    def iniciar(self):
        self.defineVez()
        while(self.fim() == False):
            self.placa()
            self.tabuleiro.desenha(self.jogadorVez.cor)
            novaPeca = None
            while(True):
                posicao = str(input('\nVez do Jogador {}: '.format(self.jogadorVez.nomeColorido()))).lower()
                match = re.search('[12345678][abcdefgh]', posicao)
                if match:
                    novaPeca = peca(int(posicao[0])-1,  self.tabuleiro.alf.index(str(posicao[1]).upper()), self.jogadorVez.cor)
                    if self.tabuleiro.pecaExiste(novaPeca) == False:
                        break
                    else:
                        print('\nJá existe uma peça para essa posição')
                else:
                    print('\nEscolha a linha de 1 a 8 e a coluna A à H: exemplo A1')
                
            self.tabuleiro.adicionaPeca(novaPeca)
            self.tabuleiro.modificaDireitaCores(novaPeca)
            self.tabuleiro.modificaEsquerdaCores(novaPeca)
            self.tabuleiro.modificaBaixoCores(novaPeca)
            self.tabuleiro.modificaCimaCores(novaPeca)
            self.tabuleiro.modificaDireitaBaixoCores(novaPeca)
            self.tabuleiro.modificaEsquerdaBaixoCores(novaPeca)
            self.defineVez()
    def topo(self):
        print('______________________________ \033[91mREVERSI\033[0m_______________________________')
        print('=====================================================================')

    def placa(self):
        self.topo()
        print('Placar')
        for j in self.jogadores:
            print('Jogador {0}: {1}'.format(j.nomeColorido(), self.tabuleiro.contaPecas(j.cor)))

class peca():
    def __init__(self, eixoX, eixoY, color):
        self.eixoX = eixoX
        self.eixoY = eixoY
        self.cor = color

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return other != None and self.eixoX == other.eixoX and self.eixoY == other.eixoY 

class jogador():
    def __init__(self, nome):
        self.nome = nome
        self.cor = None

    def jogar(self, x, y):
        return peca(x, y, self.cor)

    def nomeColorido(self):
        colors = {
        'red'       :   '\033[91m',
        'green'     :   '\033[92m',
        'yellow'    :   '\033[93m',
        'blue'      :   '\033[94m',
        'purple'    :   '\033[95m',
        'cyan'      :   '\033[96m',
        'white'     :   '\033[97m',
        'wild'      :   '',
        'dwild'     :   '',
        'dred'       :   '\033[31m',
        'dgreen'     :   '\033[32m',
        'dyellow'    :   '\033[33m',
        'dblue'      :   '\033[34m',
        'dpurple'    :   '\033[35m',
        'dcyan'      :   '\033[36m',
        'dwhite'     :   '\033[37m',
        }
    
        corPeca = { 
            color.BRANCO : colors['green'], 
            color.PRETO : colors['blue'],
            color.NENHUM: colors['white']
        }
        
        return "{0}{1}{2}".format(corPeca[self.cor], self.nome, corPeca[color.NENHUM])

class tabuleiro():
    def __init__(self):
        self.alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.matris = [[None for x in range(8)] for y in range(8)]
        self.adicionaPeca(peca(3,3, color.BRANCO))
        self.adicionaPeca(peca(4,4, color.BRANCO))
        self.adicionaPeca(peca(4,3, color.PRETO))
        self.adicionaPeca(peca(3,4, color.PRETO))

    def pecaExiste(self, peca):
        return self.matris[peca.eixoX][peca.eixoY] != None

    def adicionaPeca(self, peca):
        self.matris[peca.eixoX][peca.eixoY] = peca

    def modificaDireitaCores(self, peca):
        pecas = []
        for p in self.matris[peca.eixoX][peca.eixoY+1:8]:
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)

    def modificaEsquerdaCores(self, peca):
        pecas = []
        for p in reversed(self.matris[peca.eixoX][0:peca.eixoY]):
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)

    def modificaBaixoCores(self, peca):
        pecas = []        
        for index in range(peca.eixoX+1, 8):
            p = self.matris[index][peca.eixoY]
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)

    def modificaEsquerdaBaixoCores(self, peca):
        pecas = []
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y -=1
            p = self.matris[index][y]
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)

    def modificaDireitaBaixoCores(self, peca):
        pecas = []
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y +=1
            p = self.matris[index][y]
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)
    
    def modificaCimaCores(self, peca):
        pecas = []        
        for index in range(peca.eixoX-1, -1, -1):
            p = self.matris[index][peca.eixoY]
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)
    #Errado
    def modificaEsquerdaCimaCores(self, peca):
        pecas = []
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y +=1
            p = self.matris[index][y]
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)
    #Errado
    def modificaDireitaCimaCores(self, peca):
        pecas = []
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y +=1
            p = self.matris[index][y]
            if p == None: return
            if p.cor == peca.cor:
                for p2 in pecas:
                    p2.cor = peca.cor
                return
            pecas.append(p)

    def podeJogarDireita(self, peca):
        pecas = [peca]
        for coluna in range(peca.eixoY, 8):
            p = self.matris[peca.eixoX][coluna]
            if p == None: return True
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return False
            pecas.append(p)

    def podeJogarEsquerda(self, peca):
        pecas = [peca]
        for coluna in range(peca.eixoY, -1, -1):
            p = self.matris[peca.eixoX][coluna]
            if p == None: return False
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return True
            pecas.append(p)

    def podeJogarBaixo(self, peca):
        pecas = [peca]        
        for index in range(peca.eixoX+1, 8):
            p = self.matris[index][peca.eixoY]
            if p == None: return False
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return False
            pecas.append(p)

    def podeJogarEsquerdaBaixo(self, peca):
        pecas = [peca]
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y -=1
            p = self.matris[index][y]
            if p == None: return False
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return False
            pecas.append(p)

    def podeJogarDireitaBaixo(self, peca):
        pecas = [peca]
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y +=1
            p = self.matris[index][y]
            if p == None: return False
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return False
            pecas.append(p)
    
    def podeJogarCima(self, peca):
        pecas = [peca]        
        for index in range(peca.eixoX-1, -1, -1):
            p = self.matris[index][peca.eixoY]
            if p == None: return False
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return False
            pecas.append(p)
    
    def podeJogarEsquerdaCima(self, peca):
        pecas = [peca]
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y +=1
            p = self.matris[index][y]
            if p == None: return False
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return False
            pecas.append(p)
    
    def podeJogarDireitaCima(self, peca):
        pecas = [peca]
        y = peca.eixoY
        for index in range(peca.eixoX+1, 8-peca.eixoX):
            y +=1
            p = self.matris[index][y]
            if p == None: return False
            if p.cor == peca.cor:
                if len(pecas) > 0:
                    return True
                return False
            pecas.append(p)
    

    def posicoesOndePodeJogar(self, color):
        pecas = []
        for l in list(self.matris):
            for p in list(l):
                if p != None and p.cor != color:
                    pecaNova = peca(p.eixoX, p.eixoY-1, color)
                    if self.podeJogarEsquerda(pecaNova):
                        pecas.append(pecaNova)
                    pecaNova = peca(p.eixoX+1, p.eixoY, color)
                    if self.podeJogarBaixo(pecaNova):
                        pecas.append(pecaNova)
                    pecaNova = peca(p.eixoX-1, p.eixoY, color)
                    if self.podeJogarCima(pecaNova):
                        pecas.append(pecaNova)
                    pecaNova = peca(p.eixoX, p.eixoY+1, color)
                    if self.podeJogarDireita(pecaNova):
                        pecas.append(pecaNova)
                    pecaNova = peca(p.eixoX-1, p.eixoY+1, color)
                    if self.podeJogarDireitaCima(pecaNova):
                        pecas.append(pecaNova)
                    pecaNova = peca(p.eixoX-1, p.eixoY-1, color)
                    if self.podeJogarEsquerdaCima(pecaNova):
                        pecas.append(pecaNova)
                    pecaNova = peca(p.eixoX +1, p.eixoY+1, color)
                    if self.podeJogarEsquerdaBaixo(pecaNova):
                        pecas.append(pecaNova)
                    pecaNova = peca(p.eixoX +1, p.eixoY-1, color)
                    if self.podeJogarEsquerdaBaixo(pecaNova):
                        pecas.append(pecaNova)    
        return pecas

    def contaPecas(self, cor):
        pecas = [p for l in list(self.matris) for p in list(l) if isinstance(p, peca) and p.cor == cor]
        return len(pecas)
    
    def desenha(self, cor):
        print("  "+"  ".join(self.alf))
        # # conta = 0
        pecas = self.posicoesOndePodeJogar(cor)
        for idxr, l in enumerate(self.matris):
            # conta+=1
            linha = str(idxr+1)
            for idx, item in enumerate(l):
                if item == None:
                    if len([x for x in pecas if x.eixoX == idxr and x.eixoY == idx]) > 0:
                        linha += "[*]"
                    else: 
                        linha += "[ ]"
                elif item.cor == color.BRANCO:
                    linha += "[\033[32m\u2666\033[0m]"
                else:
                    linha += "[\033[94m\u2666\033[0m]"
            print(linha, end="\n")

class tipoMenu(Enum):
    NENHUM = None
    iniciarPartida = 1
    adicionarJogador = 2
    adicionarComputador = 3
    removerJogador = 4
    configuracao = 5

class menu():
    def __init__(self):
        self.menus = [tipoMenu.iniciarPartida, tipoMenu.adicionarJogador, tipoMenu.adicionarComputador, tipoMenu.removerJogador, tipoMenu.configuracao]
        self.p = None
    def carregar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.p.topo()
        print('1------------------------------- 1 2--------------------------------2')
        j1 = self.p.buscaJogador(color.PRETO) or "Sem Jogador"
        if isinstance(j1, jogador): j1 = j1.nomeColorido() 
        j2 = self.p.buscaJogador(color.BRANCO) or "Sem Jogador"
        if isinstance(j2, jogador): j2 = j2.nomeColorido() 
        space = '--------------------------------'
        print('|{0}| |{1}|'.format(j1+space[0:32-len(j1)], j2+space[0:32-len(j2)]))
        print('|Pontuação                       | |Pontuação                       |')
        print('1------------------------------- 1 2--------------------------------2')
        print('=====================================================================')
        tempMenu = self.menus[:]

        if self.exibeMenuAdicionarJogador() == False:
            tempMenu.remove(tipoMenu.adicionarJogador)

        if self.exibeMenuIniciarPartida() == False:
            tempMenu.remove(tipoMenu.iniciarPartida)

        if self.exibeMenuRemoverJogador() == False:
            tempMenu.remove(tipoMenu.removerJogador)

        if self.exibeMenuAdicionarComputador() == False:
            tempMenu.remove(tipoMenu.adicionarComputador)

        for menu in tempMenu:
            print(str(menu.value)+'.'+str(menu))
            print('-------------------------------')

    def iniciar(self):
        self.p = partida()
        while True:
            try:
                #os.system('cls') # on windows
                self.carregar()
                opcaoMenu = int(input('\nSelecione menu: '))
                if tipoMenu.iniciarPartida.value == opcaoMenu and self.exibeMenuIniciarPartida() == True:
                    self.p.iniciar()
                elif tipoMenu.adicionarJogador.value == opcaoMenu:
                    nome = str(input('\nNome do Jogador: '))
                    self.p.adicionarJogador(jogador(nome))
                elif tipoMenu.removerJogador.value == opcaoMenu:
                    nome = str(input('\nNome do Jogador: '))
                    self.p.removerJogador(nome)
                else:
                    print('Opção inválida')
            except Exception:
                print('Opção inválida')

    def exibeMenuAdicionarJogador(self):
        return len(self.p.jogadores) <= 2
    
    def exibeMenuRemoverJogador(self):
        return len(self.p.jogadores) >= 1
    
    def exibeMenuIniciarPartida(self):
        return len(self.p.jogadores) == 2
    
    def exibeMenuAdicionarComputador(self):
        return len(self.p.jogadores) == 1


#menu().iniciar()
os.system('cls' if os.name == 'nt' else 'clear')
p2 = partida()
p2.adicionarJogador(jogador('A'))
p2.adicionarJogador(jogador('B'))
p2.iniciar()