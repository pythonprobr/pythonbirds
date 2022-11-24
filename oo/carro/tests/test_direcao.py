import pytest
from oo.carro.direcao import Direcao


def test_valor_inicial_de_direcao_eh_norte():
    # Dado uma direção recém instanciada
    direcao = Direcao()

    # Seu valor inicial deve ser 'Norte'
    assert direcao.valor == 'Norte'


@pytest.mark.parametrize('numero_giros, valor_esperado', [
    (1, 'Leste'),
    (2, 'Sul'),
    (3, 'Oeste'),
    (4, 'Norte'),
    (5, 'Leste'),
])
def test_valor_de_direcao_apo_giros_a_direita(numero_giros, valor_esperado):
    # Dado uma direção recém instanciada
    direcao = Direcao()

    # e certo número de giros
    for _ in range(numero_giros):
        direcao.girar_a_direita()

    # direcao deve possuir valor esperado
    assert direcao.valor == valor_esperado


@pytest.mark.parametrize('numero_giros, valor_esperado', [
    (1, 'Oeste'),
    (2, 'Sul'),
    (3, 'Leste'),
    (4, 'Norte'),
    (5, 'Oeste')
])
def test_valor_de_direcao_apo_giros_a_esquerda(numero_giros, valor_esperado):
    # Dado uma direção recém instanciada
    direcao = Direcao()

    # e certo número de giros
    for _ in range(numero_giros):
        direcao.girar_a_esquerda()

    # direcao deve possuir valor esperado
    assert direcao.valor == valor_esperado
