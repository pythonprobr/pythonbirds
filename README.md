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

Método que recebe o tempo (float) como parâmetro e retorna uma tupla com 2 elementos, posição horizontal (x) como 
primeiro elemento e posição vertical (y) como segundo

### Método Status

O ator possui os status Ativo e Destruido. Além disso o status deve ser dependente do tempo. Ou seja, se o ator foi 
destruido no tempo t, ele deve possuir status ativo antes desse tempo e Destruido após esse tempo.
 

## Método sinal

O método sinal retorna 'A' quando o ator tem status Ativo e '✝' caso contrário.

### Método colidir

O método colidir deve ser executada para executar a ação de colisão. Colisão só ocorre com atores ativos e que estejam
em pixels vizinhos

## Classe Obstaculo

Classe que representa objstaculos na fase e que podem ser destruidos por pássaros. Herda de ator. Seu caracter de 
representação é a letra "O"

### Status

Um obstáculo ao ter seu status alterado para DESTRUIDO deve ter seu caracter de apresentação alterado para " " (vazio).
Assim ele vai "sumir" da tela


