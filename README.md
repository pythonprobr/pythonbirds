Python Birds
===========

Essa versão é a mais simples. Ela não contém replay nem reset, de forma que o jogo não pode retroceder.

Para versão mais complexa, acesse a branch [diversao](https://github.com/pythonprobr/pythonbirds/tree/diversao)

Projeto para Ensino de Programação Orientadas a Objetos em Python.

A versão utilizada para desenvolvimento foi Python 3.4

Um vídeo fala mais que 1000 palavras: [Python Birds](https://www.youtube.com/watch?v=b899h0lNd7U&list=PLA05yVJtRWYTm0sIa6n56UpCjCsR5ekla)

# Contribuidores

* [Giovane Liberato](https://github.com/giovaneliberato)
* [Guido Luz](https://github.com/GuidoBR)
* [Michel Amaral](https://github.com/michelamaral)
* [Renzo Nuccitelli](https://github.com/renzon)

# Abordagem

Instalar [Python 3](https://www.python.org/download/).

Baixar o zip do projeto (botão Download Zip) 

Os testes se encontram dentro do pacote "testes" e servem para definir a dinâmica das classes. Para rodar todos testes, execute:

    python executor_de_testes.py
    
Explicação detalhada sobre classes e métodos se encontram nos scripts atores.py e fase.py.

## Ordem de desenvolvimento

A ordem preferida é começar pelos atores, seguindo a ordem dos testes presentes no script atores_testes.py.
Depois passar para a fase_teste.py, onde é implementada uma fase.

É possível emular um jogo que termina em vitória rodando:

    python fase_testes.py

É possível jogar a fase rodando:

    python placa_grafica_tkinter.py

Para jogar, utilize as setas para cima e para baixo. Para lançar, utilize a tecla enter ou espaço.
Demonstração nos vídeos:

[Python Birds](https://www.youtube.com/watch?v=b899h0lNd7U&list=PLA05yVJtRWYTm0sIa6n56UpCjCsR5ekla)

## script atores.py

Contém todos atores do projeto.

## script fase.py

Contém classes respectivas a fase e ponto do plano cartesiano

## script placa_grafica.py

Contém lógica para rodar jogo e exibir no console.

## script placa_grafica_tkinter.py

Contém lógica para rodar jogo em uma janela.

# Simplificação do Jogo

1. Atores são pontos no plano cartesiano. 
2. A velocidade dos pontos é pequena, de tal forma que a cada passo os atores se movam apenas para pontos vizinhos.
3. A colisão entre pontos ocorre quando eles estão em ponto vizinho, de acordo com valor de intervalo.

A seguir é apresentada a especificação detalhada do jogo.

## Classe Ator

Classe base para todos atores do jogo.

### Método calcular_posicao

Método que recebe o tempo (float) como parâmetro e retorna uma tupla com 2 elementos, posição horizontal (x) como 
primeiro elemento e posição vertical (y) como segundo.

### Método colidir

O método colidir executa a lógica de colisão. A colisão só ocorre com atores ativos e que estejam
em pontos vizinhos. Ao colidir, os atores envolvidos devem ter seus status alterado para DESTRUIDO

## Classe Obstaculo

Classe que representa obstáculos na fase e que podem ser destruídos por pássaros. Herda de ator. Seu caracter de 
representação é a letra "O", quando ATIVO.

### Status

Um obstáculo ao ter seu status alterado para DESTRUIDO deve ter seu caracter de apresentação alterado para " " (vazio).
Assim ele vai "sumir" da tela.

## Classe Porco

Classe que representa porcos na fase e que podem ser destruídos por pássaros. Herda de ator. Seu caracter de 
representação é a o caracter "@".

### Status

Um obstáculo ao ter seu status alterado para DESTRUIDO deve ter seu caracter de apresentação alterado para "+" (sinal de mais).
Assim sua imagem é alterada para a de porco morto.

## Passaro

Classe base de todos os passáros. Cada tipo possui uma velocidade de lançamento (v). No lançamento o jogador escolhe o 
ângulo (teta), em graus, no qual o passáro deve ser lançado. O lançamento respeita as regras de lançamento oblíquo com 
gravidade (GRAVIDADE) constante e igual a 10 m/s^2.

### Método lancar

O método lançar recebe o ângulo, em graus, que será feito o lançamento. Ele deve ser convertido para radianos.
Cada pássaro deve armazenar esse valor e o tempo
de lançamento para cálculo de sua posíção. Lembrar que o tempo das fórmulas é delta_t = T_final - T_inicial.


### Método de colidir_com_chao

Todo pássaro que colidir com o chão (y<=0) deve ser destruído.

### Método foi_lançado

Esse método deve retornar verdadadeiro se o pássaro foi lançado (tempo de lançamento é None).
Caso contrário deve retornar falso.

### Lançamento

Se o pássaro ainda não foi lançado, o pássaro deve permanecer na posição inicial.
  
Caso tenha sido lançado e seu status esteja ATIVO, sua posição deve ser calculada de acordo com o lançamento oblíquo.
Nesse caso, delta_t vai ser igual ao tempo do jogo menos o tempo do lançamento.
  
Caso contrário, ele deve retornar a posição onde colidiu.

#### Método posicao_horizontal

Fórmula X=X0+v\*cos(teta)\*delta_t.

#### Método posicao_vertical

Fórmula Y=Y0+v\*sen(teta)delta_t-(G\*delta_t^2)/2.
    

## Classe Passaro Vermelho

Tipo de Pássaro que representa o pássaro vermelho. Possui velocidade de lançamento igual a 20 m/s. 
Seu caracter quanto ATIVO é "V". Quando DESTRUIDO é "v".

## Classe Passaro Amarelo

Tipo de Pássaro que representa o pássaro amarelo. Possui velocidade de lançamento igual a 30 m/s.
Seu caracter quanto DESTRUIDO é "a".

## Classe Fase

Classe responsável por organizar atores e transformar os dados em pontos a serem representados na tela.

### Método adicionar_obstaculo

Método que adiciona um ou mais obstáculos na fase.

### Método adicionar_porco

Método que adiciona um ou mais porcos na fase.

### Método adicionar_passaro

Método que adiciona um ou mais pássaros na fase.


### Método status

Recebe o tempo como parâmetro e retorna status do jogo.

1. Se o jogo está em andamento, retorna status "EM_ANDAMENTO";
2. Se o jogo acabou e não existem porcos ativos, retorna STATUS "VITORIA";
3. Se o jogo acabou e existem porcos ativos, retorna status "DERROTA".

### Método lancar

Recebe o ângulo e o tempo do lançamento. Deve delegar o lançamento ao primeiro pássaro ATIVO da lista de pássaros que 
ainda não foi lançado.

### Método calcular_pontos

Método que executa a lógica do jogo a cada passo (tempo), retornando pontos a serem exibidos na tela.

Ele deve:

1. Calcular a posição de cada pássaro, verificando se ele colidiu com algum obstáculo, porco ou chão.
2. Retornar instâncias da classe Ponto, informando x, y e caracter respectivo a cada ator.

### Divirta-se!!!!

Powered by [Python Pro](http://adm.python.pro.br)

# Observação Importante

Esse projeto usa somente o interpretador padrão do Python. Para fazer jogos com mais interatividade, existe a biblioteca Pygame. Ela não foi utilizada por motivos de simplicidade, para evitar que o aluno iniciante tenha dificuldades na hora de instalar o projeto.

Contudo o Estevão Fonseca fez um versão com essa biblioteca, confira o projeto:

<https://github.com/estevaofon/angry-birds-python>

Ele também colocou esse [vídeo no Youtube](https://www.youtube.com/watch?v=B7G5JtCFepE). 
