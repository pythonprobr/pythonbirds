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

Classe que representa obstáculos na fase e que podem ser destruidos por pássaros. Herda de ator. Seu caracter de 
representação é a letra "O"

### Status

Um obstáculo ao ter seu status alterado para DESTRUIDO deve ter seu caracter de apresentação alterado para " " (vazio).
Assim ele vai "sumir" da tela

## Classe Porco

Classe que representa porcos na fase e que podem ser destruidos por pássaros. Herda de ator. Seu caracter de 
representação é a letra "☺"

## Passaro

Classe base de todos os passáros. Cada tipo possui uma velocidade de lançamento (v). No lançamento o jogador escolhe o 
ângulo (teta), em graus, no qual o passáro deve ser lançado. O lançamento respeita as regras de lançamento oblìquo com 
gravidade (G) constante e igual a 10 m/s^2.

### Método Lancar

O método lançar recebe o ângulo, em graus, que será feito o lançamento. Cada pássaro deve armazenar esse valor e tempo
de lançamento para cálculo de sua posíção. Lembrar que o tempo das fórmulas é delta_t=Tfinal-Tinicialself

### Método posicao_horizontal

Fórmula X=X0+v*cos(teta)*delta_t.

### Método posicao_vertical

Fórmula Y=Y0+v*sen(teta)delta_t-(G*delta_t^2)/2.
    



