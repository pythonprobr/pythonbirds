Python Birds
===========

Projeto para Ensino de Programação Orientadas a Objetos em Python.

A versão utilizada para desenvolvimento foi Python 3.4

# Abordagem

Baixar a versão apenas com estrutura do projeto (branch diversao) em:



Os testes se encontram dentro do pacote "testes" e servem para definir a dinâmica das classes. Para rodar todos testes, execute

    python executor_de_testes.py
    
Explicação detalhada sobre classes e métodos se encontram em [#jogo]

## Ordem de desenvolvimento

A ordem preferida é começar pelos atores, seguindo a ordem dos testes presentes no script atores_testes.py.
Depois passar para a fase_teste.py, onde é implementada uma fase.

Após o desenvolvimento é possível emular um jogo que termina em vitória rodando:

    python fase_testes.py

É possível jogar a fase rodando:

    python python_birds.py

Para jogar, aperte enter, digite o ângulo de lançamento e aperte enter novamente.
Demonstração no vídeo:

[Python Birds](https:youtube.com)

## script atores.py

Contém todos atores do projeto.

## script fase.py

Contém classes respectivas a fase e ponto do plano cartesiano

## script placa_grafica.py

Contém lógica para rodar jogo e exibir no console.

# Simplificação do Jogo [jogo]

1. Atores são pontos (um caracter) no plano cartesiano. 
2. A velocidade dos pontos e pequena, de tal forma que a cada passo os pontos se movam apenas para pontos vizinhos.
3. A colisão entre pontos ocorre quando eles estão em ponto vizinho

A seguir segue a especificação detalhada do jogo.

## Classe Ator

Classe base para todos os atores do jogo.

### Método calcular_posicao

Método que recebe o tempo (float) como parâmetro e retorna uma tupla com 2 elementos, posição horizontal (x) como 
primeiro elemento e posição vertical (y) como segundo.

### Método status

O ator possui os status Ativo ou Destruido. Além disso o status deve ser dependente do tempo. Ou seja, se o ator foi 
destruido no tempo t, ele deve possuir status Ativo antes desse tempo e Destruido após.
 

## Método sinal

O método sinal retorna 'A' quando o ator tem status Ativo e '+' caso contrário. Também é depende do tempo.

### Método colidir

O método colidir deve ser executada para executar a ação de colisão. Colisão só ocorre com atores ativos e que estejam
em pontos vizinhos. O ator deve guardar o tempo de colisão para calcular corretamente seu status.

## Classe Obstaculo

Classe que representa obstáculos na fase e que podem ser destruidos por pássaros. Herda de ator. Seu caracter de 
representação é a letra "O" quando Ativo.

### Status

Um obstáculo ao ter seu status alterado para DESTRUIDO deve ter seu caracter de apresentação alterado para " " (vazio).
Assim ele vai "sumir" da tela.

## Classe Porco

Classe que representa porcos na fase e que podem ser destruidos por pássaros. Herda de ator. Seu caracter de 
representação é a o caracter "@".

## Passaro

Classe base de todos os passáros. Cada tipo possui uma velocidade de lançamento (v). No lançamento o jogador escolhe o 
ângulo (teta), em graus, no qual o passáro deve ser lançado. O lançamento respeita as regras de lançamento oblíquo com 
gravidade (G) constante e igual a 10 m/s^2.

### Método lancar

O método lançar recebe o ângulo, em graus, que será feito o lançamento. Cada pássaro deve armazenar esse valor e o tempo
de lançamento para cálculo de sua posíção. Lembrar que o tempo das fórmulas é delta_t = Tfinal - Tinicial

### Método posicao_horizontal

Fórmula X=X0+v*cos(teta)*delta_t.

### Método posicao_vertical

Fórmula Y=Y0+v*sen(teta)delta_t-(G*delta_t^2)/2.
    

### Método de colidir_com_chaoo

Toda vez que o pássaro colidir com o chão (y=0) ele deve ser destruido.

## Classe Passaro Vermelho

Tipo de Pássaro que representa o pássaro vermelho. Possui velocidade de lançamento igual a 20 m/s. Seu caracter é "D".

## Classe Passaro Amarelo

Tipo de Pássaro que representa o pássaro amarelo. Possui velocidade de lançamento igual a 30 m/s. Seu caracter é ">".

## Classe Fase

Classe responsável por organizar atores e transformarem os dados em pontos a serem representados na tela.

### Método adicionar_obstaculo

Método que adiciona um ou mais obstáculos na fase

### Método adicionar_porco

Método que adiciona um ou mais porcos na fase

### Método adicionar_passaro

Método que adiciona um ou mais pássaros na fase

### Método acabou

Método que recebe o tempo do jogo e retorna verdadeiro (True) se o jogo acabou e (False) caso contrário.
O jogo pode acabar por duas razôes:

1. Todos porcos foram destruidos
2. Não há mais pássaros a serem lançados

### Método status

Recebe o tempo como parâmetro e retorna mensagem com status do jogo.

1. Se o jogo está em andamento, retorna mensagem "Jogo em andamento."
2. Se o jogo acabou e não existem porcos ativos, retorna a mensagem "Jogo em encerrado. Você ganhou!"
3. Se o jogo acabou e existem porcos ativos, retorna a mensagem "Jogo em encerrado. Você perdeu!"

### Método lancar

Recebe o ângulo e o tempo do lançamento. Deve delegar o lançamento ao primeiro pássaro ativo da lista de pássaros.

### Método calcular_pontos

Método que executa a lógica do jogo a cada passo (tempo), retornando pontos a serem exibidos na tela.

Ele deve:

1. Calcular a posição de cada pássaro, verificando se ele colidiu com algum obstáculo, porco ou chão.
2. Retornar instâncias da classe Ponto, informando x,y e caracter respectivo a cada ator.

### Divirta-se!!!!

Powered by [Python Pro](http://adm.python.pro.br)