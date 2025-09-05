# 🎮 Tetris The New Game

## 📌 Sobre o Projeto
Este projeto é uma implementação do clássico **Tetris**, desenvolvido em **Python 3.12.7** com a biblioteca `curses` para exibição no terminal.  
Além das peças tradicionais, o jogo conta com uma **peça especial "bomba" (🧨)** que destrói blocos em uma área 3x3, adicionando um diferencial estratégico ao gameplay.
Manual de Instruções para o usuário incluso no projeto juntamento com o relatório completo de utilização.

O projeto foi desenvolvido no contexto da disciplina **MI-Algoritmos I**.

---

## ⚙️ Funcionalidades
- Tabuleiro 20x10 exibido no terminal.  
- Peças clássicas do Tetris (I, O, T, S, Z, J, L).  
- Peça especial **Bomba (🧨)** que remove blocos ao redor.  
- Sistema de **pontuação** baseado em linhas eliminadas:
  - 1 linha = 100 pontos  
  - 2 linhas = 400 pontos  
  - 3 linhas = 600 pontos  
  - 4 linhas = 800 pontos (Tetris!)  
- **Aumento de dificuldade**: a velocidade de queda das peças acelera conforme a pontuação aumenta.  
- **Game Over** quando não há mais espaço para novas peças.  

---

## 🎮 Controles
Durante o jogo:
- **W** → Rotacionar peça  
- **A** → Mover para esquerda  
- **D** → Mover para direita  
- **S** → Descer mais rápido  

⚠️ **Atenção:** não mantenha as teclas pressionadas, pois isso pode causar problemas na exibição.  
Certifique-se também de **desativar o CAPS LOCK**.  

---

## 🔧 MELHORIAS 
Melhorias a serem feitas: O código está a disposição de melhorias de algumas funcionalidades, bem como a movimentação dos Tetriminos. Possivelmente poderia ser utilizada a biblioteca curses ou Keyboard e numpy para manipulação das matrizes.
Outro ponto de melhoria seria exibir a próxima peça para o usuário e uma aba com as melhores pontuações feitas pelo jogador, fazendo com que ele buscar sempre bater o seu recorde.

---

## 🛠️ Requisitos
- **Sistema Operacional**: Windows 10  
- **Versão do Python**: 3.12.7  
- Dependências:
  ```bash
  pip install windows-curses
