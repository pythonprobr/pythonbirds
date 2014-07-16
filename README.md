pythonbirds
===========

Projeto para Ensino de Programação Orientadas a Objetos em Python

## Simplificação do Jogo

1. O jogo será feito considerando que os atores são pontos no plano cartesiano. 
2. A velocidade dos pontos e pequena, de tal forma que a cada passo os pontos se movam apenas para pixels vizinhos.
3. A colisão entre entre pontos ocorre quando eles estão em pixel vizinho

# Classes do Jogo

## Classe Ator

Classe base para todos os atores do jogo.

### Método calcular_posicao

Método que recebe o tempo (float) como parâmetro e retorna uma tupla com 3 elementos, posição horizontal (x), posição
vertical (y) e sinal a ser exibido em tela (caracter).

x e y devem ser números inteiros. Devem ser aproximados utilizando lógica de arredondamento.

### Status

O ator possui os status Ativo e Destruido. Quando destruido, o caracter the apresentação quando for calculada a posição 
deve ser "✝"
