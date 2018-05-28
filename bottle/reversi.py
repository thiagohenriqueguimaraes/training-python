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

class partida():
    def __init__(self):
        self.jogadores = []
        self.tabuleiro = tabuleiro()
        self.jogadorVez = None
        self.cores = [color.BRANCO, color.PRETO]

    def adicionarJogador(self, jogador):
        if len(self.jogadores) == 2:
            return False
            print('Só é permitido dois jogadores')
        jogador.cor = self.cores.pop()
        self.jogadores.append(jogador)
    
    def removerJogador(self, nome):
        for j in self.jogadores:
            if j.nome == nome:
                self.cores.append(j.cor)
                self.jogadores.remove(j)
                break
        print('Jogador não encontrado')

    def buscaNomeJogador(self, cor):
        for j in self.jogadores:
            if j.cor == cor:
                return '\033[91m'+j.nome+'\033[0m'
        return 'Sem Jogador'

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
        if len(self.tabuleiro.pecas) == 64: 
            return True
        pecas = []
        for p in self.tabuleiro.pecas:
            pecas.append(p.cor)
        pecas = list(set(pecas))

        if len(pecas) == 1: 
            return True

        return False
    
    def iniciar(self):
        self.defineVez()
        while(self.fim() == False):
            self.placa()
            self.tabuleiro.desenha()
            novaPeca = None
            while(True):
                posicao = str(input('\nVez do Jogador {}: '.format(self.jogadorVez.nome))).lower()
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

            self.defineVez()

    def placa(self):
        print('______________________________ REVERSI_______________________________')
        print('=====================================================================')
        print('Placar')
        for j in self.jogadores:
            print('Jogador {0}: {1}'.format(j.nome, self.tabuleiro.contaPecas(j.cor)))

class peca():
    def __init__(self, eixoX, eixoY, color):
        self.eixoX = eixoX
        self.eixoY = eixoY
        self.cor = color

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.eixoX == other.eixoX and self.eixoY == other.eixoY 

class jogador():
    def __init__(self, nome):
        self.nome = nome
        self.cor = None

    def jogar(self, x, y):
        return peca(x, y, self.cor)

class tabuleiro():
    def __init__(self):
        self.alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.pecas = [peca(3,3, color.BRANCO), peca(4,4, color.BRANCO), peca(4,3, color.PRETO),peca(3,4, color.PRETO)]
    
    def pecaExiste(self, peca):
        for p in self.pecas:
            if p == peca:
                return True
        return False

    def adicionaPeca(self, peca):
        for p in self.pecas:
            if(p == peca):
                return False
        self.pecas.append(peca)

    def setaCor(self, x, y):
        for peca in self.pecas:
            if(peca.eixoX == x and peca.eixoY == y):
                return peca.cor
        return color.NENHUM

    def contaPecas(self, cor):
        conta = 0
        for p in self.pecas:
            if p.cor == cor:
                conta+= 1
        return conta
    
    def desenha(self, tamanho=8):
        print("  "+"  ".join(self.alf))
            
        for l in range(tamanho):
            linha = str(l+1)
            for c in range(tamanho):
                color = self.setaCor(l,c)
                if color == color.BRANCO:
                    linha += "[\033[32m\u2666\033[0m]"
                elif color == color.PRETO:
                    linha += "[\033[94m\u2666\033[0m]"
                else:
                    linha += "[ ]"
            print(linha,end='\n')

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
        os.system('cls') # on windows
        os.system('cls' if os.name == 'nt' else 'clear')
        print('______________________________ \033[91mREVERSI\033[0m_______________________________')
        print('=====================================================================')
        print('1------------------------------- 1 2--------------------------------2')
        j1 = self.p.buscaNomeJogador(color.PRETO)
        j2 = self.p.buscaNomeJogador(color.BRANCO)
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

menu().iniciar()
